#!/usr/bin/env python3
"""Static checks for the n8n workflow export (no n8n instance needed).

Usage: python3 scripts/validate_workflow.py workflows/ai-hospital-incident-management-gahar.json
Checks: valid JSON, unique node names, every connection endpoint exists, every non-trigger /
non-sub-node is reachable from a trigger, and every Code node parses as JavaScript (needs `node`).
"""
import json, subprocess, sys, tempfile, os

path = sys.argv[1] if len(sys.argv) > 1 else "workflows/ai-hospital-incident-management-gahar.json"
wf = json.load(open(path, encoding="utf-8"))
nodes = {n["name"]: n for n in wf["nodes"]}
errors = []

if len(nodes) != len(wf["nodes"]):
    errors.append("duplicate node names")

edges = []
for src, kinds in wf["connections"].items():
    if src not in nodes:
        errors.append("connection source missing: " + src)
    for kind, outs in kinds.items():
        for out in outs:
            for t in out:
                if t["node"] not in nodes:
                    errors.append("connection target missing: %s -> %s" % (src, t["node"]))
                edges.append((src, t["node"], kind))

TRIGGERS = ("Trigger", "webhook", "emailReadImap", "formTrigger", "manualTrigger", "scheduleTrigger", "errorTrigger")
roots = [n for n, v in nodes.items() if any(v["type"].endswith(t) or t in v["type"] for t in TRIGGERS)]
seen, stack = set(roots), list(roots)
while stack:
    cur = stack.pop()
    for s, t, k in edges:
        if k == "main" and s == cur and t not in seen:
            seen.add(t); stack.append(t)
# sub-nodes (models, tools, embeddings, loaders, splitters) feed a main node through ai_* links
sub = {s for s, t, k in edges if k != "main"}
for n, v in nodes.items():
    if n not in seen and n not in sub and v["type"] != "n8n-nodes-base.stickyNote":
        errors.append("unreachable node: " + n)

for n, v in nodes.items():
    if v["type"] == "n8n-nodes-base.code":
        js = v["parameters"]["jsCode"]
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write("(function(){ const $json={},$={};\n" + js + "\n});")
            tmp = f.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode:
            errors.append("JS syntax error in '%s': %s" % (n, r.stderr.strip().splitlines()[-1] if r.stderr else "?"))

print("nodes:", len(nodes), "| connections:", len(edges), "| triggers:", len(roots))
if errors:
    print("FAILED"); [print(" -", e) for e in errors]; sys.exit(1)
print("OK - structure valid")

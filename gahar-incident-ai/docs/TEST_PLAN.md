# Test plan (expected results; actuals to be filled after running)

Rows come from `data/synthetic_incidents.csv`. Record run ID, screenshot, pass/fail and defect ticket per case. A parsing success is not a clinical-safety result.

## Per-stage minimum suite (3 normal, 1 edge, 1 unsafe)

| # | Stage | Case | Input | Expected | Actual |
|---|---|---|---|---|---|
| 1 | Intake / PHI gate | Normal x3 | rows 1, 3, 4 | `phi_status=clean`, ID `INC-…-XXXX` unique per run | Pending |
| 2 | Intake | Edge: missing department | row 6 | Validation fails, polite request to reporter, row in `ValidationErrors`, no routing | Pending |
| 3 | PHI gate | Unsafe: phone + injection | row 5 | Quarantine, no model call, Telegram notice, redacted row in `Quarantine` | Pending |
| 4 | Triage | Normal: clinical / facility / security | rows 1, 3, 4 | Routes clinical / facility / security | Pending |
| 5 | Triage | Edge: conflicting domains | row 7 | `manual_triage`, no AI analysis, notice | Pending |
| 6 | Specialist + RAG | Normal x3 | rows 1, 3, 4 | JSON with facts/hypotheses/missing evidence; citations only if retrieved | Pending |
| 7 | Specialist + RAG | Edge: no relevant standard | any, KB not loaded | `gahar_citations=[]`, `citation_status=unverified` | Pending |
| 8 | Judge / hard stop | Unsafe output | force identifier in output | Output quarantine, hard stop | Pending |
| 9 | Approval backend | Normal: authorized reply | reply with correct CODE | Register `APPROVED`, owner/due saved, Telegram notice | Pending |
| 10 | Approval backend | Unsafe: spoofed sender / wrong code | reply from unlisted address | Rejected, `UnauthorizedAttempts` row, hard-stop alert, nothing released | Pending |

## End-to-end scenarios
1. **Typical - medication near miss (row 1):** all stages, draft does not invent injury, email, authorized approval, action `OPEN`, dashboard updates.
2. **Complex - fall with ambiguous harm (row 2):** `Unknown` harm escalates; no definitive RCA; clarification path.
3. **Unsafe - identifier + injection (row 5):** quarantine, refusal, no external call, issue-log entry.
4. **Sentinel timers (row 8):** urgent alert shows 48 h notify-by and 45-day RCA-due dates; system states it does not decide reportability.

## KPI measurement
| KPI | Baseline | Target | Method | Actual |
|---|---|---|---|---|
| Draft time | 20 min (assumed) | <= 10 min | Time 10 synthetic reports manually vs `draft_seconds` | Pending |
| Routing accuracy | n/m | >= 90% | Gold-labeled benchmark | Pending |
| High-risk approval | n/m | 100% | Audit `ActionRegister` vs `UnauthorizedAttempts` | Pending |
| Action owner coverage | n/m | 100% | Approved rows with owner and due date | Pending |
| Officer effort | n/m | >= 4/5 | Post-test survey | Pending |

Judge calibration: two raters who did not build the stage score the same outputs; compare with judge scores and adjust the rubric. Not done yet.

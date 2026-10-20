# Issue log (A5)

| No. | Issue | Stage | Cause | Fix | Status |
|---|---|---|---|---|---|
| 1 | Original export dropped incident fields after agent nodes (`Tag Report` read agent output only) | Specialist | AI Agent returns only `output` | `Tag Report` rebuilds from `Validate Envelope` | Fixed in build, untested live |
| 2 | Merge node had a single input and would wait | Specialist | Leftover from 4-branch design | Removed; `Tag Report` -> `JS Parser` | Fixed |
| 3 | Vector stores were empty (nothing ingested) | Specialist | No loader | Loader lane downloads GAHAR 2025 handbook; all stores share one key | Fixed in build, untested live |
| 4 | Keyword routing defaulted unknowns to "safety" | Triage | Fall-through default | 0 or >1 domain -> `manual_triage` | Fixed |
| 5 | Temporary IDs could collide | Intake | Second-resolution timestamp | Random 4-char suffix | Fixed |
| 6 | Quarantine log stored raw text with identifiers | PHI gate | Auto-map of whole item | Log redacted text only | Fixed |
| 7 | Telegram messages had literal `\\n`; chat ID hard-coded | Notify | Original export | Real newlines; `TELEGRAM_CHAT_ID` env | Fixed |
| 8 | Approval used an unauthenticated resume webhook | Approval | No sender/identity check | Allow-list + one-time code + token, fail closed | Fixed in build, untested live |
| 9 | Final audit output was not parsed or schema-checked | Audit | Prompt/schema mismatch | `Parse Audit` normalizes issues/actions/owners | Fixed |
| 10 | PHI gate cannot detect personal names in free text | PHI gate | Regex-only | Needs adversarial testing; consider NER or clinician review | Open |
| 11 | In-memory vector store is lost on restart | Specialist | n8n in-memory store | Re-run loader; consider persistent store for a pilot | Open |
| 12 | Judge and generator share a vendor | Evaluation | Single OpenAI credential | Swap judge model family; calibrate with human raters | Open |
| 13 | Parameter formats unverified on the target n8n version | All | Not run live | Import, open each node, fix any schema warnings | Open |

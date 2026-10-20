# GAHAR standards reference (researched 18 Oct 2026)

What the web check found, and how the workflow uses it. Verify against gahar.gov.eg before relying on it for accreditation.

| Finding | Source | Used in workflow |
|---|---|---|
| Current hospital handbook is the **GAHAR Handbook for Hospital Accreditation Standards, 2025 edition**, described as the **second edition** (first: 2021). Four sections: prerequisites, patient-centered, organization-centered, academic/teaching hospitals (16 chapters). | [Handbook (v3 PDF)](https://gahar.gov.eg/upload/gahar-handbook-for-hospital-accreditation-standards-2025--v3.pdf) · [v2 PDF](https://gahar.gov.eg/upload/gahar-handbook-for-hospitals-accreditation-standards-2025---v2.pdf) | Knowledge-base loader downloads the v2 PDF and embeds it. If you prefer v3, change the URL in node *Download GAHAR Handbook 2025*. |
| The handbook carries a "Summary of Changes" per chapter versus 2021; the national safety list was renamed **GAHAR Safety Requirements (GSR)**, with a new GSR on cardiopulmonary resuscitation (CSS.05). | Same handbook | Specialist prompts cite only codes returned by retrieval. |
| **Sentinel events: notify GAHAR within 48 hours; submit RCA with corrective plan within 45 days** (late RCA can risk accreditation suspension; see standard QPI.11). | Handbook v3; GAHAR news item "Updates on Accreditation Procedures" (12 Apr 2026) | `Validate Envelope` computes `gahar_notify_by` / `rca_due_by`; urgent alert and review email show them. The system never decides reportability. |
| A GAHAR **Manual for Management of Reportable Events (2025)** exists. | [GAHAR manual](https://www.gahar.gov.eg/upload/gahar-manual-for-reportable-events.pdf) | Referenced in alerts for the officer's reportability assessment. |
| A sentinel-event mailbox appears in GAHAR's 2025 *primary healthcare* provisional handbook. Not confirmed for hospitals. | [PHC provisional 2025](https://gahar.gov.eg/upload/phc-provisional--a.s-2025-.pdf) | **Not used.** Confirm the correct reporting channel with GAHAR. |
| Latest GAHAR publications found are the 2025 hospital edition and a 2026 ambulatory handbook; no newer hospital edition was found. | [Accreditation updates](https://gahar.gov.eg/en/news/updates-on-accreditation-procedures) | Re-check before pitching; refresh via the monthly trigger. |

Caveats: the search tool returned fragments of the PDFs, so clause-level wording was not verified; the 48 h / 45 day figures come from the handbook summary and the April 2026 notice and should be checked against QPI.11 in the PDF. The handbook's effective date was not explicit in the copy read.

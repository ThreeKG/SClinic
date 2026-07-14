# SClinic

Project workspace for the SClinic audit, planning, evidence, and client-facing deliverables.

## Structure

- `Docs & Planing/`
  - `deliverables/` — exported PDF/PPTX and related render files
  - `evidence/` — live-site captures, headers, robots, sitemap, Lighthouse output
  - `notes/` — working research notes
  - `plans/` — implementation plans
- `scripts/` — build scripts for the report and deck
- `IDEA.md` — original source brief

## Main outputs

- Executive report: `Docs & Planing/deliverables/SClinic_Executive_Report.pdf`
- Client deck: `Docs & Planing/deliverables/SClinic_Client_Deck.pptx`

## Regenerate

```bash
python3 scripts/build_client_materials.py
```

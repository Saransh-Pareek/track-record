# Track Record

Validating Aurizon Network's track condition metrics (CETS Modules 1 and 9) on real operational data.
UQ DATA7901/DATA7902 capstone, supervised by Dr Archie Chapman, sponsored by The ARCS Group.

**Status:** project scaffold only. No pipeline code yet; the data has not arrived.

## Layout
- `contracts/` — one data contract per table
- `src/track_record/` — `ingest`, `validate`, `transform`, `metrics`, `synthetic`
- `tests/` — unit, contract and end-to-end tests
- `notebooks/` — exploration and characterisation
- `docs/` — ADR log (design decisions) and AI-use log
- `data/` — local only, never committed

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

Raw data is confidential and must never be committed. Credentials go in `.env` (git-ignored); see `.env.example`.

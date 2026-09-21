# Source code

- `track_record/synthetic/generate.py` — synthetic track geometry generator. Builds sections to the schema in Table 1 of the proposal, with planted defects, deterioration between runs, and maintenance resets, so pipeline code can be written and tested before the operational data arrives. All thresholds in it are illustrative placeholders, not CETS values.

Run it with:

```
python -m track_record.synthetic.generate
```

Pipeline code (ingest, validate, transform, metrics) is added once the data arrives.

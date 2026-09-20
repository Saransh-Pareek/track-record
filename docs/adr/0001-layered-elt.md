# ADR 0001: Use a layered ELT pipeline

Status: proposed

Decision: store data exactly as received (raw), then stage, curate and compute metrics in separate layers.
Why: every result can be traced back to its source file, and bad batches stop at the staged layer.

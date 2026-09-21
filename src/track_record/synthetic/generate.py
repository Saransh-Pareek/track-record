"""
Synthetic track geometry generator for Track Record.

Produces records with the same shape as the Aurizon delivery described in
Table 1 of the proposal, so that pipeline code can be written and tested
before the operational data arrives.

NOTE: every threshold below is an illustrative placeholder, not a CETS value.
Real limits come from Module 9, Tables 9.3 and 9.13, and are applied only to
the operational data.
"""
import numpy as np, pandas as pd

RNG = np.random.default_rng(20260921)
STEP = 0.5          # metres between samples
SECTION_LEN = 1000  # metres per oTCI section
N_SECTIONS = 40
N_RUNS = 6          # six inspection runs, roughly three years at two a year

# illustrative placeholder limits (mm) — not CETS values
LIMITS = {"twist_3m": {"m3": 12, "d14": 16, "d7": 20, "d1": 25},
          "top_left": {"m3": 14, "d14": 18, "d7": 23, "d1": 28},
          "gauge":    {"m3": 10, "d14": 14, "d7": 18, "d1": 22}}


def correlated_noise(n, sigma, length_scale=40):
    """Random roughness with spatial correlation, so neighbouring samples relate."""
    white = RNG.normal(0, 1, n + length_scale)
    kernel = np.ones(length_scale) / length_scale
    smooth = np.convolve(white, kernel, mode="valid")[:n]
    return smooth / smooth.std() * sigma


def build_section(section_id, run, base_state, defects):
    n = int(SECTION_LEN / STEP)
    chainage = np.arange(n) * STEP / 1000 + section_id * SECTION_LEN / 1000
    rows = {"section_id": section_id, "run_id": run, "chainage_km": chainage}
    for param, sigma in (("top_left", 2.2), ("twist_3m", 1.8), ("gauge", 1.5)):
        signal = base_state[param] + correlated_noise(n, sigma)
        # deterioration: roughness grows a little with every run
        signal = signal * (1 + 0.06 * run)
        for pos, size, p in defects:
            if p != param:
                continue
            idx = int(pos / STEP)
            width = 12
            lo, hi = max(0, idx - width), min(n, idx + width)
            bump = size * np.exp(-0.5 * ((np.arange(lo, hi) - idx) / 4.0) ** 2)
            signal[lo:hi] += bump * (1 + 0.05 * run)
        rows[param] = signal
    return pd.DataFrame(rows)


def generate():
    frames = []
    base_state = {p: RNG.normal(0, 0.4) for p in ("top_left", "twist_3m", "gauge")}
    defect_plan = {}
    for s in range(N_SECTIONS):
        defects = []
        for _ in range(RNG.poisson(0.8)):          # some sections get a local defect
            param = RNG.choice(["twist_3m", "top_left", "gauge"])
            defects.append((RNG.uniform(50, 950), RNG.uniform(8, 26), param))
        defect_plan[s] = defects
    for run in range(N_RUNS):
        for s in range(N_SECTIONS):
            frames.append(build_section(s, run, base_state, defect_plan[s]))
    return pd.concat(frames, ignore_index=True), defect_plan


def priority(value, param):
    lim = LIMITS[param]
    v = abs(value)
    if v >= lim["d1"]:
        return "d1"
    if v >= lim["d7"]:
        return "d7"
    if v >= lim["d14"]:
        return "d14"
    if v >= lim["m3"]:
        return "m3"
    return None


def analyse(df):
    out = []
    for (s, r), g in df.groupby(["section_id", "run_id"]):
        row = {"section_id": s, "run_id": r}
        pcis = []
        worst = None
        for param in ("top_left", "twist_3m", "gauge"):
            v = g[param].values
            stat = np.abs(v).mean() + 3 * v.std(ddof=1)        # ATIS-style statistic
            pci = 100 * stat / LIMITS[param]["m3"]              # PCI as % of the m3 limit
            pcis.append(pci)
            peak = np.abs(v).max()
            p = priority(peak, param)
            order = {"d1": 4, "d7": 3, "d14": 2, "m3": 1, None: 0}
            if order[p] > order[worst]:
                worst = p
            row[f"peak_{param}"] = peak
        row["oTCI"] = float(np.mean(pcis))
        row["worst_priority"] = worst
        out.append(row)
    return pd.DataFrame(out)


if __name__ == "__main__":
    df, plan = generate()
    res = analyse(df)
    median_level = res["oTCI"].median()
    acceptable = res[res["oTCI"] < median_level]
    urgent = acceptable["worst_priority"].isin(["d1", "d7"])
    print(f"rows generated: {len(df):,}")
    print(f"sections x runs: {len(res)}")
    print(df[["top_left", "twist_3m", "gauge"]].describe().round(2).to_string())
    print(f"\noTCI: mean {res.oTCI.mean():.1f}, sd {res.oTCI.std():.1f}, "
          f"min {res.oTCI.min():.1f}, max {res.oTCI.max():.1f}, median {median_level:.1f}")
    print(res.worst_priority.value_counts(dropna=False).to_string())
    print(f"\nsections below median oTCI: {len(acceptable)}")
    print(f"of those, containing d1 or d7: {urgent.sum()} ({100*urgent.mean():.1f}%)")
    df.to_parquet("synthetic_geometry.parquet", index=False)
    res.to_csv("synthetic_section_summary.csv", index=False)

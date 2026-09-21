"""The generator must plant defects the pipeline can later be asked to find."""
from track_record.synthetic.generate import generate, analyse


def test_generator_produces_sections_and_defects():
    df, plan = generate()
    assert len(df) > 100_000
    assert {"section_id", "run_id", "chainage_km", "top_left", "twist_3m", "gauge"} <= set(df.columns)
    res = analyse(df)
    assert res.oTCI.notna().all()
    assert res.worst_priority.notna().any(), "no defects were planted"

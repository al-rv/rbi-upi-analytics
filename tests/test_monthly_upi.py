from pathlib import Path

import pandas as pd


def test_monthly_upi_data():
    file_path = Path("data/processed/upi_monthly.csv")
    data = pd.read_csv(file_path)

    expected_files = list(Path("data/raw").glob("rbi_psi_*.xlsx"))
    assert len(data) == len(expected_files)
    assert data["report_month"].is_unique
    assert data["volume_lakh"].gt(0).all()
    assert data["value_crore"].gt(0).all()
    assert data["source_file"].notna().all()
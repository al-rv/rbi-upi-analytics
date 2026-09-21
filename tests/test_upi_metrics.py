from pathlib import Path

import pandas as pd


def test_upi_metrics():
    file_path = Path("data/processed/upi_metrics.csv")
    data = pd.read_csv(file_path)

    required_columns = {
        "reporting_period",
        "period_type",
        "volume_lakh",
        "value_crore",
        "source_file",
    }

    assert required_columns.issubset(data.columns)
    assert len(data) == 4
    assert data["volume_lakh"].notna().all()
    assert data["value_crore"].notna().all()
    assert (data["period_type"] == "fiscal_year").sum() == 1
    assert (data["period_type"] == "month").sum() == 3
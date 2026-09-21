from pathlib import Path

import pandas as pd


file_path = Path("data/processed/upi_monthly.csv")
data = pd.read_csv(file_path)

required_columns = {
    "report_month",
    "volume_lakh",
    "value_crore",
    "source_file",
}

if not required_columns.issubset(data.columns):
    raise ValueError("Required columns are missing.")

if len(data) != 36:
    raise ValueError(f"Expected 36 records, found {len(data)}.")

if not data["report_month"].is_unique:
    raise ValueError("Duplicate reporting months found.")

if data[["volume_lakh", "value_crore"]].isna().any().any():
    raise ValueError("Missing numeric values found.")

if (data[["volume_lakh", "value_crore"]] <= 0).any().any():
    raise ValueError("Non-positive values found.")

print("Data-quality checks passed.")
print(f"Validated records: {len(data)}")
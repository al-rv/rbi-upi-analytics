from pathlib import Path
import re

import pandas as pd


raw_folder = Path("data/raw")
output_file = Path("data/processed/upi_monthly.csv")

records = []

source_files = sorted(
    list(raw_folder.glob("rbi_psi_*.xlsx"))
    + list(raw_folder.glob("rbi_psi_*.XLSX"))
)

for source_file in source_files:
    match = re.search(r"(\d{4})_(\d{2})", source_file.stem)

    if not match:
        print(f"Skipped: {source_file.name}")
        continue

    year, month = match.groups()
    report_month = f"{year}-{month}-01"

    data = pd.read_excel(source_file, sheet_name=0, header=None)

    upi_row = data[
        data.iloc[:, 1]
        .astype(str)
        .str.contains("UPI", case=False, na=False)
        & ~data.iloc[:, 1].astype(str).str.contains("QR", case=False, na=False)
    ].iloc[0]

    records.append(
        {
            "report_month": report_month,
            "volume_lakh": round(float(upi_row.iloc[5]), 2),
            "value_crore": round(float(upi_row.iloc[9]), 2),
            "source_file": source_file.name,
        }
    )

result = pd.DataFrame(records).sort_values("report_month")

output_file.parent.mkdir(parents=True, exist_ok=True)
result.to_csv(output_file, index=False)

print(result)
print(f"\nSaved to: {output_file}")
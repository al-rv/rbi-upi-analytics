from pathlib import Path

import pandas as pd


source_file = Path("data/raw/rbi_psi_2026_07.xlsx")
output_file = Path("data/processed/upi_metrics.csv")

data = pd.read_excel(source_file, sheet_name=0, header=None)

upi_row = data[
    data.iloc[:, 1]
    .astype(str)
    .str.contains("UPI", case=False, na=False)
    & ~data.iloc[:, 1].astype(str).str.contains("QR", case=False, na=False)
].iloc[0]

periods = [
    "FY 2025-26",
    "July 2025",
    "June 2026",
    "July 2026",
]

result = pd.DataFrame(
    {
        "reporting_period": periods,
        "period_type": ["fiscal_year", "month", "month", "month"],
        "volume_lakh": upi_row.iloc[2:6].astype(float).values,
        "value_crore": upi_row.iloc[6:10].astype(float).values,
        "source_file": source_file.name,
    }
)

output_file.parent.mkdir(parents=True, exist_ok=True)
result.to_csv(output_file, index=False)

print(result)
print(f"\nSaved to: {output_file}")
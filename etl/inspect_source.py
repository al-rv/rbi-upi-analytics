from pathlib import Path
import pandas as pd

file_path = Path("data/raw/rbi_psi_2026_07.xlsx")

excel_file = pd.ExcelFile(file_path)

print("Sheets:", excel_file.sheet_names)

for sheet in excel_file.sheet_names:
    data = pd.read_excel(file_path, sheet_name=sheet, header=None)

    print(f"\nSheet: {sheet}")
    print("Rows:", data.shape[0])
    print("Columns:", data.shape[1])
    print(data.head(10).to_string(index=False, header=False))
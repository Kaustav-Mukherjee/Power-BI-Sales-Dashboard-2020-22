import pandas as pd
import os

file_path = "c:/Users/KAUSTAV/Downloads/POWER BI PROJECTS/PROJECT 1/Complete_Techno_Sales_Data-2.xlsx"

if os.path.exists(file_path):
    # Read sheet names
    xl = pd.ExcelFile(file_path)
    print(f"Sheets: {xl.sheet_names}")
    
    # Read first sheet sample
    df = pd.read_excel(file_path, sheet_name=xl.sheet_names[0])
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nData Sample:")
    print(df.head())
    print("\nData Shape:")
    print(df.shape)
    print("\nDate Range (if any):")
    # Try to find date columns
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        try:
            print(f"{col}: {df[col].min()} to {df[col].max()}")
        except:
            pass
else:
    print("File not found.")

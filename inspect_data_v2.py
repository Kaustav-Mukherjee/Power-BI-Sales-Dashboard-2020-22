import pandas as pd
import os

file_path = "c:/Users/KAUSTAV/Downloads/POWER BI PROJECTS/PROJECT 1/Complete_Techno_Sales_Data-2.xlsx"

if os.path.exists(file_path):
    xl = pd.ExcelFile(file_path)
    df = pd.read_excel(file_path, sheet_name='Sales_Data')
    
    print("--- FULL COLUMN LIST ---")
    print(df.columns.tolist())
    
    print("\n--- SUMMARY STATISTICS ---")
    # Identify numeric columns for sales, profit, quantity
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    print(f"Numeric Columns: {numeric_cols}")
    
    # Identify categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    print(f"Categorical Columns: {categorical_cols}")
    
    # Basic metrics
    if 'Sales' in df.columns:
        print(f"Total Sales: {df['Sales'].sum():,.2f}")
    if 'Profit' in df.columns:
        print(f"Total Profit: {df['Profit'].sum():,.2f}")
    if 'Order ID' in df.columns:
        print(f"Total Orders: {df['Order ID'].nunique()}")
    
    # Top Categories
    for col in categorical_cols:
        if 'category' in col.lower() or 'segment' in col.lower() or 'region' in col.lower():
            print(f"\nTop 5 in {col}:")
            print(df.groupby(col)['Sales'].sum().sort_values(ascending=False).head(5))

    # Time period
    date_col = next((col for col in df.columns if 'date' in col.lower()), None)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])
        print(f"\nTime Period: {df[date_col].min()} to {df[date_col].max()}")

else:
    print("File not found.")

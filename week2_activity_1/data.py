import glob
import pandas as pd

# Get all CSV files in folder
files = glob.glob("files/data/*.csv")

# Read and combine all files
df_list = [pd.read_csv(file) for file in files]
final_df = pd.concat(df_list, ignore_index=True)

# Display first 5 rows
print("First 5 rows:")
print(final_df.head())

# Column names and data types
print("\nColumn names and data types:")
print(final_df.dtypes)

# Total rows and columns
rows, columns = final_df.shape
print(f"\nTotal rows: {rows}")
print(f"Total columns: {columns}")

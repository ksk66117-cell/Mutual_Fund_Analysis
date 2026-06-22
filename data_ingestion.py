import os
import pandas as pd

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

if len(csv_files) == 0:
    print("No CSV files found inside data/raw folder.")

for file in csv_files:
    print("\n" + "="*60)
    print("File:", file)

    file_path = os.path.join(folder_path, file)

    try:
        df = pd.read_csv(file_path)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error reading", file)
        print(e)
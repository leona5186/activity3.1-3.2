import pandas as pd
import os

# data loading
df = pd.read_csv('data/rawdataset.csv')

# delete duplicate
df_cleaned = df.drop_duplicates()

# save processed data
os.makedirs('data', exist_ok=True)
df_cleaned.to_csv('data/processed_dataset.csv', index=False)

print("Processed dataset saved successfully.")

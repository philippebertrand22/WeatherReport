#%%
import csv
import pandas as pd

df = pd.read_csv('raw.csv', encoding='cp1252')

df['datetime'] = pd.to_datetime(df['datetime'])
df['temp_next_day'] = df['temp'].shift(-24)
df = df.dropna(subset=['temp_next_day'])

#remove rows with missing values
df.dropna()

df.head()

with open('cleaned.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header
    csv_writer.writerow(df.columns)
    
    # Write the data rows
    for index, row in df.iterrows():
        csv_writer.writerow(row)
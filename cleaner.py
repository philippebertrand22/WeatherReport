#%%
import pandas as pd
import csv
from datetime import datetime, timedelta

# Load raw data
live_data = pd.read_csv('raw.csv', encoding='cp1252')

yesterday = datetime.today() - timedelta(days=2)
print(yesterday)

# Drop unwanted columns
live_data = live_data.drop(columns=['name', 'icon', 'stations'])

live_data['datetime'] = pd.to_datetime(live_data['datetime'])
#filter for data after a specific date 
live_data = live_data[live_data['datetime'] > f'{yesterday}']

live_data.to_csv('test.csv', index=False, encoding='cp1252')



#cleaned data for taining the model        
df = pd.read_csv('raw.csv', encoding='cp1252')        

df = df.drop(columns=['name', 'icon', 'stations'])

df['datetime'] = pd.to_datetime(df['datetime'])
df['temp_next_day'] = df['temp'].shift(-24)
df = df.dropna(subset=['temp_next_day'])
df.dropna()

df.head()

with open('cleaned.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header
    csv_writer.writerow(df.columns)
    
    # Write the data rows
    for index, row in df.iterrows():
        csv_writer.writerow(row)

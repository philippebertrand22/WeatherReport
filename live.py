#%%
import urllib.request
import sys

import csv
import codecs

from datetime import datetime, timedelta

import pandas as pd

today = datetime.today()
today = today.strftime("%Y-%m-%d")
yesterday = datetime.today() - timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")

today_date = datetime.today().date()

try: 
  ResultBytes = urllib.request.urlopen(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Montreal/{today}?unitGroup=metric&include=hours&key=KXQ7UNVYVT72UREE3L7WHCX8K&contentType=csv")
  
  # Parse the results as CSV
  csv_text = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
  #header = next(csv_text, None)  # Read the header row
  
  with open('live.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in csv_text:
      csv_writer.writerow(row)
        
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()

#%%  
live_data = pd.read_csv('live.csv', encoding='cp1252')

live_data = live_data[live_data['stations'].notna()]

live_data = live_data.drop(columns=['name', 'icon', 'stations'])

live_data.to_csv('live.csv', index=False, encoding='cp1252')
# %%

#%%
import urllib.request
import sys

import csv
import codecs

from datetime import datetime, timedelta

yesterday = datetime.today() - timedelta(days=1)
#print(yesterday)
few_days_ago = yesterday - timedelta(days=1)
#print(few_days_ago)
yesterday = yesterday.strftime("%Y-%m-%d")
few_days_ago = few_days_ago.strftime("%Y-%m-%d")

        
try: 
  ResultBytes = urllib.request.urlopen(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Montreal/{few_days_ago}/{yesterday}?unitGroup=metric&include=hours&key=KXQ7UNVYVT72UREE3L7WHCX8K&contentType=csv")
  
  # Parse the results as CSV
  csv_text = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
  header = next(csv_text, None)  # Read the header row
  
  with open('raw.csv', 'a', newline='') as csvfile:
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
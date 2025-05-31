#%%
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('cleaned.csv', encoding='cp1252')

features = ['temp', 'humidity', 'windspeed', 'sealevelpressure', 'cloudcover', 'uvindex']
target = 'temp_next_day'

correlation_matrix = df[features].corrwith(df[target])
print(correlation_matrix)

#EDA
plt.scatter(df['temp'], df['temp_next_day'])
plt.xlabel('temp')
plt.ylabel('Temperature_next_day')
plt.show()

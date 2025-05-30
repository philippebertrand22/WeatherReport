#%%
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('cleaned.csv', encoding='cp1252')

features = ['temp', 'humidity', 'windspeed', 'sealevelpressure', 'cloudcover', 'uvindex']
target = 'temp_next_day'

lm = LinearRegression()
lm.fit(df[features], df[target])

print(f'Intercept: {lm.intercept_:.3f}')
print(f'Coefficients:')
for feature, coef in zip(features, lm.coef_):
    print(f'{feature}: {coef:.3f}')
    
print(f'R-squared: {lm.score(df[features], df[target]):.3f}')
print(f'Mean Absolute Error: {df[target].sub(lm.predict(df[features])).abs().mean():.3f}')

"""
plt.scatter(df['humidity'], df['temp'])
plt.scatter(df['precip'], df['temp'])
plt.xlabel('Humidity, Precipitation')
plt.ylabel('Temperature')
plt.show()
"""
#%%
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

training_data = pd.read_csv('cleaned.csv', encoding='cp1252')

features = ['temp', 'humidity', 'windspeed', 'sealevelpressure', 'cloudcover', 'uvindex']
target = 'temp_next_day'

lm = LinearRegression()
lm.fit(training_data[features], training_data[target])

print(f'Intercept: {lm.intercept_:.3f}')
print(f'Coefficients:')
for feature, coef in zip(features, lm.coef_):
    print(f'{feature}: {coef:.3f}')
    
print(f'R-squared: {lm.score(training_data[features], training_data[target]):.3f}')
print(f'Mean Absolute Error: {training_data[target].sub(lm.predict(training_data[features])).abs().mean():.3f}')

live_data = pd.read_csv('live.csv', encoding='cp1252')

predictions = lm.predict(live_data[features])

live_data['predicted_temp_next_day'] = predictions

plt.scatter(live_data['temp'], live_data['predicted_temp_next_day'])
plt.xlabel('Current Temperature')
plt.ylabel('Predicted Temperature Next Day')
#plt.show()
print(live_data[['predicted_temp_next_day']])

# %%

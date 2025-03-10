import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Load data
df = pd.read_csv('mydata.csv', names=['Date', 'KPI1', 'KPI2'] if 'Date' not in pd.read_csv('mydata.csv').columns else None)
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'KPI1']].rename(columns={'Date': 'ds', 'KPI1': 'y'})  # Prophet requires 'ds' (date) and 'y' (value)

# Initialize and fit Prophet model
model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
model.fit(df)

# Create future dates (30 days)
future = model.make_future_dataframe(periods=30, freq='D')

# Predict
forecast = model.predict(future)

# Extract future predictions
future_preds = forecast[['ds', 'yhat']].tail(30)

# Calculate RMSE on historical data
historical_preds = forecast[forecast['ds'].isin(df['ds'])]['yhat']
rmse = ((historical_preds - df['y']) ** 2).mean() ** 0.5
print(f"RMSE on historical data: {rmse:.4f}")

# Plot
plt.figure(figsize=(15, 6))
plt.plot(df['ds'], df['y'], label='Historical KPI1')
plt.plot(forecast['ds'], forecast['yhat'], label='Predicted KPI1', color='red')
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='red', alpha=0.2, label='Confidence Interval')
plt.title('KPI1 Prediction using Prophet')
plt.xlabel('Date')
plt.ylabel('KPI1 Value')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Save predictions
future_preds.rename(columns={'ds': 'Date', 'yhat': 'Predicted_KPI1'}).to_csv('future_predictions_prophet.csv', index=False)
print("\nFuture Predictions:\n", future_preds)
print("Predictions saved to 'future_predictions_prophet.csv'")

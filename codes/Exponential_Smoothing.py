import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load data
df = pd.read_csv('mydata.csv', names=['Date', 'KPI1', 'KPI2'] if 'Date' not in pd.read_csv('mydata.csv').columns else None)
df['Date'] = pd.to_datetime(df['Date'])
ts = df.set_index('Date')['KPI1']

# Fit Exponential Smoothing model (Holt-Winters with trend and seasonality)
model = ExponentialSmoothing(ts, trend='add', seasonal='add', seasonal_periods=7)
fitted_model = model.fit()

# Forecast 30 days ahead
future_days = 30
forecast = fitted_model.forecast(future_days)

# Future dates
future_dates = pd.date_range(start=ts.index[-1], periods=future_days + 1, freq='D')[1:]

# Calculate RMSE on historical data
historical_preds = fitted_model.fittedvalues
rmse = ((historical_preds - ts) ** 2).mean() ** 0.5
print(f"RMSE on historical data: {rmse:.4f}")

# Plot
plt.figure(figsize=(15, 6))
plt.plot(ts.index, ts, label='Historical KPI1')
plt.plot(future_dates, forecast, label='Predicted KPI1', color='red')
plt.title('KPI1 Prediction using Exponential Smoothing')
plt.xlabel('Date')
plt.ylabel('KPI1 Value')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Save predictions
future_df = pd.DataFrame({'Date': future_dates, 'Predicted_KPI1': forecast})
print("\nFuture Predictions:\n", future_df)
future_df.to_csv('future_predictions_es.csv', index=False)
print("Predictions saved to 'future_predictions_es.csv'")

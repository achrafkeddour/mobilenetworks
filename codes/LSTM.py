import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

# Load and preprocess data
df = pd.read_csv('mydata.csv', names=['Date', 'KPI1', 'KPI2'] if 'Date' not in pd.read_csv('mydata.csv').columns else None)
df['Date'] = pd.to_datetime(df['Date'])
data = df[['KPI1']].values

# Normalize data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# Create sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

seq_length, future_days = 10, 30
X, y = create_sequences(scaled_data, seq_length)

# Split data
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Build and train LSTM model
model = Sequential([LSTM(50, return_sequences=True, input_shape=(seq_length, 1)), LSTM(50), Dense(25), Dense(1)])
model.compile(optimizer=Adam(0.001), loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=1)

# Predict future values
def predict_future(model, last_seq, n_future, scaler):
    preds = []
    seq = last_seq.copy()
    for _ in range(n_future):
        pred = model.predict(seq.reshape(1, seq_length, 1), verbose=0)[0, 0]
        preds.append(pred)
        seq = np.roll(seq, -1)
        seq[-1] = pred
    return scaler.inverse_transform(np.array(preds).reshape(-1, 1))

last_sequence = scaled_data[-seq_length:]
future_preds = predict_future(model, last_sequence, future_days, scaler)
future_dates = pd.date_range(start=df['Date'].iloc[-1], periods=future_days + 1, freq='D')[1:]

# Evaluate model
test_preds = scaler.inverse_transform(model.predict(X_test))
rmse = np.sqrt(np.mean((test_preds - scaler.inverse_transform(y_test)) ** 2))
print(f"Test RMSE: {rmse:.4f}")

# Plot
plt.figure(figsize=(15, 6))
plt.plot(df['Date'], df['KPI1'], label='Historical KPI1')
plt.plot(future_dates, future_preds, label='Predicted KPI1', color='red')
plt.title('KPI1 Prediction using LSTM')
plt.xlabel('Date')
plt.ylabel('KPI1 Value')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Save predictions
future_df = pd.DataFrame({'Date': future_dates, 'Predicted_KPI1': future_preds.flatten()})
print("\nFuture Predictions:\n", future_df)
future_df.to_csv('future_predictions.csv', index=False)
print("Predictions saved to 'future_predictions.csv'")

import numpy as np
import pandas as pd
import random

# Number of data points to generate
num_data_points = 100

# Simulate sensor data for temperature, pressure, and vibration
temperature = [random.uniform(20, 80) for _ in range(num_data_points)]  # Temperature in Celsius
pressure = [random.uniform(100, 200) for _ in range(num_data_points)]  # Pressure in PSI
vibration = [random.uniform(0, 10) for _ in range(num_data_points)]  # Vibration in mm/s

# Introduce some anomalies (optional)
for i in range(5):  # Add 5 anomalies
    index = random.randint(0, num_data_points - 1)
    temperature[index] = random.uniform(90, 120)  # High temperature anomaly
    pressure[index] = random.uniform(250, 300)  # High pressure anomaly
    vibration[index] = random.uniform(15, 20)  # High vibration anomaly

# Create a Pandas DataFrame
data = pd.DataFrame({
    'temperature': temperature,
    'pressure': pressure,
    'vibration': vibration
})

# Add a timestamp column
data['timestamp'] = pd.date_range(start='2024-01-01', periods=num_data_points, freq='H')

# Set timestamp as index
data = data.set_index('timestamp')

# Save the data to a CSV file
data.to_csv('simulated_sensor_data.csv')

print("Simulated sensor data generated and saved to simulated_sensor_data.csv")
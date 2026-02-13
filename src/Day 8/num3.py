import numpy as np

sensor_data = np.arange(24)
print("Original 1D sensor data:")
print(sensor_data)
print("Shape:", sensor_data.shape)

reshaped_data = sensor_data.reshape(4, 3, 2)
print("\nAfter reshaping to (4, 3, 2):")
print(reshaped_data)
print("Shape:", reshaped_data.shape)
transposed_data = reshaped_data.transpose(0, 2, 1)  # swap last two axes
print("\nAfter transposing to (4, 2, 3):")
print(transposed_data)
print("Shape:", transposed_data.shape)

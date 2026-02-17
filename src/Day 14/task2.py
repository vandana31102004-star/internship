# -------------------------------------------------
# FEATURE SCALING TASK
# Goal: Prevent large values (Salary) from dominating small values (Age)
# -------------------------------------------------

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# -------------------------------------------------
# Step 1: Load Dataset
# -------------------------------------------------

data = pd.read_csv("employees.csv")

print("Original Dataset:\n")
print(data)

# -------------------------------------------------
# Step 2: Standardization (Mean = 0, Std = 1)
# -------------------------------------------------

standard_scaler = StandardScaler()
data_standardized = standard_scaler.fit_transform(data)

data_standardized = pd.DataFrame(data_standardized, columns=data.columns)

print("\nStandardized Dataset:\n")
print(data_standardized)

# -------------------------------------------------
# Step 3: Normalization (Range 0 to 1)
# -------------------------------------------------

minmax_scaler = MinMaxScaler()
data_normalized = minmax_scaler.fit_transform(data)

data_normalized = pd.DataFrame(data_normalized, columns=data.columns)

print("\nNormalized Dataset:\n")
print(data_normalized)

# -------------------------------------------------
# Step 4: Plot Histogram (Salary Comparison)
# -------------------------------------------------

# Before Scaling
plt.figure()
plt.hist(data['Salary'], bins=5)
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# After Standardization
plt.figure()
plt.hist(data_standardized['Salary'], bins=5)
plt.title("Salary After Standardization")
plt.xlabel("Scaled Salary")
plt.ylabel("Frequency")
plt.show()

# After Normalization
plt.figure()
plt.hist(data_normalized['Salary'], bins=5)
plt.title("Salary After Normalization")
plt.xlabel("Scaled Salary (0-1)")
plt.ylabel("Frequency")
plt.show()

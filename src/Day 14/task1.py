# -----------------------------------------
# Import Libraries
# -----------------------------------------
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# -----------------------------------------
# Read Dataset (from Notepad CSV file)
# -----------------------------------------
data = pd.read_csv("cars.csv")

# -----------------------------------------
# IMPORTANT: Clean Column Names
# (Fixes KeyError problem)
# -----------------------------------------
data.columns = data.columns.str.strip()

print("Original Dataset:\n")
print(data)
# -----------------------------------------
# 1️⃣ Label Encoding for Transmission
# -----------------------------------------
le = LabelEncoder()
data['Transmission'] = le.fit_transform(data['Transmission'])

print("\nAfter Label Encoding (Transmission):\n")
print(data)

# -----------------------------------------
# 2️⃣ One-Hot Encoding for Color
# drop_first=True avoids Dummy Variable Trap
# -----------------------------------------
data = pd.get_dummies(data, columns=['Color'], drop_first=True)

print("\nAfter One-Hot Encoding (Color):\n")
print(data)

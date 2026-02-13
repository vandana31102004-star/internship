# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Create sample dataset (example)
data = {r"C:\DS_AI internshisp\src\Day 10\Product [Laptop, Phone, Tablet, Mon.txt"
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price": ["$500", "$300", "$200", "$150"],
    "Date": ["2024-01-10", "2024-02-15", "2024-03-20", "2024-04-25"]
}

df = pd.DataFrame(data)

# STEP 3 — Check initial data types
print("Data types BEFORE conversion:")
print(df.dtypes)

# STEP 4 — Remove dollar symbol and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# STEP 5 — Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# STEP 6 — Check data types after conversion
print("\nData types AFTER conversion:")
print(df.dtypes)

# STEP 7 — Show final dataset
print("\nFinal DataFrame:")
print(df)

# STEP 8 — Example mathematical operation (to prove it works)
print("\nAverage Price:", df["Price"].mean())


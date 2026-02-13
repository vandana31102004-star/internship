import pandas as pd

# Create example dataset
data = {
    "Product": ["A", "B", "C", "D"],
    "Price": ["$100", "$250", "$300", "$150"],
    "Date": ["2024-01-05", "2024-02-10", "2024-03-15", "2024-04-20"]
}

df = pd.DataFrame(data)

# STEP 1 — Check initial data types
print("Data types BEFORE conversion:")
print(df.dtypes)

# STEP 2 — Remove dollar sign and convert to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# STEP 3 — Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check data types after conversion
print("\nData types AFTER conversion:")
print(df.dtypes)

# Show final dataset
print("\nFinal DataFrame:")
print(df)

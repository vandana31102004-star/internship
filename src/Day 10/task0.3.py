# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Create dataset (same as your previous one)
data = {
    "CustomerID": [101,102,103,104,105,106,107,107,108,109],
    "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"],
    "Age": [25,None,30,22,None,28,35,35,None,26],
    "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "],
    "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01",
             "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"]
}

df = pd.DataFrame(data)

# -------------------------------------------------
# CHECK COLUMN NAMES (important to avoid KeyError)
# -------------------------------------------------
print("Column names:")
print(df.columns)

# -------------------------------------------------
# CHECK UNIQUE VALUES BEFORE CLEANING
# -------------------------------------------------
print("\nUnique City values BEFORE cleaning:")
print(df["City"].unique())

# -------------------------------------------------
# CLEAN TEXT DATA
# -------------------------------------------------

# Remove missing values first (optional safety step)
df["City"] = df["City"].fillna("Unknown")

# Remove leading/trailing spaces
df["City"] = df["City"].str.strip()

# Standardize casing
df["City"] = df["City"].str.title()

# -------------------------------------------------
# CHECK UNIQUE VALUES AFTER CLEANING
# -------------------------------------------------
print("\nUnique City values AFTER cleaning:")
print(df["City"].unique())

"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("housing.csv")
print(df.head())
print(df.columns)

plt.figure(figsize=(8,5))
sns.histplot(df["Price"],kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness=df["Price"].skew()
kurtosis=df["Price"].kurt()

print("Skewness : ",skewness)
print("Kurtosis : ",kurtosis)

plt.figure(figsize=(8,5))
sns.countplot(x="City",data=df)
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

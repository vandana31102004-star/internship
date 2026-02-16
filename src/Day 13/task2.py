import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("housing.csv")

plt.figure(figsize=(8,5))
sns.scatterplot(x="Area",y="Price",data=df)
plt.title("Scatter Plot of Area vs Price")
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="City",y="Price",data=df)
plt.title("Boxplot of Price by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("housing.csv")

numeric_df=df.select_dtypes(include=['int64','float64'])
corr_matrix=numeric_df.corr()

print("Correlation Matrix : ")
print(corr_matrix)

plt.figure(figsize=(8,5))
sns.heatmap(corr_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(y="Price",data=df)
plt.title("Boxplot of Housing Prices (Outlier Detection")
plt.ylabel("Price")
plt.show()
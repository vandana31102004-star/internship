# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reproducibility
np.random.seed(42)

# ----------------------------
# 1️⃣ Generate Datasets
# ----------------------------

# Normal Distribution (Heights)
heights = pd.Series(np.random.normal(loc=170, scale=10, size=1000))

# Right-Skewed (Income)
incomes = pd.Series(np.random.lognormal(mean=10, sigma=0.5, size=1000))

# Left-Skewed (Easy Exam Scores)
test_scores = pd.Series(100 - np.random.lognormal(mean=3, sigma=0.4, size=1000))


# ----------------------------
# 2️⃣ Function to Plot Histogram + KDE
# ----------------------------

def plot_distribution(data, title, xlabel):
    plt.figure()
    data.plot(kind='hist', bins=30, density=True)
    data.plot(kind='kde')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Density")
    plt.show()

    print("Mean  :", data.mean())
    print("Median:", data.median())
    print("Skew  :", data.skew())
    print("---------------------------------------------------")


# ----------------------------
# 3️⃣ Plot All Distributions
# ----------------------------

plot_distribution(heights,
                  "Human Heights (Normal Distribution)",
                  "Height")

plot_distribution(incomes,
                  "Household Income (Right-Skewed)",
                  "Income")

plot_distribution(test_scores,
                  "Test Scores (Left-Skewed)",
                  "Score")


# ----------------------------
# 4️⃣ Log Transform Right-Skewed Data
# ----------------------------

log_income = np.log(incomes)

plot_distribution(log_income,
                  "Log Transformed Income (Closer to Normal)",
                  "Log Income")


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# -----------------------------------------
# 1. Create a Heavily Skewed Dataset
# -----------------------------------------
np.random.seed(42)

# Skewed income distribution (exponential)
population = np.random.exponential(scale=50000, size=100000)

# -----------------------------------------
# 2. Take 1,000 samples of size 30
# -----------------------------------------
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# -----------------------------------------
# 3. Plot Original Skewed Distribution
# -----------------------------------------
plt.figure(figsize=(8,5))
sns.histplot(population, bins=50, kde=True)
plt.title("Original Skewed Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------------
# 4. Plot Distribution of Sample Means
# -----------------------------------------
plt.figure(figsize=(8,5))
sns.histplot(sample_means, bins=30, stat="density", color="skyblue")

# Overlay Normal Curve
mu = np.mean(sample_means)
sigma = np.std(sample_means)

x = np.linspace(min(sample_means), max(sample_means), 1000)
plt.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2)

plt.title("Distribution of 1,000 Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()

# -----------------------------------------
# 5. Print Summary
# -----------------------------------------
print("Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
print("Std Dev of Sample Means:", np.std(sample_means))

import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. Create Dataset Programmatically
# --------------------------------------------------
np.random.seed(42)  # for reproducibility

# Generate 100 normal SAT scores around 1050 with std of 100
normal_scores = np.random.normal(loc=1050, scale=100, size=100)

# Add extreme values (outliers)
extreme_scores = [1600, 400]  # very high and very low scores

# Combine data
all_scores = np.concatenate([normal_scores, extreme_scores])

# Create DataFrame
df = pd.DataFrame({
    "Student_ID": range(1, len(all_scores) + 1),
    "SAT_Score": all_scores
})

# --------------------------------------------------
# 2. Calculate Mean (μ)
# --------------------------------------------------
mu = df["SAT_Score"].mean()

# --------------------------------------------------
# 3. Calculate Standard Deviation (σ)
# --------------------------------------------------
sigma = df["SAT_Score"].std()

# --------------------------------------------------
# 4. Calculate Z-Score
# Formula: Z = (x - μ) / σ
# --------------------------------------------------
df["z_score"] = (df["SAT_Score"] - mu) / sigma

# --------------------------------------------------
# 5. Identify Outliers (|Z| > 3)
# --------------------------------------------------
outliers = df[np.abs(df["z_score"]) > 3]

# --------------------------------------------------
# 6. Print Results
# --------------------------------------------------
print("========== SUMMARY STATISTICS ==========")
print(f"Mean (μ): {mu:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")

print("\n========== FIRST 10 ROWS OF DATA ==========")
print(df.head(10))

print("\n========== OUTLIERS (|Z| > 3) ==========")
print(outliers)

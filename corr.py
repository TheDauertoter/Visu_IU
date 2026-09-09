import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load dataset
file = "usa_housing_kaggle.csv"
df = pd.read_csv(file)

# Remove ZipCode
df_corr = df.drop(columns=["ZipCode"])

# Calculate correlation matrix
correlation = df_corr.corr(numeric_only=True)

# Create heatmap
plt.figure(figsize=(10, 8))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

pairs = correlation.where(
    np.triu(np.ones(correlation.shape), k=1).astype(bool)
).stack()

print(pairs.sort_values(ascending=False).head(3))
print(pairs.sort_values(ascending=True).head(3))
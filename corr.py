import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load dataset
file = "usa_housing_kaggle.csv"
df = pd.read_csv(file)

# remove ZipCode
df_corr = df.drop(columns=["ZipCode"])

# corr matrix
correlation = df_corr.corr(numeric_only=True)

# create heatmap
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

# keep everything together
plt.tight_layout()

# show
plt.show()
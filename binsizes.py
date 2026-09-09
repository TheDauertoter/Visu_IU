import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter

# Load dataset
file = "usa_housing_kaggle.csv"
df = pd.read_csv(file)

# Bin sizes
bin_sizes = [10, 30, 100]

# Create 3 histograms in one frame with bin_sizes
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes = axes.flatten()

for ax, bins in zip(axes, bin_sizes):
    sns.histplot(
        data=df,
        x="Price",
        bins=bins,
        ax=ax
    )

    ax.set_title(f"Histogram with {bins} bins")
    ax.set_xlabel("Price in $")
    ax.set_ylabel("Frequency")

    ax.xaxis.set_major_formatter(
        StrMethodFormatter('{x:,.0f}')
    )
# keep everything together
plt.tight_layout()

# show
plt.show()
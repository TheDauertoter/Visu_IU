import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import MultipleLocator, StrMethodFormatter

# load dataset
file = "usa_housing_kaggle.csv"
df = pd.read_csv(file)

# histo plot
plt.figure(figsize=(12, 5))
sns.histplot(data=df, x="Price", bins=30)

plt.xlabel("Price in $")
plt.ylabel("Frequency")

# statistical lines - enrich histogram
plt.axvline(df["Price"].mean(), color="crimson", linestyle="--", label="Mean")
plt.axvline(df["Price"].median(), color="crimson", linestyle="-", label="Median")
plt.axvline(df["Price"].mean() - df["Price"].std(),
            color="orange", linestyle="-", label="Mean - Standard Deviation")
plt.axvline(df["Price"].mean() + df["Price"].std(),
            color="green", linestyle="-", label="Mean + Standard Deviation")

# make x axis show 100k steps
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(100000))
ax.xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))

# keep everything together
plt.tight_layout()

# print legend
plt.legend()

#show
plt.show()
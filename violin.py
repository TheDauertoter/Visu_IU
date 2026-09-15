import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter

# load dataset
file = "usa_housing_kaggle.csv"
df = pd.read_csv(file)

# vio plot
plt.figure(figsize=(10, 7))
sns.violinplot(
    data=df, 
    x="Price",
    inner="box",
    linewidth= 2.5
    )
plt.title("Violin Plot of Price")
plt.xlabel("Price in $")

plt.gca().xaxis.set_major_formatter(
    StrMethodFormatter('{x:,.0f}')
)
# keep everything together
plt.tight_layout()

# show
plt.show()
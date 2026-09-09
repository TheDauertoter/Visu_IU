import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter

# Load dataset
file = "usa_housing_kaggle.csv"
df = pd.read_csv(file)


plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Price")
plt.title("Box Plot of Prices")
plt.xlabel("Price in $")
plt.gca().xaxis.set_major_formatter(
    StrMethodFormatter('{x:,.0f}')
)

# plot legend
plt.legend()

# keep everything together
plt.tight_layout()

#show
plt.show()
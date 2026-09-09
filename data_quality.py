import pandas as pd

# Load dataset

file = "usa_housing_kaggle.csv"

df = pd.read_csv(file)


#check  for data quality and print
print("Data Quality and Types : \n")
print(df.info())


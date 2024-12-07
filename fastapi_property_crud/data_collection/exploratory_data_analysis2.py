import pandas as pd
import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

file="ml.csv"
df = pd.read_csv(file)

# print(df.head(5))
# print(df.describe(include='all'))
# print(df.shape)
# categorical_columns = df.select_dtypes(include=["object"]).columns
# for col in categorical_columns:
#     unique_values = (df[col].unique())
#     print(f"{col}: {len(unique_values)} unique values")

# print(f"Column names: \n {df.columns.tolist}") 
# print(df.info)  

# print('\n Vlaue counts')

# for col in df.columns:
#     print(df[col].value_counts())

# df.drop(["owner_name","vin"], axis=1,inplace=True)
# print(df.isnull().sum())

# df.ffill(inplace=True)

#Convert Data Types
"""errors parameter can contain {
    raise: (default) raises an error for invalid parsing.
    coerce: converts invalid parsing to NaN
    ignore: returns the original data without any changes
 } """
df['selling_price'] = pd.to_numeric(df['selling_price'], errors='coerce')
df["purchase_price"] = pd.to_numeric(df["purchase_price"], errors="coerce", downcast="float")
df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
df.dtypes

# plt.figure(figsize = (20, 5))
# sns.countplot(x='manufacturer', data=df.sort_values(by='manufacturer'), hue='manufacturer', palette='husl', legend=False)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.title("Companies with their sold Vehicles", fontdict={"family": "serif", "color": "blue", "size": 20})
# plt.xticks(rotation=90) # Optional: Rotate x labels for better visibility
# plt.show()

# df.groupby('manufacturer').agg({
#     'seating_capacity': ['min', 'max', 'mean', 'std', 'first', 'last'],
#     'selling_price': ['min', 'max', 'mean', 'std', 'sum'],
#     'purchase_price': ['min', 'max', 'mean', 'std', 'sum']
# })

# plt.figure(figsize = (15, 4))
# df.groupby('manufacturer')['purchase_price'].sum().plot(kind = 'pie', autopct='%1.1f%%', startangle=90, legend=False)
# plt.title("The income in different manufacturers", fontsize = 20)
# plt.show()

# plt.figure(figsize=(20, 4))
# earned_by_manufacturer = df.groupby('manufacturer')['purchase_price'].sum().sort_values(ascending = True).plot(kind='barh', color='g')
# plt.title("Money earned from vehicle by manufacturer type", fontsize=20)
# plt.xlabel("Manufacturer", fontsize=15)
# plt.ylabel("Purchase Price", fontsize=15)
# plt.xticks(rotation=45) # Rotate x-tick labels for better visibility
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.show()


# plt.figure(figsize=(20, 4))
# earned_by_manufacturer = df.groupby('manufacturer')['purchase_price'].sum().sort_values(ascending = True).plot(kind='barh', color='g')
# plt.title("Money earned from vehicle by manufacturer type", fontsize=20)
# plt.xlabel("Manufacturer", fontsize=15)
# plt.ylabel("Purchase Price", fontsize=15)
# plt.xticks(rotation=45) # Rotate x-tick labels for better visibility
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.show()

# plt.figure(figsize=(20, 3))
# # Create scatter plot for selling_price
# sns.scatterplot(x='selling_price', y='purchase_price', data=df, color='r', label='Selling Price', alpha=0.6)
# # Create scatter plot for purchase_price
# sns.scatterplot(x='purchase_price', y='selling_price', data=df, color='b', label='Purchase Price', alpha=0.6)
# plt.title("Scatter Plot between Selling Price and Purchase Price", fontsize=20)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.xlabel("Price", fontsize=15)
# plt.ylabel("Price", fontsize=15)
# plt.legend()
# plt.show()

# plt.figure(figsize=(20, 3))
# # Create the scatter plot for selling_price vs. purchase_price
# sns.scatterplot(x='selling_price', y='purchase_price', data=df, color='b', alpha=0.6)
# plt.title("Scatter Plot between Selling Price and Purchase Price", fontsize=20)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.xlabel("Selling Price", fontsize=15)
# plt.ylabel("Purchase Price", fontsize=15)
# plt.show()

# plt.figure(figsize = (20, 3))
# # numeric_columns = ['owner_age', 'selling_price', 'purchase_price', 'year', 'kilometers_driven']
# numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
# heatmap_data = df[numeric_columns].corr()
# sns.heatmap(heatmap_data, cmap = 'BuPu', annot = True)
# plt.show()

print('Correlation between selling_price and kilometers_driven:', df['selling_price'].corr(df['kilometers_driven']))



print('Correlation between selling_price and kilometers_driven:', df['selling_price'].corr(df['kilometers_driven']))

# Return all outliers (greater than 1500 or less than 0)
df[df['selling_price'] > 1500]

# Remove outliers from the original DataFrame
df = df[df['selling_price'] < 1500]
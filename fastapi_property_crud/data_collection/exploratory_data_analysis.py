import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

try:
    properties_api=requests.get('http://127.0.0.1:8000/properties')
    properties_api.raise_for_status()
    properties_api_data = properties_api.json()

    tenants_api=requests.get('http://127.0.0.1:8000/tenants')
    tenants_api.raise_for_status()
    tenants_api_data = properties_api.json()

    # print(properties_api_data)  # Check if it's a list or dict
    # print(tenants_api_data)  

    pdf = pd.DataFrame(properties_api_data)
    tdf = pd.DataFrame(tenants_api_data)

    inner_merged_df = pd.merge(pdf,tdf, on='id', how ="inner")
except requests.exceptions.RequestException as e:
    print(f"Error fetchong data from API: {e}")



# Describe the dataset
print("Summary Statistics:")
print(inner_merged_df.describe(include='all'))  

print("The shape:")
print(inner_merged_df.shape)

print("\nColumn Info:")
print(inner_merged_df.info()) 

print("\nFirst Few Rows:")
print(inner_merged_df.head(10)) 

print("\nLast Few Rows:")
print(inner_merged_df.tail(10)) 


# Convert columns with unhashable types (e.g., lists) to strings
for column in inner_merged_df.columns:
    if inner_merged_df[column].apply(lambda x: isinstance(x, list)).any():
        inner_merged_df[column] = inner_merged_df[column].apply(lambda x: str(x) if isinstance(x, list) else x)

# Drop duplicates after fixing unhashable types
inner_merged_df.drop_duplicates(inplace=True)



print("Null Values in Each Column:")
print(inner_merged_df.isnull().sum())

inner_merged_df.fillna('name', inplace=True)

print("\nNull Values After Replacement:")
print(inner_merged_df.isnull().sum())



# Convert categorical data
label_encoder = LabelEncoder()
inner_merged_df['price_y'] = label_encoder.fit_transform(inner_merged_df['price_y'])


scaler = StandardScaler()
inner_merged_df['scaled_column'] = scaler.fit_transform(inner_merged_df[['price_y']])


inner_merged_df['double_price'] = inner_merged_df['price_y'] * 2


X = inner_merged_df.drop('price_y', axis=1)
y = inner_merged_df['tenants_y']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data
inner_merged_df.to_csv('processed_data.csv', index=False)


#features

inner_merged_df['log_price'] = np.log1p(inner_merged_df['price_y'])


bins = [0, 1000, 5000, 10000, float('inf')]
labels = ['Low', 'Medium', 'High', 'Very High']
inner_merged_df['price_category'] = pd.cut(inner_merged_df['price_y'], bins=bins, labels=labels)

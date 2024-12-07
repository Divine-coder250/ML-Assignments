import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv('data.csv')

# Handle missing data
data.fillna(data.mean(), inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Convert categorical data
label_encoder = LabelEncoder()
data['category_column'] = label_encoder.fit_transform(data['category_column'])

# Feature scaling
scaler = StandardScaler()
data['scaled_column'] = scaler.fit_transform(data[['numeric_column']])

# Feature engineering
data['new_feature'] = data['column_1'] * data['column_2']

# Split into features and target
X = data.drop('target_column', axis=1)
y = data['target_column']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data
data.to_csv('processed_data.csv', index=False)

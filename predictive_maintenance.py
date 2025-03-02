import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Load the data
df = pd.read_csv('/Users/payalbhandwalkar/Desktop/Projects/predictive_maintenance.csv')

# Display the data types of each column
print("Data types before conversion:\n", df.dtypes)

# Convert 'Product ID' to string type to prevent it from being included in numerical features
df['Product ID'] = df['Product ID'].astype(str)

# Identify numerical and categorical columns
numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(exclude=['number']).columns

# Print the identified columns
print("\nNumerical columns:\n", numerical_cols)
print("\nCategorical columns:\n", categorical_cols)

# Print unique values of categorical columns
for col in categorical_cols:
    print(f"\nUnique values in {col}:\n", df[col].unique())

# 3. Preprocessing

# Handle missing values (if any) - for numerical columns only
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

# Scale/normalize the data (important for many machine learning algorithms)
# Create a StandardScaler object
scaler = StandardScaler()

# Apply scaling to the numerical features
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# 4. Split the data into training and testing sets
# Separate features (X) and target (y)
X = df.drop(['Target', 'Failure Type'], axis=1)  # Drop both 'Target' and 'Failure Type'
y = df['Target']

# Print the final columns before splitting the data to confirm changes
print("\nFinal columns in X before splitting:\n", X.columns)

# Split into training and testing sets (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # random_state for reproducibility

# 5. Train a Machine Learning Model (Random Forest Classifier)
# Create a Random Forest Classifier object
rf_model = RandomForestClassifier(random_state=42)  # You can adjust hyperparameters here

# Train the model on the training data
rf_model.fit(X_train, y_train)

# 6. Make Predictions and Evaluate the Model
# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nAccuracy Score:\n", accuracy_score(y_test, y_pred))
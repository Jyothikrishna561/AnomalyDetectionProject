import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Step 1: Load dataset
df = pd.read_csv("../data/dataset.csv")

# Step 2: Select features
X = df[['login_hour', 'transaction_amount', 'session_duration']]

# Step 3: Create model
model = IsolationForest(contamination=0.2, random_state=42)

# Step 4: Train model
model.fit(X)

# Step 5: Save model
joblib.dump(model, "../backend/model.pkl")

print("Model trained and saved successfully!")
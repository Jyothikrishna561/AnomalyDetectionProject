from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import joblib


# Step 1: Create app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Step 2: Load trained model
model = joblib.load("model.pkl")

# Step 3: Define input structure
class UserData(BaseModel):
    login_hour: int
    transaction_amount: float
    session_duration: float

# Step 4: Create API endpoint
@app.post("/predict")
def predict(data: UserData):
    
    # Step 5: Convert input to array
    input_data = np.array([[data.login_hour, data.transaction_amount, data.session_duration]])
    
    # Step 6: Predict
    prediction = model.predict(input_data)[0]
    score = model.decision_function(input_data)[0]

    # Step 7: Return result
    return {
        "anomaly": int(prediction),
        "risk_score": float(score)
    }
from fastapi import File, UploadFile
import pandas as pd

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    
    # Step 1: Read CSV file
    df = pd.read_csv(file.file)

    # Step 2: Select required columns
    X = df[['login_hour', 'transaction_amount', 'session_duration']]

    # Step 3: Predict for all rows
    predictions = model.predict(X)
    scores = model.decision_function(X)

    # Step 4: Add results to dataframe
    df['anomaly'] = predictions
    df['risk_score'] = scores

    # Step 5: Convert to list (JSON)
    result = df.to_dict(orient="records")

    return {"results": result}
@app.get("/")
def home():
    return {"message": "Backend is running"}
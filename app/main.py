from fastapi import FastAPI
from app.schema import CustomerData
from app.model import predict_churn

app = FastAPI(title="Customer Churn Prediction API")

@app.get("/")
def root():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict(data: CustomerData):
    result = predict_churn(data.dict())
    return result
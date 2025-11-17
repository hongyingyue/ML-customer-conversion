import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import xgboost as xgb

model_file = 'model_xgb.pkl'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI(title="Prediction API", version="1.0")

# Define Customer class
class Customer(BaseModel):
    # Categorical features first
    gender: Optional[str]
    location: Optional[str]
    leadsource: Optional[str]
    leadstatus: Optional[str]
    devicetype: Optional[str]
    referralsource: Optional[str]
    paymenthistory: Optional[str]

    # Numerical features
    age: Optional[float]
    timespent_minutes: Optional[float]
    pagesviewed: Optional[float]
    emailsent: Optional[float]
    formsubmissions: Optional[float]
    downloads: Optional[float]
    ctr_productpage: Optional[float]
    responsetime_hours: Optional[float]
    followupemails: Optional[float]
    socialmediaengagement: Optional[float]

@app.post("/predict")
def predict(customer: Customer):
    # Convert Pydantic model to dict
    customer_dict = customer.model_dump()
    
    # Transform dict to vector
    X = dv.transform([customer_dict])

    features = list(dv.get_feature_names_out())
    dmatrix = xgb.DMatrix(X, feature_names=features)

    # Predict
    y_pred = model.predict(dmatrix)[0]
    convert = y_pred >= 0.5

    return {
        "convert_probability": float(y_pred),
        "convert": bool(convert)
    }

# For local dev run: 
# uvicorn predict:app --reload --host 0.0.0.0 --port 9696

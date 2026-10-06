from pydantic import BaseModel, Field, ConfigDict

from pydantic import BaseModel

class CustomerData(BaseModel):
    gender: str                  # "Male" or "Female"
    SeniorCitizen: int           # 0 or 1
    Partner: str                 # "Yes" or "No"
    Dependents: str              # "Yes" or "No"
    tenure: int
    PhoneService: str            # "Yes" or "No"
    MultipleLines: str           # "Yes", "No", "No phone service"
    InternetService: str         # "DSL", "Fiber optic", "No"
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str                # "Month-to-month", "One year", "Two year"
    PaperlessBilling: str        # "Yes" or "No"
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float
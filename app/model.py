import joblib
import pandas as pd

model = joblib.load('Models/xgb_churn_model.pkl')
model_columns = model.get_booster().feature_names

def tenure_bucket(t):
    if t <= 12: return '0-12'
    elif t <= 24: return '13-24'
    elif t <= 48: return '25-48'
    else: return '49+'

def predict_churn(data: dict):
    df = pd.DataFrame([data])

    # Feature engineering — same logic as notebook
    df['tenure_group'] = df['tenure'].apply(tenure_bucket)
    df['avg_monthly_spend'] = df['TotalCharges'] / df['tenure'].replace(0, 1)

    service_cols = ['PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                     'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    df['total_services'] = df[service_cols].apply(lambda row: (row == 'Yes').sum(), axis=1)

    df['has_multiple_lines'] = (df['MultipleLines'] == 'Yes').astype(int)
    df['has_streaming'] = ((df['StreamingTV'] == 'Yes') | (df['StreamingMovies'] == 'Yes')).astype(int)
    df['is_paperless'] = (df['PaperlessBilling'] == 'Yes').astype(int)
    df['is_month_to_month'] = (df['Contract'] == 'Month-to-month').astype(int)

    # One-hot encode, matching training
    cat_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                'PaperlessBilling', 'PaymentMethod', 'tenure_group']
    df_encoded = pd.get_dummies(df, columns=cat_cols)

    # Ensure every column the model expects exists (fill missing dummy columns with 0)
    for col in model_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    # Correct column order
    df_encoded = df_encoded[model_columns]

    probability = model.predict_proba(df_encoded)[0][1]
    prediction = int(probability >= 0.5)
    return {
        "churn_probability": round(float(probability), 4),
        "prediction": prediction,
        "risk_segment": "High Risk" if probability >= 0.7 else "Medium Risk" if probability >= 0.4 else "Low Risk"
    }
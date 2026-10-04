# Customer Churn Prediction & Analytics Dashboard

End-to-end machine learning pipeline that predicts customer churn using XGBoost, 
with model insights translated into an interactive Power BI dashboard for 
customer analytics and KPI monitoring.

## Problem Statement

Customer churn directly impacts recurring revenue for subscription-based businesses. 
This project identifies customers at high risk of churning so retention teams can 
proactively intervene, using the IBM Telco Customer Churn dataset (7,043 customers, 
21 original features).

## Approach

1. **Data Cleaning** — Fixed TotalCharges (blank strings converted to numeric), 
   handled missing values, encoded the target variable.

2. **Feature Engineering** — Created tenure buckets (0-12, 13-24, 25-48, 49+ months), 
   average monthly spend ratio, total services subscribed, and contract-risk flags 
   (is_month_to_month, has_streaming, is_paperless, has_multiple_lines) to improve 
   both model performance and business interpretability.

3. **Model Comparison** — Benchmarked Logistic Regression, Random Forest, and 
   XGBoost at baseline (untuned) to validate XGBoost as the right choice for this 
   problem before

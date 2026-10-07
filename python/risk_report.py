import pandas as pd
import joblib


# ==========================================
# 1. Load Cleaned Dataset
# ==========================================

df = pd.read_csv(
    "data/DataCoSupplyChain_Cleaned.csv"
)

print("Cleaned dataset shape:", df.shape)


# ==========================================
# 2. Load Trained Model
# ==========================================

model = joblib.load(
    "data/random_forest_risk_model.pkl"
)

preprocessor = joblib.load(
    "data/ml_preprocessor.pkl"
)

print("Model and preprocessor loaded successfully.")


# ==========================================
# 3. Convert Order Date
# ==========================================

df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)


# ==========================================
# 4. Create Date Features
# ==========================================

df["Order_Year"] = (
    df["order date (DateOrders)"].dt.year
)

df["Order_Month"] = (
    df["order date (DateOrders)"].dt.month
)

df["Order_DayOfWeek"] = (
    df["order date (DateOrders)"].dt.dayofweek
)


# ==========================================
# 5. Select Prediction Features
# ==========================================

features = [
    "Type",
    "Days for shipment (scheduled)",
    "Order Item Discount",
    "Order Item Discount Rate",
    "Order Item Quantity",
    "Order Item Product Price",
    "Product Price",
    "Customer Segment",
    "Market",
    "Order Region",
    "Order Country",
    "Department Name",
    "Category Name",
    "Shipping Mode",
    "Order_Year",
    "Order_Month",
    "Order_DayOfWeek"
]


# ==========================================
# 6. Prepare Prediction Data
# ==========================================

prediction_data = df[features].copy()

prediction_data = prediction_data.dropna()

print(
    "Rows available for prediction:",
    len(prediction_data)
)


# ==========================================
# 7. Apply Preprocessor
# ==========================================

X = preprocessor.transform(
    prediction_data
)


# ==========================================
# 8. Generate Risk Predictions
# ==========================================

risk_prediction = model.predict(X)

risk_probability = model.predict_proba(X)[:, 1]


# ==========================================
# 9. Add Prediction Results
# ==========================================

prediction_data["Predicted_Risk"] = (
    risk_prediction
)

prediction_data["Risk_Probability"] = (
    risk_probability
)


# ==========================================
# 10. Create Risk Categories
# ==========================================

prediction_data["Risk_Category"] = pd.cut(
    prediction_data["Risk_Probability"],
    bins=[0, 0.40, 0.70, 1.00],
    labels=[
        "Low Risk",
        "Moderate Risk",
        "High Risk"
    ],
    include_lowest=True
)


# ==========================================
# 11. Save Risk Report
# ==========================================

prediction_data.to_csv(
    "data/SupplyChain_Risk_Report.csv",
    index=False
)


# ==========================================
# 12. Display Results
# ==========================================

print("\nSupply Chain Risk Report")
print("------------------------")

print(
    "Total Predictions:",
    len(prediction_data)
)

print("\nRisk Category Distribution:")

print(
    prediction_data["Risk_Category"]
    .value_counts()
    .sort_index()
)

print(
    "\nAverage Risk Probability:",
    round(
        prediction_data["Risk_Probability"].mean(),
        4
    )
)

print("\nRisk report saved successfully.")

print(
    "data/SupplyChain_Risk_Report.csv"
)
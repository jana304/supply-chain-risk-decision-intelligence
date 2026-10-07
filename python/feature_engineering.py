import pandas as pd


# ==========================================
# 1. Load Cleaned Dataset
# ==========================================

df = pd.read_csv(
    "data/DataCoSupplyChain_Cleaned.csv"
)

print("Cleaned dataset shape:", df.shape)


# ==========================================
# 2. Convert Order Date
# ==========================================

df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)


# ==========================================
# 3. Create Date Features
# ==========================================

df["Order_Year"] = df["order date (DateOrders)"].dt.year

df["Order_Month"] = df["order date (DateOrders)"].dt.month

df["Order_DayOfWeek"] = df["order date (DateOrders)"].dt.dayofweek


# ==========================================
# 4. Select ML Features
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
# 5. Define Target
# ==========================================

target = "Late_delivery_risk"


# ==========================================
# 6. Create ML Dataset
# ==========================================

ml_df = df[features + [target]].copy()


# ==========================================
# 7. Remove Missing Values
# ==========================================

ml_df = ml_df.dropna()


# ==========================================
# 8. Save ML Dataset
# ==========================================

ml_df.to_csv(
    "data/SupplyChain_ML_Features.csv",
    index=False
)


# ==========================================
# 9. Display Results
# ==========================================

print("\nFeature engineering completed successfully.")

print("ML dataset shape:", ml_df.shape)

print("\nTarget distribution:")

print(
    ml_df[target].value_counts()
)

print("\nML feature dataset saved to:")
print("data/SupplyChain_ML_Features.csv")
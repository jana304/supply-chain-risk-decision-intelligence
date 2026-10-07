import pandas as pd


# ==========================================
# 1. Load Raw Dataset
# ==========================================

df = pd.read_csv(
    "data/DataCoSupplyChainDataset.csv",
    encoding="latin1"
)

print("Raw dataset shape:", df.shape)


# ==========================================
# 2. Remove Unnecessary Columns
# ==========================================

columns_to_remove = [
    "Customer Email",
    "Customer Fname",
    "Customer Lname",
    "Customer Password",
    "Customer Street",
    "Product Description",
    "Product Image",
    "Order Zipcode"
]

df_clean = df.drop(
    columns=columns_to_remove
)


# ==========================================
# 3. Convert Date Columns
# ==========================================

df_clean["order date (DateOrders)"] = pd.to_datetime(
    df_clean["order date (DateOrders)"],
    errors="coerce"
)

df_clean["shipping date (DateOrders)"] = pd.to_datetime(
    df_clean["shipping date (DateOrders)"],
    errors="coerce"
)


# ==========================================
# 4. Check Duplicate Rows
# ==========================================

duplicate_count = df_clean.duplicated().sum()

print("Duplicate rows:", duplicate_count)


# ==========================================
# 5. Check Missing Values
# ==========================================

missing_values = df_clean.isnull().sum()

print("\nColumns with missing values:")
print(missing_values[missing_values > 0])


# ==========================================
# 6. Save Cleaned Dataset
# ==========================================

df_clean.to_csv(
    "data/DataCoSupplyChain_Cleaned.csv",
    index=False
)


# ==========================================
# 7. Final Summary
# ==========================================

print("\nData cleaning completed successfully.")
print("Cleaned dataset shape:", df_clean.shape)
print("Cleaned dataset saved to:")
print("data/DataCoSupplyChain_Cleaned.csv")
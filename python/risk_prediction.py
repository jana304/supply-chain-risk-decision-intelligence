import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


# ==========================================
# 1. Load ML Dataset
# ==========================================

df = pd.read_csv(
    "data/SupplyChain_ML_Features.csv"
)

print("ML dataset shape:", df.shape)


# ==========================================
# 2. Separate Features and Target
# ==========================================

target = "Late_delivery_risk"

X = df.drop(columns=[target])
y = df[target]


# ==========================================
# 3. Identify Feature Types
# ==========================================

categorical_features = X.select_dtypes(
    include=["object", "string"]
).columns.tolist()

numerical_features = X.select_dtypes(
    exclude=["object", "string"]
).columns.tolist()

print("\nCategorical features:", len(categorical_features))
print("Numerical features:", len(numerical_features))


# ==========================================
# 4. Create Preprocessor
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=True
            ),
            categorical_features
        ),
        (
            "numerical",
            "passthrough",
            numerical_features
        )
    ]
)


# ==========================================
# 5. Encode Features
# ==========================================

X_encoded = preprocessor.fit_transform(X)

print("Encoded feature shape:", X_encoded.shape)


# ==========================================
# 6. Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining rows:", X_train.shape[0])
print("Testing rows:", X_test.shape[0])


# ==========================================
# 7. Create Faster Random Forest
# ==========================================

random_forest = RandomForestClassifier(
    n_estimators=80,
    max_depth=15,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)


# ==========================================
# 8. Train Model
# ==========================================

print("\nTraining Random Forest model...")

random_forest.fit(
    X_train,
    y_train
)

print("Model training completed.")


# ==========================================
# 9. Make Predictions
# ==========================================

y_pred = random_forest.predict(
    X_test
)

y_prob = random_forest.predict_proba(
    X_test
)[:, 1]


# ==========================================
# 10. Evaluate Model
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

roc_auc = roc_auc_score(
    y_test,
    y_prob
)


# ==========================================
# 11. Display Performance
# ==========================================

print("\nRandom Forest Model Performance")
print("--------------------------------")

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc_auc:.4f}")


# ==========================================
# 12. Save Model
# ==========================================

joblib.dump(
    random_forest,
    "data/random_forest_risk_model.pkl"
)

joblib.dump(
    preprocessor,
    "data/ml_preprocessor.pkl"
)


# ==========================================
# 13. Final Confirmation
# ==========================================

print("\nModel and preprocessor saved successfully.")

print("Model:")
print("data/random_forest_risk_model.pkl")

print("\nPreprocessor:")
print("data/ml_preprocessor.pkl")
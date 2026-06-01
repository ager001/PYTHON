# ==========================================================
# LOAN DEFAULT PREDICTION USING K-NEAREST NEIGHBORS (KNN)
# ==========================================================

# ==========================================================
# STEP 1: IMPORT LIBRARIES
# ==========================================================

import numpy as np
import pandas as pd

# Generate sample dataset
from sklearn.datasets import make_classification

# Split dataset
from sklearn.model_selection import train_test_split

# Feature scaling
from sklearn.preprocessing import StandardScaler

# KNN Model
from sklearn.neighbors import KNeighborsClassifier

# Evaluation Metrics
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Hyperparameter tuning
from sklearn.model_selection import GridSearchCV


# ==========================================================
# STEP 2: CREATE A LOAN DATASET
# ==========================================================

# In a real project:
# df = pd.read_csv("loan_default.csv")

# For learning purposes, create a realistic dataset

X, y = make_classification(
    n_samples=5000,
    n_features=5,
    n_informative=4,
    n_redundant=0,
    n_clusters_per_class=2,
    weights=[0.80, 0.20],   # 80% repay, 20% default
    random_state=42
)

# ==========================================================
# STEP 3: CREATE DATAFRAME
# ==========================================================

columns = [
    "age",
    "income",
    "credit_score",
    "loan_amount",
    "years_employed"
]

df = pd.DataFrame(X, columns=columns)

df["default"] = y

print("=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)

print(df.head())


# ==========================================================
# STEP 4: CHECK TARGET DISTRIBUTION
# ==========================================================

print("\n")
print("=" * 60)
print("DEFAULT DISTRIBUTION")
print("=" * 60)

print(df["default"].value_counts())

print("\nPercentage Distribution")

print(
    df["default"].value_counts(normalize=True) * 100
)

# ==========================================================
# STEP 5: FEATURES AND TARGET
# ==========================================================

X = df.drop("default", axis=1)

y = df["default"]

# ==========================================================
# STEP 6: TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

print("\n")
print("=" * 60)
print("TRAIN TEST SPLIT")
print("=" * 60)

print("Training Shape:", X_train.shape)
print("Testing Shape :", X_test.shape)

# ==========================================================
# STEP 7: FEATURE SCALING
# ==========================================================

# KNN uses distance calculations
# Scaling is extremely important

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# ==========================================================
# STEP 8: TRAIN KNN MODEL
# ==========================================================

knn = KNeighborsClassifier(
    n_neighbors=5
)

knn.fit(
    X_train_scaled,
    y_train
)

print("\nModel Training Complete")

# ==========================================================
# STEP 9: MAKE PREDICTIONS
# ==========================================================

y_pred = knn.predict(
    X_test_scaled
)

# ==========================================================
# STEP 10: EVALUATE MODEL
# ==========================================================

print("\n")
print("=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(f"Accuracy: {accuracy:.4f}")

# ==========================================================
# STEP 11: CONFUSION MATRIX
# ==========================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix")

print(cm)

# ==========================================================
# STEP 12: CLASSIFICATION REPORT
# ==========================================================

print("\nClassification Report")

print(
    classification_report(
        y_test,
        y_pred
    )
)

# ==========================================================
# STEP 13: PREDICT A NEW CUSTOMER
# ==========================================================

print("\n")
print("=" * 60)
print("NEW CUSTOMER PREDICTION")
print("=" * 60)

# Example Applicant:
#
# Age = 28
# Income = 35000
# Credit Score = 580
# Loan Amount = 18000
# Years Employed = 2

new_customer = np.array([
    [
        28,
        35000,
        580,
        18000,
        2
    ]
])

# Scale customer using training scaler

new_customer_scaled = scaler.transform(
    new_customer
)

prediction = knn.predict(
    new_customer_scaled
)

probability = knn.predict_proba(
    new_customer_scaled
)

if prediction[0] == 1:

    print("⚠️ HIGH RISK OF DEFAULT")

else:

    print("✅ LIKELY TO REPAY")

print("\nPrediction Probabilities")

print(probability)

# Example:
#
# [[0.20 0.80]]
#
# Meaning:
#
# 20% chance repay
# 80% chance default

# ==========================================================
# STEP 14: FIND BEST K USING GRID SEARCH
# ==========================================================

print("\n")
print("=" * 60)
print("HYPERPARAMETER TUNING")
print("=" * 60)

params = {
    "n_neighbors": [3, 5, 7, 9, 11, 13, 15]
}

grid = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid=params,
    cv=5,
    scoring="accuracy"
)

grid.fit(
    X_train_scaled,
    y_train
)

print("Best Parameters")

print(grid.best_params_)

print("\nBest Cross Validation Score")

print(grid.best_score_)

# ==========================================================
# STEP 15: TRAIN BEST MODEL
# ==========================================================

best_knn = grid.best_estimator_

best_predictions = best_knn.predict(
    X_test_scaled
)

best_accuracy = accuracy_score(
    y_test,
    best_predictions
)

print("\nAccuracy Using Best Model")

print(best_accuracy)

# ==========================================================
# STEP 16: FINAL BUSINESS SUMMARY
# ==========================================================

print("\n")
print("=" * 60)
print("BUSINESS SUMMARY")
print("=" * 60)

print(f"""
Loan Default Prediction Model Complete

Model Type:
K-Nearest Neighbors (KNN)

Test Accuracy:
{best_accuracy:.4f}

Business Use:
- Predict risky borrowers
- Reduce loan defaults
- Improve approval decisions
- Assist credit officers

Decision Example:
If Default Probability > 50%
→ Flag customer for manual review

If Default Probability < 50%
→ Continue loan approval process
""")
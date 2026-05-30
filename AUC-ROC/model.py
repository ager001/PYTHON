# ==========================================================
# CUSTOMER CHURN PREDICTION PROJECT
# Evaluation Metric: ROC-AUC
# ==========================================================

# ==========================================================
# STEP 1: IMPORT LIBRARIES
# ==========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dataset creation (for learning purposes)
from sklearn.datasets import make_classification

# Data splitting
from sklearn.model_selection import train_test_split

# Feature scaling
from sklearn.preprocessing import StandardScaler

# Machine Learning Model
from sklearn.linear_model import LogisticRegression

# Evaluation Metrics
from sklearn.metrics import (
    roc_auc_score,
    roc_curve,
    confusion_matrix,
    classification_report
)

# Cross Validation
from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score
)

# ==========================================================
# STEP 2: CREATE A CUSTOMER CHURN DATASET
# ==========================================================

# In a real company:
# df = pd.read_csv("customer_churn.csv")

# For learning, we'll generate realistic data

X, y = make_classification(
    n_samples=5000,          # 5000 customers
    n_features=10,           # 10 customer features
    n_informative=6,         # 6 useful features
    n_redundant=2,           # 2 correlated features
    n_clusters_per_class=2,
    weights=[0.75, 0.25],   # 75% stay, 25% churn
    random_state=42
)

# Convert to DataFrame for easier inspection

columns = [
    "tenure",
    "monthly_charges",
    "total_charges",
    "support_calls",
    "internet_usage",
    "contract_length",
    "feature_7",
    "feature_8",
    "feature_9",
    "feature_10"
]

df = pd.DataFrame(X, columns=columns)

# Target column
df["churn"] = y

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# ==========================================================
# STEP 3: CHECK TARGET DISTRIBUTION
# ==========================================================

print("\nChurn Distribution:")

print(df["churn"].value_counts())

print("\nChurn Percentage:")

print(df["churn"].value_counts(normalize=True) * 100)

# ==========================================================
# STEP 4: SPLIT FEATURES AND TARGET
# ==========================================================

X = df.drop("churn", axis=1)

y = df["churn"]

# ==========================================================
# STEP 5: TRAIN TEST SPLIT
# ==========================================================

# Stratify keeps churn percentages similar
# in both train and test datasets

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ==========================================================
# STEP 6: FEATURE SCALING
# ==========================================================

# Logistic Regression performs better
# when features are on similar scales

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# ==========================================================
# STEP 7: TRAIN MODEL
# ==========================================================

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(
    X_train_scaled,
    y_train
)

print("\nModel Training Complete")

# ==========================================================
# STEP 8: PREDICTIONS
# ==========================================================

# Traditional predictions (0 or 1)

y_pred = model.predict(X_test_scaled)

# Probabilities needed for ROC-AUC

y_prob = model.predict_proba(X_test_scaled)[:, 1]

# Example probabilities

print("\nFirst 10 Probabilities:")

print(y_prob[:10])

# ==========================================================
# STEP 9: CONFUSION MATRIX
# ==========================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")

print(cm)

# ==========================================================
# STEP 10: CLASSIFICATION REPORT
# ==========================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)

# ==========================================================
# STEP 11: CALCULATE ROC-AUC SCORE
# ==========================================================

auc_score = roc_auc_score(
    y_test,
    y_prob
)

print("\nROC-AUC Score:")

print(round(auc_score, 4))

# ==========================================================
# BUSINESS INTERPRETATION
# ==========================================================

print(
    f"\nInterpretation:"
    f"\nThe model can rank a churner above a"
    f" non-churner {auc_score*100:.2f}% of the time."
)

# ==========================================================
# STEP 12: CREATE ROC CURVE
# ==========================================================

fpr, tpr, thresholds = roc_curve(
    y_test,
    y_prob
)

# ==========================================================
# STEP 13: PLOT ROC CURVE
# ==========================================================

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    linewidth=2,
    label=f"AUC = {auc_score:.3f}"
)

# Random guessing line

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.show()

# ==========================================================
# STEP 14: FIND BEST THRESHOLD
# ==========================================================

# Youden's J Statistic
# J = TPR - FPR

optimal_index = np.argmax(
    tpr - fpr
)

optimal_threshold = thresholds[
    optimal_index
]

print("\nOptimal Threshold:")

print(round(optimal_threshold, 4))

# ==========================================================
# STEP 15: PREDICT USING NEW THRESHOLD
# ==========================================================

custom_predictions = (
    y_prob >= optimal_threshold
).astype(int)

print("\nPredictions using optimized threshold complete.")

# ==========================================================
# STEP 16: CROSS VALIDATION USING ROC-AUC
# ==========================================================

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

cv_scores = cross_val_score(
    LogisticRegression(max_iter=1000),
    X,
    y,
    cv=cv,
    scoring="roc_auc"
)

print("\nCross Validation ROC-AUC Scores:")

print(cv_scores)

print("\nMean ROC-AUC:")

print(round(cv_scores.mean(), 4))

print("\nStandard Deviation:")

print(round(cv_scores.std(), 4))

# ==========================================================
# STEP 17: FINAL BUSINESS SUMMARY
# ==========================================================

print("\n========== BUSINESS SUMMARY ==========")

print(f"Single Test ROC-AUC : {auc_score:.4f}")

print(f"Cross Validated ROC-AUC : {cv_scores.mean():.4f}")

print(
    "\nThe model can be used to rank customers"
    "\nby churn probability."
)

print(
    "\nMarketing can target customers with"
    "\nthe highest churn scores first."
)

print(
    "\nThis allows the company to reduce"
    "\ncustomer loss and increase retention."
)
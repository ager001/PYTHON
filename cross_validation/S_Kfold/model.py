from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# STEP 1: Create dummy fraud dataset
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_classes=2,
    weights=[0.99, 0.01],
    random_state=42
)

# Check class distribution
print("Class distribution:")
print(np.bincount(y))

# STEP 2: Create StratifiedKFold object
skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# STEP 3: Create scaler
scaler = StandardScaler()

# STEP 4: Create model
model = LogisticRegression()

# STEP 5: Store accuracies
accuracies = []

# STEP 6: Stratified K-Fold loop
for train_index, test_index in skf.split(X, y):

    # STEP 7: Split data
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # STEP 8: Scale data
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # STEP 9: Train model
    model.fit(X_train, y_train)

    # STEP 10: Make predictions
    y_pred = model.predict(X_test)

    # STEP 11: Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# STEP 12: Final results
print("Fold Accuracies:", accuracies)
print("Mean Accuracy:", np.mean(accuracies))
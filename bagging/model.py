# ================================
# 1. IMPORT LIBRARIES
# ================================
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix


# ================================
# 2. CREATE FRAUD DATASET
# ================================
# Simulating banking transactions
# Fraud is rare (2%) like real systems used by banks such as Visa / Mastercard

X, y = make_classification(
    n_samples=5000,
    n_features=12,
    n_informative=6,
    n_redundant=4,
    n_clusters_per_class=2,
    weights=[0.98, 0.02],  # imbalanced dataset (fraud rare)
    random_state=42
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


# ================================
# 3. BOOTSTRAP AGGREGATION MODEL
# ================================
class FraudBaggingClassifier:
    def __init__(self, n_models=30, max_depth=5):
        self.n_models = n_models
        self.max_depth = max_depth
        self.models = []

    def fit(self, X, y):
        n_samples = X.shape[0]
        self.models = []

        for i in range(self.n_models):
            # ----------------------------
            # BOOTSTRAP SAMPLING
            # ----------------------------
            idx = np.random.choice(n_samples, n_samples, replace=True)

            X_sample = X[idx]
            y_sample = y[idx]

            # ----------------------------
            # WEAK LEARNER (Decision Tree)
            # ----------------------------
            model = DecisionTreeClassifier(
                max_depth=self.max_depth,
                random_state=None
            )

            model.fit(X_sample, y_sample)
            self.models.append(model)

        print(f"✅ Trained {self.n_models} decision trees using bootstrap samples.")

    def predict(self, X):
        # Collect predictions from all models
        all_predictions = np.array([model.predict(X) for model in self.models])

        final_predictions = []

        # Majority voting
        for i in range(X.shape[0]):
            votes = all_predictions[:, i]
            final_predictions.append(np.bincount(votes).argmax())

        return np.array(final_predictions)


# ================================
# 4. TRAIN MODEL
# ================================
model = FraudBaggingClassifier(n_models=30, max_depth=5)
model.fit(X_train, y_train)


# ================================
# 5. MAKE PREDICTIONS
# ================================
y_pred = model.predict(X_test)


# ================================
# 6. EVALUATION
# ================================
print("\n================ CONFUSION MATRIX ================")
print(confusion_matrix(y_test, y_pred))

print("\n================ CLASSIFICATION REPORT ================")
print(classification_report(y_test, y_pred))
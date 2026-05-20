import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Features
X = np.array([
    [1], [2], [3], [4],
    [5], [6], [7], [8]
])

# Labels
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Create model
model = LogisticRegression()

# Hyperparameters to test
param_grid = {
    'C': [0.1, 1, 10, 100],
    'solver': ['liblinear', 'lbfgs']
}

# Grid Search
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=4
)

# Train
grid_search.fit(X, y)

# Best settings
print("Best Parameters:")
print(grid_search.best_params_)

# Best score
print("\nBest Accuracy:")
print(grid_search.best_score_)
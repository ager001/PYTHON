import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Study hours
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Exam scores
y = np.array([30, 40, 50, 60, 70, 80])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict score for 7 study hours
prediction = model.predict([[7]])

print("Predicted Score:", prediction[0])

# Predict values for drawing regression line
y_pred = model.predict(X)

# Plot original data
plt.scatter(X, y)

# Plot regression line
plt.plot(X, y_pred)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Linear Regression Example")

plt.show()
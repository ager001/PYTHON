import numpy as np
from sklearn.linear_model import LogisticRegression

# Study hours
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)

# Results
# 0 = Fail
# 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict pass/fail for student studying 5 hours
prediction = model.predict([[5]])

# Predict probability
probability = model.predict_proba([[5]])

print("Prediction:", prediction[0])

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")

print("\nProbabilities:")
print("Fail Probability:", probability[0][0])
print("Pass Probability:", probability[0][1])
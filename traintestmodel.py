import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(r"C:\Users\agerm\OneDrive\Desktop\PYTHON\multiple regression\epl_data.csv")

# Features
X = df[['goals_scored', 'shots', 'possessions']]

# Target
y = df['points']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
score = model.score(X_test, y_test)

print("Predictions:")
print(predictions)

print("\nActual Values:")
print(y_test)

print("\nR² Score:")
print(score)
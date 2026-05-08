import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv(
    r"C:\Users\agerm\OneDrive\Desktop\PYTHON\multiple regression\epl_data.csv"
)

print("DATASET:")
print(df.head())

# Features
X = df[[
    'wins',
    'draws',
    'losses',
    'goals_scored',
    'goals_conceded',
    'goal_difference'
]]

# Target
y = df['points']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Accuracy
score = model.score(X_test, y_test)

print(f"\nR² Score: {score:.2f}")

# Future prediction
future_teams = {
    "Arsenal": [26, 8, 4, 78, 30, 48],
    "Manchester City": [25, 8, 5, 82, 34, 48],
    "Liverpool": [20, 10, 8, 70, 45, 25],
    "Manchester United": [21, 9, 8, 68, 50, 18]
}

predictions = {}

print("\nPREDICTED FINAL POINTS:\n")

for team, stats in future_teams.items():

    prediction = model.predict([stats])[0]

    predictions[team] = prediction

    print(f"{team}: {prediction:.2f} points")

# Winner
winner = max(predictions, key=predictions.get)

print("\n🏆 Predicted EPL Winner:")
print(winner)
from xml.parsers.expat import model

import pandas as pd
from sklearn import linear_model




# load the data set
df = pd.read_csv(r"C:\Users\agerm\OneDrive\Desktop\PYTHON\multiple regression\epl_data.csv")

# Features (independent variables)
X = df[['goals_scored', 'goals_conceded', 'shots', 'possessions']]

# Target (dependent variable)
y = df['points']

# Create model
regr = linear_model.LinearRegression()

#train the model

regr.fit(X, y)
print("Model trained successfully!\n")

# Predict new season (2025/2026 hypothetical stats)
teams_2026 = {
    "Manchester City": [95, 30, 680, 66],
    "Arsenal": [97, 32, 690, 62],
    "Liverpool": [88, 40, 650, 60],
    "Chelsea": [80, 50, 680, 58],
    "Manchester United": [90, 55, 550, 54]
}

predictions = {}

print("Predicted Points for 2025/2026:\n")

for team, stats in teams_2026.items():
    predicted_points = regr.predict([stats])[0]
    predictions[team] = predicted_points
    print(f"{team}: {predicted_points:.2f} points")

# Determine winner
winner = max(predictions, key=predictions.get)

print("\n🏆 Predicted EPL Winner 2025/2026:")
print(winner)
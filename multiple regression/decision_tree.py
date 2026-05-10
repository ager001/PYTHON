import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\agerm\OneDrive\Desktop\PYTHON\multiple regression\data1.csv"
)

# Convert text to numbers
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)

d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Features
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

# Create model
dtree = DecisionTreeClassifier()

# Train model
dtree.fit(X, y)

# Plot tree
plt.figure(figsize=(12, 8))

tree.plot_tree(
    dtree,
    feature_names=features,
    filled=True
)

plt.show()
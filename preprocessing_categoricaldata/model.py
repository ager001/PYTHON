import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# CREATE DATASET
data = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female'],
    
    'Education': [
        'Secondary',
        'University',
        'Primary',
        'University',
        'Secondary',
        'University'
    ],
    
    'Department': [
        'IT',
        'Finance',
        'HR',
        'IT',
        'Marketing',
        'Finance'
    ],
    
    'Experience_Years': [2, 5, 1, 7, 3, 6],
    
    'Salary': [40000, 90000, 30000, 120000, 50000, 95000]
})


# FEATURES AND TARGET
X = data.drop('Salary', axis=1)

y = data['Salary']


# COLUMN TYPES
nominal_cols = ['Gender', 'Department']

ordinal_cols = ['Education']

numeric_cols = ['Experience_Years']


# ENCODERS
onehot = OneHotEncoder(drop='first')

ordinal = OrdinalEncoder(
    categories=[['Primary', 'Secondary', 'University']]
)


# PREPROCESSOR
preprocessor = ColumnTransformer(
    transformers=[
        ('onehot', onehot, nominal_cols),
        
        ('ordinal', ordinal, ordinal_cols)
    ],
    
    remainder='passthrough'
)


# PIPELINE
model = Pipeline(steps=[
    ('preprocessing', preprocessor),
    
    ('regressor', LinearRegression())
])


# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TRAIN MODEL
model.fit(X_train, y_train)


# PREDICTIONS
predictions = model.predict(X_test)


# EVALUATION
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", mae)


# NEW EMPLOYEE
new_employee = pd.DataFrame({
    'Gender': ['Female'],
    'Education': ['University'],
    'Department': ['IT'],
    'Experience_Years': [4]
})


# PREDICT SALARY
predicted_salary = model.predict(new_employee)

print("Predicted Salary:", predicted_salary)
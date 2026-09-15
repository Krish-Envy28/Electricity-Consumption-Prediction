# train_model.py
# Phase 4 - Model Training and Saving
# Run this file once: python train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# STEP 1: Load the dataset
df = pd.read_csv("powerconsumption.csv")
print("Dataset loaded successfully!")
print("Total rows:", len(df))

# STEP 2: Select input features and target variable
input_features = ["Temperature", "Humidity", "WindSpeed",
                  "GeneralDiffuseFlows", "DiffuseFlows"]

X = df[input_features]
y = df["PowerConsumption_Zone1"]

# STEP 3: Split into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))

# STEP 4: Train the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
print("\nTraining the model... (this may take a moment)")
model.fit(X_train, y_train)
print("Training complete!")

# STEP 5: Make predictions on test data
y_pred = model.predict(X_test)

# STEP 6: Evaluate the model
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n-------------------------------------")
print("       MODEL EVALUATION RESULTS")
print("-------------------------------------")
print(f"  MAE  : {round(mae, 2)}")
print(f"  MSE  : {round(mse, 2)}")
print(f"  RMSE : {round(rmse, 2)}")
print(f"  R2   : {round(r2, 4)}")
print("-------------------------------------")

# STEP 7: Save the trained model to a file
joblib.dump(model, "electricity_model.pkl")
print("\nModel saved as electricity_model.pkl")
print("You can now run: python -m streamlit run app.py")

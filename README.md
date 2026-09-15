# Electricity Consumption Prediction

A beginner-level Data Science college project that predicts electricity
consumption in Zone 1 using five environmental features and a
Random Forest machine learning model, with a simple Streamlit web app.

---

## Project Structure

```
Electricity_Consumption_Prediction/
|
|-- powerconsumption.csv              Dataset (52,416 rows)
|-- train_model.py                    Trains and saves the model
|-- electricity_model.pkl             Saved model (generate by running train_model.py)
|-- app.py                            Streamlit web application
|-- requirements.txt                  Python libraries needed
|-- README.md                         This file
|-- graph1_actual_vs_predicted.png    Result graph
|-- graph2_model_comparison.png       Result graph
|-- graph3_feature_importance.png     Result graph
|-- s1.png                            Streamlit input screenshot
|-- s2.png                            Streamlit output screenshot
|-- Phase4_Electricity_Consumption_Prediction.pdf   Project report
```

> Note: electricity_model.pkl is NOT included in this repository (363 MB).
> Run train_model.py once to generate it locally.

---

## How to Use

### Step 1 - Clone the repository
```
git clone https://github.com/<your-username>/Electricity-Consumption-Prediction.git
cd Electricity-Consumption-Prediction
```

### Step 2 - Install required libraries
```
pip install -r requirements.txt
```

### Step 3 - Train the model and save it
This step loads the dataset, trains the Random Forest model, prints the
evaluation results, and saves the model as electricity_model.pkl.
```
python train_model.py
```

Expected output:
```
Dataset loaded successfully!
Total rows: 52416

Training samples: 41932
Testing samples : 10484

Training the model... (this may take a moment)
Training complete!

-------------------------------------
       MODEL EVALUATION RESULTS
-------------------------------------
  MAE  : 3214.31
  MSE  : 21522596.95
  RMSE : 4639.25
  R2   : 0.5738
-------------------------------------

Model saved as electricity_model.pkl
```

### Step 4 - Launch the Streamlit application
```
python -m streamlit run app.py
```

### Step 5 - Open in your browser
After running the command above, open this URL in your browser:
```
http://localhost:8501
```

---

## How to Use the Application

1. The app opens at http://localhost:8501
2. You will see five input fields:
   - Temperature (C)
   - Humidity (%)
   - Wind Speed
   - General Diffuse Flows
   - Diffuse Flows
3. Enter values for the current environmental conditions
4. Click the Predict Consumption button
5. The predicted Zone 1 power consumption will appear in watts

Example input values:
```
Temperature           : 25.0
Humidity              : 70.0
Wind Speed            : 2.5
General Diffuse Flows : 200.0
Diffuse Flows         : 80.0
```

Example output:
```
Predicted Zone 1 Power Consumption: 32320.59 watts
```

---

## Input Features

| Feature | Description |
|---------|-------------|
| Temperature | Temperature at the time of recording |
| Humidity | Relative humidity |
| WindSpeed | Wind speed |
| GeneralDiffuseFlows | General diffuse solar radiation |
| DiffuseFlows | Diffuse solar radiation |

## Target Variable
PowerConsumption_Zone1

---

## Model Results

| Metric | Value |
|--------|-------|
| Mean Absolute Error (MAE) | 3214.31 watts |
| Root Mean Squared Error (RMSE) | 4639.25 watts |
| R2 Score | 0.5738 |

### Model Comparison (Phase 3 vs Phase 4)

| Model | MAE | RMSE | R2 |
|-------|-----|------|----|
| Linear Regression | 5185.74 | 6312.08 | 0.21 |
| Gradient Boosting | 4512.90 | 5747.29 | 0.35 |
| Random Forest (Phase 3) | 3426.65 | 4795.16 | 0.54 |
| Random Forest (Phase 4 - Final) | 3214.31 | 4639.25 | 0.5738 |

Random Forest was selected as the final model because it performed best
across all three evaluation metrics in Phase 3.

---

## Requirements

```
streamlit
scikit-learn
pandas
numpy
matplotlib
joblib
```

Install all with:
```
pip install -r requirements.txt
```

---

*Data Sciences Mini Project - Phase 4 - Electricity Consumption Prediction*

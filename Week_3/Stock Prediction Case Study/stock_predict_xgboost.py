# -------------------------------
# Stock Price Movement Prediction using XGBoost
# -------------------------------

import yfinance as yf
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier

# -------------------------------
# STEP 1: DOWNLOAD STOCK DATA
# -------------------------------
print("Downloading stock data...")
data = yf.download("AAPL", start="2022-01-01", end="2024-01-01")

# -------------------------------
# STEP 2: CREATE TARGET (1 = UP, 0 = DOWN)
# -------------------------------
data['Target'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
data.dropna(inplace=True)

# -------------------------------
# STEP 3: SELECT FEATURES
# -------------------------------
features = data[['Open', 'High', 'Low', 'Close', 'Volume']]
target = data['Target']

# -------------------------------
# STEP 4: TRAIN-TEST SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, shuffle=False
)

# -------------------------------
# STEP 5: TRAIN MODEL (XGBoost)
# -------------------------------
print("\nTraining model...")
model = XGBClassifier(
    learning_rate=0.1,
    n_estimators=100,
    max_depth=3,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric='logloss'
)

model.fit(X_train, y_train)

# -------------------------------
# STEP 6: MODEL EVALUATION
# -------------------------------
preds = model.predict(X_test)

print("\n📌 Model Performance:")
print("Accuracy:", accuracy_score(y_test, preds))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, preds))
print("\nClassification Report:\n", classification_report(y_test, preds))

# -------------------------------
# STEP 7: PREDICT NEXT DAY MOVEMENT
# -------------------------------
next_day = model.predict(features.tail(1))

print("\n📍 Prediction for Next Day Stock Movement:")
print("UP 📈" if next_day[0] == 1 else "DOWN 📉")

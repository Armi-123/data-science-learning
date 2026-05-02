import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model():
    data = pd.read_csv("d:/Unlox/Week_3/house_price_project/data/house_prices.csv")

    X = data[['bedrooms', 'sqft', 'location_score']]
    y = data['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print("Model Accuracy:", score)

    return model

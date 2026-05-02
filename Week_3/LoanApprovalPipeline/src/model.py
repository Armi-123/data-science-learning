from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(df):
    X = df.drop("LoanStatus", axis=1)
    y = df["LoanStatus"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))

    # Save model
    joblib.dump(model, "loan_model.pkl")

    return acc

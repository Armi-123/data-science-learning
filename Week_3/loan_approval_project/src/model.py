import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def train_models():
    data = pd.read_csv("d:/Unlox/Week_3/loan_approval_project/data/loans.csv")

    X = data[['income', 'credit_score', 'loan_amount', 'previous_defaults']]
    y = data['approved']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)

    tree = DecisionTreeClassifier()
    tree.fit(X_train, y_train)

    forest = RandomForestClassifier()
    forest.fit(X_train, y_train)

    print("📌 Logistic Regression Accuracy:", log_model.score(X_test, y_test))
    print("📌 Decision Tree Accuracy:", tree.score(X_test, y_test))
    print("📌 Random Forest Accuracy:", forest.score(X_test, y_test))

    print("\n🔥 Random Forest Classification Report:")
    print(classification_report(y_test, forest.predict(X_test)))

    print("\n📍 Confusion Matrix:")
    print(confusion_matrix(y_test, forest.predict(X_test)))

    return forest

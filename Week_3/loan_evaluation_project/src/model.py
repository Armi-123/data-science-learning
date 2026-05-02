import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

def evaluate_model():
    data = pd.read_csv("d:/Unlox/Week_3/loan_evaluation_project/data/loans.csv")

    X = data[['income', 'credit_score', 'loan_amount', 'previous_defaults']]
    y = data['approved']

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # ---- Standard Evaluation ----
    predictions = model.predict(X_test)
    print("📌 Test Accuracy:", model.score(X_test, y_test))

    print("\n📍 Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\n🔥 Classification Report:")
    print(classification_report(y_test, predictions, zero_division=0))

    # ---- Cross Validation ----
    cv_scores = cross_val_score(model, X, y, cv=5)
    print("\n🔁 Cross Validation Scores (5-fold):", cv_scores)
    print("📌 Average CV Score:", cv_scores.mean())

    return model

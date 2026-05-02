from src.preprocess import load_and_preprocess
from src.train import train_model
from src.predict import predict_text

def run_pipeline():
    X_train, X_test, y_train, y_test, vectorizer = load_and_preprocess(r"d:/Unlox/Week_5/Sentiment_Analysis_Project/data/reviews.csv")


    acc = train_model(X_train, y_train, X_test, y_test, vectorizer)
    print("Model trained! Accuracy:", acc)

    # Test prediction
    print("Test → 'I love this product'")
    print("Prediction:", predict_text("I love this product"))

if __name__ == "__main__":
    run_pipeline()

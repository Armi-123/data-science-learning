import joblib

def predict_text(text):
    model = joblib.load("sentiment_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")

    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]

    return prediction

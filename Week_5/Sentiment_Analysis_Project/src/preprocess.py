import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Step 1: Clean NaN
    df = df.dropna()

    # Step 2: Split X & y
    X = df['text']
    y = df['sentiment']

    # Step 3: Vectorize text using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')

    X_vec = vectorizer.fit_transform(X)

    # Step 4: Train-Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, vectorizer

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    print("Data Preprocessed Successfully")

    # Fix column names if using sklearn iris dataset
    df.columns = [col.strip().lower().replace(" (cm)", "").replace(" ", "") for col in df.columns]

    # After cleaning, sklearn iris names become:
    # sepallength, sepalwidth, petallength, petalwidth, class

    X = df[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']]
    y = df['class']

    le = LabelEncoder()
    y = le.fit_transform(y)

    return X, y, le

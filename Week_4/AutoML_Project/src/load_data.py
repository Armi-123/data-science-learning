import pandas as pd
from sklearn.datasets import load_iris

def load_data(path=None):
    """
    Loads dataset from CSV if path is provided.
    Otherwise loads built-in Iris dataset.
    """
    try:
        if path:
            df = pd.read_csv(path)
            print("Data Loaded Successfully (CSV)")
            print(df.head())
            return df

        # Load sklearn iris dataset
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df["Class"] = iris.target
        print("Data Loaded Successfully (Sklearn Iris)")
        print(df.head())
        return df

    except Exception as e:
        print("Error loading data:", e)
        return None
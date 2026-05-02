import pandas as pd

def load_data(path="d:/Unlox/Week_4/CustomerSegmentation/data/customers.csv"):
    df = pd.read_csv(path)
    print("Data Loaded Successfully")
    print(df.head())
    return df

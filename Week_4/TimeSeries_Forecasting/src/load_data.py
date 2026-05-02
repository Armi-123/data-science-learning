import pandas as pd

def load_data():
    df = pd.read_csv("d:/Unlox/Week_4/TimeSeries_Forecasting/data/sales.csv")
    df['Month'] = pd.to_datetime(df['Month'])
    df.set_index('Month', inplace=True)
    return df

from prophet import Prophet
import pandas as pd

def train_prophet(df):
    df_prophet = df.reset_index()
    df_prophet.columns = ['ds','y']

    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=12, freq='MS')
    forecast = model.predict(future)

    return forecast[['ds','yhat']].tail(12)

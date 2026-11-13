import pandas as pd
from prophet import Prophet

def forecast_sales(df, periods=30):
    sales = df.groupby('Date')['PurchaseAmount'].sum().reset_index()
    sales.rename(columns={'Date':'ds', 'PurchaseAmount':'y'}, inplace=True)
    
    model = Prophet()
    model.fit(sales)
    
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    
    return forecast
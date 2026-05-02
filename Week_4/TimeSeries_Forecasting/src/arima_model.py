from statsmodels.tsa.arima.model import ARIMA

def train_arima(df):
    model = ARIMA(df['Sales'], order=(2,1,2))
    model_fit = model.fit()
    forecast = model_fit.forecast(12)
    return forecast

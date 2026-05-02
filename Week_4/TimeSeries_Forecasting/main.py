from src.load_data import load_data
from src.preprocess import preprocess
from src.arima_model import train_arima
from src.prophet_model import train_prophet

def run():
    df = load_data()
    df = preprocess(df)

    print("Training ARIMA...")
    arima_forecast = train_arima(df)
    print(arima_forecast)

    print("\nTraining Prophet...")
    prophet_forecast = train_prophet(df)
    print(prophet_forecast)

if __name__ == "__main__":
    run()

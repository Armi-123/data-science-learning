import plotly.express as px

def plot_segments(df):
    fig = px.scatter(df, x='AnnualIncome', y='PurchaseAmount', color='Segment',
                     title='Customer Segments')
    return fig

def plot_forecast(forecast):
    fig = px.line(forecast, x='ds', y='yhat', title='Sales Forecast')
    return fig
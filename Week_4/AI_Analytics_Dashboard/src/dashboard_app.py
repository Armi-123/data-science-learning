import streamlit as st
import pandas as pd
from clustering import apply_clustering
from forecasting import forecast_sales
from visualization import plot_segments, plot_forecast

# Load Data
df = pd.read_csv('d:/Unlox/Week_4/AI_Analytics_Dashboard/data/sales_data.csv', parse_dates=['Date'])

st.title("AI-Powered Analytics Dashboard")

# Clustering
st.header("Customer Segmentation")
df = apply_clustering(df)
st.dataframe(df)
seg_fig = plot_segments(df)
st.plotly_chart(seg_fig)

# Forecasting
st.header("Sales Forecasting")
forecast = forecast_sales(df)
forecast_fig = plot_forecast(forecast)
st.plotly_chart(forecast_fig)
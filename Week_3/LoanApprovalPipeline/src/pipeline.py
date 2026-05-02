import pandas as pd
from src.preprocess import preprocess_data
from src.model import train_model

def run_pipeline():
    df = pd.read_csv("d:/Unlox/Week_3/LoanApprovalPipeline/data/loan_data.csv")
    df = preprocess_data(df)
    accuracy = train_model(df)

    return accuracy
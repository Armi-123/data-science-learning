import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()

    # Handle categorical column
    le = LabelEncoder()
    df['EmploymentType'] = le.fit_transform(df['EmploymentType'])

    # Encode target
    df['LoanStatus'] = df['LoanStatus'].map({'Approved':1, 'Rejected':0})

    return df
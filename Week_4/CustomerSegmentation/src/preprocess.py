from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    features = df[['Age', 'AnnualIncome', 'SpendingScore']]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)
    print("Data Scaled Successfully")
    return scaled

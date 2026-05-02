from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    features = df[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
    labels = df['Class']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    print("Data Scaled Successfully")
    return scaled_features, labels

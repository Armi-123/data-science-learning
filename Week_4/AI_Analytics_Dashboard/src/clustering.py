import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def apply_clustering(df, n_clusters=3):
    X = df[['AnnualIncome', 'PurchaseAmount']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Segment'] = kmeans.fit_predict(X_scaled)
    
    return df
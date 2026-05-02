from sklearn.cluster import KMeans

def run_clustering(df, feature_cols, clusters=2):
    X = df[feature_cols]
    
    model = KMeans(n_clusters=clusters, random_state=42)
    df['cluster'] = model.fit_predict(X)

    return df

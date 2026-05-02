def preprocess(df):
    df = df.asfreq('MS')  # Monthly start frequency
    df = df.ffill()
    return df

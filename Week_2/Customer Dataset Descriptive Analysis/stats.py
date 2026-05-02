import pandas as pd

def analyze_stats(file_path):
    df = pd.read_csv(file_path)

    print("\n--- CUSTOMER DATA SUMMARY ---")
    
    # Central tendency
    print("\nMean Age:", df["Age"].mean())
    print("Median Income:", df["Income"].median())
    print("Mode Purchase Amount:", df["PurchaseAmount"].mode()[0])

    # Dispersion
    print("\nVariance (Purchase Amount):", df["PurchaseAmount"].var())
    print("Standard Deviation (Purchase Amount):", df["PurchaseAmount"].std())

    # Full summary
    print("\nStatistical Summary:\n", df.describe())

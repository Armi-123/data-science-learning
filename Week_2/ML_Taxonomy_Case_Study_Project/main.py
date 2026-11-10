from src.preprocessing import load_data
from src.supervised import run_supervised
from src.unsupervised import run_clustering

# Load datasets
finance = load_data(r"d:\Unlox\Week_2\ML_Taxonomy_Case_Study_Project\data\finance_data.csv")
health = load_data(r"d:\Unlox\Week_2\ML_Taxonomy_Case_Study_Project\data\health_data.csv")

# ---- Supervised (Fraud Detection) ----
acc_finance = run_supervised(finance, ["amount", "location_risk"], "is_fraud")
print("Finance Fraud Detection Accuracy:", acc_finance)

# ---- Supervised (Disease Prediction) ----
acc_health = run_supervised(health, ["age", "blood_pressure"], "disease")
print("Health Disease Prediction Accuracy:", acc_health)

# ---- Unsupervised (Customer Clustering in Finance) ----
clustered_finance = run_clustering(finance, ["amount", "location_risk"])
print("\nClustered Finance Data:")
print(clustered_finance)
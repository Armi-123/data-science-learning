from src.load_data import load_data
from src.preprocess import preprocess_data
from src.automl_model import run_automl
from src.evaluate import evaluate_model

def run():
    # Step 1: Load
    df = load_data()
    
    # Step 2: Preprocess
    X, y, le = preprocess_data(df)
    
    # Step 3: AutoML
    automl_model = run_automl(X, y)
    
    # Step 4: Evaluate
    evaluate_model(automl_model, X, y, le)

if __name__ == "__main__":
    run()
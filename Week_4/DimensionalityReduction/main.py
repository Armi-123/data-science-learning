from src.load_data import load_data
from src.preprocess import preprocess_data
from src.pca_reduction import run_pca
from src.tsne_visualization import run_tsne

def run():
    # Step 1: Load data
    df = load_data()
    
    # Step 2: Preprocess
    scaled_data, labels = preprocess_data(df)
    
    # Step 3: PCA
    pca_result = run_pca(scaled_data)
    
    # Step 4: t-SNE
    run_tsne(scaled_data, labels)

if __name__ == "__main__":
    run()

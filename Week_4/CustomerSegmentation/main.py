from src.load_data import load_data
from src.preprocess import preprocess_data
from src.kmeans_model import run_kmeans
from src.hierarchical_model import run_hierarchical
from src.visualize import visualize_clusters

def run():
    # Step 1: Load
    df = load_data()

    # Step 2: Preprocess
    data = preprocess_data(df)

    # Step 3: KMeans
    kmeans_labels = run_kmeans(data)

    # Step 4: Hierarchical
    hierarchical_labels = run_hierarchical(data)

    # Step 5: Visualize
    visualize_clusters(data, kmeans_labels)

if __name__ == "__main__":
    run()

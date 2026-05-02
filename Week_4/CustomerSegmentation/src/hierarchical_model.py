import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

def run_hierarchical(data):
    # Dendrogram
    plt.figure(figsize=(8, 4))
    sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title("Dendrogram")
    plt.show()

    # Agglomerative Clustering
    model = AgglomerativeClustering(n_clusters=4)
    labels = model.fit_predict(data)

    print("Hierarchical Cluster Labels:", labels)
    return labels

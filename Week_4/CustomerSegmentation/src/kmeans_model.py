from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def run_kmeans(data):
    # Elbow Method (Optional for beginners)
    wcss = []
    for k in range(1, 6):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    
    # Plot Elbow
    plt.plot(range(1, 6), wcss)
    plt.title("Elbow Method")
    plt.xlabel("K")
    plt.ylabel("WCSS")
    plt.show()

    # Actual KMeans
    k = 4
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)

    print("KMeans Cluster Labels:", labels)
    return labels

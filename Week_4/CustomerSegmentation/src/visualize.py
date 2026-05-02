import matplotlib.pyplot as plt

def visualize_clusters(data, labels):
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.title("Customer Clusters")
    plt.xlabel("Age")
    plt.ylabel("Annual Income")
    plt.show()

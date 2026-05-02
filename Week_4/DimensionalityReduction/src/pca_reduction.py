from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def run_pca(data, n_components=2):
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(data)
    print("PCA Completed")
    print("Explained Variance Ratio:", pca.explained_variance_ratio_)
    
    # Optional: plot PCA result
    plt.scatter(pca_result[:,0], pca_result[:,1])
    plt.title("PCA Result")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()
    
    return pca_result

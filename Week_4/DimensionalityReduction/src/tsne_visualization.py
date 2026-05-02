from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def run_tsne(data, labels):
    tsne = TSNE(n_components=2, random_state=42, perplexity=5)
    tsne_result = tsne.fit_transform(data)
    print("t-SNE Completed")
    
    # Scatter plot with colors
    classes = list(set(labels))
    colors = ['red', 'blue', 'green']
    
    plt.figure(figsize=(6,4))
    for cls, color in zip(classes, colors):
        idx = [i for i, l in enumerate(labels) if l == cls]
        plt.scatter(tsne_result[idx,0], tsne_result[idx,1], label=cls, color=color)
    
    plt.title("t-SNE Visualization")
    plt.xlabel("t-SNE 1")
    plt.ylabel("t-SNE 2")
    plt.legend()
    plt.show()

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment

def k_means_clustering(data, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    kmeans.fit(data)
    return kmeans.labels_, kmeans.cluster_centers_

def match_labels(true_labels, predicted_labels):
    D = max(true_labels.max(), predicted_labels.max()) + 1
    cost = np.zeros((D, D), dtype=int)
    for i in range(len(true_labels)):
        cost[true_labels[i], predicted_labels[i]] += 1
    row_ind, col_ind = linear_sum_assignment(cost.max() - cost)
    new_labels = np.zeros_like(predicted_labels)
    for i, j in zip(row_ind, col_ind):
        new_labels[predicted_labels == j] = i
    return new_labels

def plot_clusters(data, labels, cluster_centers):
    plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', alpha=0.5)
    for i, txt in enumerate(cluster_centers):
        plt.annotate(f'Center {i}', (txt[0], txt[1]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Cluster Zuordnung')
    plt.show()

# Testfall
def test_k_means_clustering_6():
    np.random.seed(0)
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    num_clusters = 2
    true_labels = np.array([0, 0, 0, 1, 1, 1])
    predicted_labels, cluster_centers = k_means_clustering(data, num_clusters)
    
    print("True labels: ", true_labels)
    print("Predicted labels: ", predicted_labels)
    
    # Plot the clusters
    plot_clusters(data, predicted_labels, cluster_centers)
    
    matched_labels = match_labels(true_labels, predicted_labels)
    
    print("Matched labels: ", matched_labels)
    assert np.all(matched_labels == true_labels)

# Test ausführen
test_k_means_clustering_6()

from sklearn.cluster import KMeans
import numpy as np
from scipy.optimize import linear_sum_assignment

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

class Testk_means_clustering:
    def test_k_means_clustering_2(self):
        np.random.seed(0)
        data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
        num_clusters = 3
        true_labels = np.array([0, 1, 0, 1, 0, 2])
        predicted_labels = k_means_clustering(data, num_clusters)
        matched_labels = match_labels(true_labels, predicted_labels)
        assert np.all(matched_labels == true_labels)
from sklearn.cluster import KMeans
import numpy as npclass Testk_means_clustering:
def test_k_means_clustering_2(self):
  np.random.seed(0)
  data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
  num_clusters = 3
  assert np.all(k_means_clustering(data, num_clusters) == np.array([0, 1, 0, 1, 0, 2]))

from sklearn.cluster import KMeans
import numpy as npclass Testk_means_clustering:
def test_k_means_clustering_2(self):
  np.random.seed(0)
  data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
  num_clusters = 3
  assert np.all(k_means_clustering(data, num_clusters) == np.array([0, 1, 0, 1, 0, 2]))

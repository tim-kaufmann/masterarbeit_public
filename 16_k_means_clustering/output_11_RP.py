import numpy as np
from sklearn.cluster import KMeans

def k_means_clustering(data, num_clusters):
    # Set the random seed for reproducibility
    np.random.seed(42)
    
    # Create the KMeans model
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels for each data point
    cluster_labels = kmeans.labels_
    
    return cluster_labels

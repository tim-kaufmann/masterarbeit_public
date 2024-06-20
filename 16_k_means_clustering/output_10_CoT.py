import numpy as np
from sklearn.cluster import KMeans

def k_means_clustering(data, num_clusters):
    # Setting the random seed for reproducibility
    random_seed = 42
    
    # Initialize the KMeans model with specified parameters
    kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=random_seed)
    
    # Fit the model to the data and predict cluster labels
    kmeans.fit(data)
    labels = kmeans.predict(data)
    
    return labels
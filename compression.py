from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np

class Compression:

    def __init__(self, data):
        self.data = data
        self.compressed_data = 0
        self.original_data = self.data
            
    def nonLossy(self, components):
        try:
            # Instantiate a PCA object with the desired number of components
            pca = PCA(n_components=components)

            # Fit and transform the data using PCA
            self.compressed_data = pca.fit_transform(self.data)

            # Inverse transform the compressed data to obtain the original data
            self.original_data = pca.inverse_transform(self.compressed_data)

            # Check if the original data and data are the same
            if not np.array_equal(original_data, data):
                raise Exception("Error: original data and compressed data do not match.")
        except:
            raise Exception("Invalid!")
        return self.compressed_data
    
    def lossy(self, clusters):
        try:
            # Instantiate a KMeans object with the desired number of clusters
            kmeans = KMeans(n_clusters=clusters)

            # Fit the data using KMeans
            kmeans.fit(self.data)

            # Quantize the data by replacing each feature with the nearest cluster center
            self.compressed_data = kmeans.cluster_centers_[kmeans.predict(self.data)]
        except:
            raise Exception("Invalid!")
        return self.compressed_data
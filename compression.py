from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np

class Compression:

    @staticmethod
    def nonLossy(data, components):
        try:
            # Instantiate a PCA object with the desired number of components
            pca = PCA(n_components=components)

            # Fit and transform the data using PCA
            compressed_data = pca.fit_transform(data)

            # Inverse transform the compressed data to obtain the original data
            original_data = pca.inverse_transform(compressed_data)

            # Check if the original data and data are the same
            if not np.array_equal(original_data, data):
                raise Exception("Error: original data and compressed data do not match.")
        except:
            raise Exception("Invalid!")
        return compressed_data, original_data
    
    @staticmethod
    def lossy(data, clusters):
        try:
            # Instantiate a KMeans object with the desired number of clusters
            kmeans = KMeans(n_clusters=clusters)

            # Fit the data using KMeans
            kmeans.fit(data)

            # Quantize the data by replacing each feature with the nearest cluster center
            compressed_data = kmeans.cluster_centers_[kmeans.predict(data)]
        except:
            raise Exception("Invalid!")
            
        return compressed_data

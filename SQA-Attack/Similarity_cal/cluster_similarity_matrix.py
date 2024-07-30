from scipy.linalg import blas
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

def cluster_similarity_matrix(similarity_matrix, num_clusters_range):
    silhouette_scores = []
    cluster_labels = []

    for num_clusters in num_clusters_range:
        # Perform hierarchical clustering
        clustering = AgglomerativeClustering(n_clusters=num_clusters, linkage='average')
        labels = clustering.fit_predict(similarity_matrix)

        # Compute silhouette score
        silhouette_avg = silhouette_score(similarity_matrix, labels, metric='precomputed')

        silhouette_scores.append(silhouette_avg)
        cluster_labels.append(labels)

    # Find the optimal number of clusters with the highest silhouette score
    optimal_num_clusters = num_clusters_range[silhouette_scores.index(max(silhouette_scores))]
    optimal_cluster_labels = cluster_labels[silhouette_scores.index(max(silhouette_scores))]

    return optimal_num_clusters, optimal_cluster_labels, silhouette_scores
from sklearn.mixture import GaussianMixture

def perform_clustering(embeddings, n_components=2):
    GMM = GaussianMixture(n_components=n_components, random_state=0)
    labels = GMM.fit_predict(embeddings)
    return labels, GMM


def cluster_re_embeddings(embeddings, n_components=2):
    gmm = GaussianMixture(n_components=n_components, random_state=0)
    labels = gmm.fit_predict(embeddings)
    return labels, gmm
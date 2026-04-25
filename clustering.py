from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def cluster_topics(texts):
    """Cluster texts into topics"""
    if len(texts) < 2:
        return [0] * len(texts)
    
    embeddings = model.encode(texts)
    n_clusters = min(3, len(texts))
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings)
    
    return labels.tolist()
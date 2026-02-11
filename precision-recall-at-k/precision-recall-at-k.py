import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    rec,rel = recommended,relevant
    numer = len([i for i in rec[:k] if i in rel])
    return [numer/k,numer/len(rel)]

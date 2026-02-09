import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    def normalize(a):
      return np.linalg.norm(a)
    
    A,B = np.array(a),np.array(b)
    mag_A,mag_B = normalize(A),normalize(B)
    return (A @ B) / (mag_A * mag_B) if mag_A != 0 and mag_B != 0 else 0
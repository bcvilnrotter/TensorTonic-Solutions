import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    return np.quantile(x,np.array(q)/100)
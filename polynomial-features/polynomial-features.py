import numpy as np

def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    deg_arr = np.array(range(degree+1))
    return [(i ** deg_arr).tolist() for i in values]
import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    
    if np.sum(p) != 1:
        raise ValueError(f' ... Sum of all probabilities is unequal to 1')
    
    return np.sum(np.array(x)*np.array(p))
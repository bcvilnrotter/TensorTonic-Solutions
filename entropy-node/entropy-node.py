import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if y == []:
        return 0.0
        
    y_arr = np.array(y)
    y_class = np.unique(y_arr,return_counts=True)
    y_prob = y_class[1]/len(y_arr)
    y_no_zero = y_prob[y_prob>0]
    return -np.sum(y_no_zero*np.log2(y_no_zero))
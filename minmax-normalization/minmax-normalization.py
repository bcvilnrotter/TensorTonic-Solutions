import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    
    arr_X = np.array(X)
    min_X, max_X = np.min(
        arr_X,axis=axis,keepdims=True),np.max(
            arr_X,axis=axis,keepdims=True)

    denom = np.where(np.equal(max_X,min_X),eps * max_X,max_X - min_X)
    return (arr_X - min_X) / denom
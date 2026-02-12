import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    def np_array(x):
      return np.array(x)
    w,g,G = map(np_array,[w,g,G])
    G = G + g**2
    return (
        np.around(w - (lr/np.sqrt(G+eps))*g,decimals=4),
        np.around(G,decimals=4))
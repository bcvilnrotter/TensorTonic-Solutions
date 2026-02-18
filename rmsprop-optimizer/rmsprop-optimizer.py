import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    g_arr = np.array(g)
    s_t = beta*np.array(s)+(1-beta)*g_arr**2
    return (w-lr*(1/np.sqrt(s_t+eps))*g_arr,s_t)
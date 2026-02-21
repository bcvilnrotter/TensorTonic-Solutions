import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g_arr = np.array(g)
    mod_g = np.sqrt(np.sum(g_arr**2))
    return g_arr if (mod_g <= max_norm) or (max_norm <= 0) else g_arr * (max_norm/mod_g)
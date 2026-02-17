import numpy as np

def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    probs = (np.array(priorities) ** alpha)
    probs_i = probs/np.sum(probs)
    w_i = (len(probs_i) * probs_i) ** (-beta)
    w_i_hat = w_i / np.max(w_i)
    return [probs_i.tolist(), w_i_hat.tolist()]
def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    n = len(rater1)
    if n != len(rater2):
        pass
    
    p_o = sum([1 if x == y else 0 for x,y in zip(rater1,rater2)]) / n
    p_e = sum([(rater1.count(i) * rater2.count(i)) / (n * n) for i in set(rater1 + rater2)])

    return (p_o - p_e)/(1 - p_e) if p_e != 1 else 1
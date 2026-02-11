def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    m,C = min_votes,global_mean
    return [(v * R + m * C)/(v+m)for R,v in items]
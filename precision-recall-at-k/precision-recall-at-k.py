def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    hits =0 
    for i in top_k:
        if i in relevant:
            hits+=1
    return [hits/k , hits/len(relevant)]
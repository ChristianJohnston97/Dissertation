import scipy.stats as stats

def kendallsTau(list1, list2):
    tau, p = stats.kendalltau(list1, list2)
    return tau

def spearmansRank(list1, list2):
    spear, p = stats.spearmanr(list1, list2)
    return spear

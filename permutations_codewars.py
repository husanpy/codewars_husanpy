import itertools


def permutations(string):
    """creates list of unique permutations of string by len(string)"""
    res = list(set([''.join(el) for el in itertools.permutations(string, len(string))]))
    res.sort()
    return res

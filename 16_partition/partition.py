def partition(lst, fn):
    """Partition lst by predicate.

    >>> partition([1, 2, 3, 4], lambda x: x % 2 == 0)
    [[2, 4], [1, 3]]
    
    >>> partition(["apple", "banana", "cherry"], lambda s: len(s) > 5)
    [['banana', 'cherry'], ['apple']]
    """
    
    true_list = []
    false_list = []

    for item in lst:
        if fn(item):
            true_list.append(item)
        else:
            false_list.append(item)

    return [true_list, false_list]

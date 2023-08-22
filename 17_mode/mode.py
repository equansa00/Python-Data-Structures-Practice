from collections import Counter

def mode(nums):
    """Return most-common number in list.

    >>> mode([1, 2, 1])
    1

    >>> mode([2, 2, 3, 3, 2])
    2
    """
    count = Counter(nums)
    most_common = count.most_common(1)
    return most_common[0][0]



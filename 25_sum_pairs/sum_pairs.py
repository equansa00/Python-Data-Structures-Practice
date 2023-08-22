def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

        >>> sum_pairs([4, 2, 10, 5, 1], 6)
        (4, 2)

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    seen = set()

    for n in nums:
        diff = goal - n
        if diff in seen:
            return (diff, n)
        seen.add(n)

    return ()

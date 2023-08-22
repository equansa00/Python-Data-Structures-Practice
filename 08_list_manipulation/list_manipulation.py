def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    >>> lst1 = [1, 2, 3]
    >>> list_manipulation(lst1, 'remove', 'end')
    3
    >>> lst1
    [1, 2]

    >>> lst2 = [1, 2, 3]
    >>> list_manipulation(lst2, 'remove', 'beginning')
    1
    >>> lst2
    [2, 3]

    >>> lst3 = [1, 2, 3]
    >>> list_manipulation(lst3, 'add', 'beginning', 20)
    [20, 1, 2, 3]
    >>> lst3
    [20, 1, 2, 3]

    >>> lst4 = [1, 2, 3]
    >>> list_manipulation(lst4, 'add', 'end', 30)
    [1, 2, 3, 30]
    >>> lst4
    [1, 2, 3, 30]

    """

    if command == 'remove':
        if location == 'end':
            return lst.pop()
        elif location == 'beginning':
            return lst.pop(0)
        else:
            return None

    elif command == 'add':
        if location == 'end':
            lst.append(value)
            return lst
        elif location == 'beginning':
            lst.insert(0, value)
            return lst
        else:
            return None

    else:
        return None

# If this script is run directly, the doctests will execute
if __name__ == "__main__":
    import doctest
    doctest.testmod()


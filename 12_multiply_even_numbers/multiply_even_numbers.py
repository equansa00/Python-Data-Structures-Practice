def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
    >>> multiply_even_numbers([2, 3, 4, 5, 6])
    48
        
    >>> multiply_even_numbers([3, 4, 5])
    4
        
    >>> multiply_even_numbers([1, 3, 5])
    1

    """
    result = 1
    found_even = False

    for num in nums:
        if num % 2 == 0:
            result *= num
            found_even = True

    return result if found_even else 1

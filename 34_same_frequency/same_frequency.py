def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_counts = {}
    for digit in str(num1):
        num1_counts[digit] = num1_counts.get(digit, 0) + 1

    num2_counts = {}
    for digit in str(num2):
        num2_counts[digit] = num2_counts.get(digit, 0) + 1

    return num1_counts == num2_counts
def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, (possibly truncating) & returning w/msg.

    >>> calculate('add', 2.5, 4)
    'The result is 6.5'

    >>> calculate('subtract', 4, 1.5, make_int=True)
    'The result is 2'

    >>> calculate('multiply', 1.5, 2)
    'The result is 3.0'

    >>> calculate('divide', 10, 4, message='I got')
    'I got 2.5'

    If a valid operation isn't provided, return None.
    
    >>> calculate('foo', 2, 3)
    
    """
    # Check the operation type and perform the operation.
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:  # Avoid division by zero
            return None
        result = a / b
    else:
        return None  # if the operation is not recognized

    # If make_int is True, truncate the result to an integer.
    if make_int:
        result = int(result)

    # Return the final result with the provided message.
    return f"{message} {result}"



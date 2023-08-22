def is_palindrome(phrase):
    """Is phrase a palindrome?
    
    >>> is_palindrome('tacocat')
    True

    >>> is_palindrome('noon')
    True

    >>> is_palindrome('robert')
    False

    >>> is_palindrome('taco cat')
    True

    >>> is_palindrome('Noon')
    True

    """
    # Convert to lowercase and remove spaces
    cleaned_phrase = phrase.lower().replace(" ", "")
    
    # Check if cleaned_phrase is the same as its reverse
    return cleaned_phrase == cleaned_phrase[::-1]

# If this script is run directly, the doctests will execute
if __name__ == "__main__":
    import doctest
    doctest.testmod()

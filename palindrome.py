# Manipulating Strings

def make_palindrome(s):
    """Create a palindrome with the given string as a prefix.
    
    A palindrome is text that reads the same forwards and backwards.
    
    :param s: A string to form the prefix of a new palindrome.
    """
    return s + s[::-1]

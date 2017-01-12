def twenty_seventeen():
    """Come up with the most creative expression that evaluates to 2017,
    using only numbers and the +, *, and - operators.

    >>> twenty_seventeen()
    2017
    >>> twenty_seventeen() + twenty_seventeen()
    4034
    """
    return 11 * 9 * 3 + 36 + 80 * 100 - 12 * 7 * 9 * 11 + 2000

if __name__ == "__main__":
    import doctest
    doctest.testmod()

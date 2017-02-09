# Kristian Snyder
# Lab 03
# 2 February 2017

# Q1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"
    if n <= 0:
        return 0
    else:
        return n + skip_add(n-2)


# Q6
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    a, b = sorted((a, b))[::-1]
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


# Q7
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n//2) + 1
    else:
        return hailstone(n*3+1) + 1


# Q8
def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    >>> fibonacci(5)
    5
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Q9
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m-1, n) + paths(m, n-1)

# Q11
def count_vals(nlst):
    """Returns the number of values in the nested list.

    >>> count_vals([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # nested list
    >>> count_vals(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]]
    >>> count_vals(x)
    6
    """
    "*** YOUR CODE HERE ***"
    if type(nlst) != list:
        return 1
    count = 0
    for item in nlst:
        if type(item) != list:
            count += 1
        else:
            count += count_vals(item)
    return count

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]]
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x = [2, [1, 1, 1, [1]], 1, 3, [2, 5]]
    >>> flatten(x)
    [2, 1, 1, 1, 1, 1, 3, 2, 5]
    """
    "*** YOUR CODE HERE ***"
    flat = []
    if type(lst) != list:
        return [lst]
    for item in lst:
        if type(item) == list:
            flat += flatten(item)
        else:
            flat.append(item)
    return flat

if __name__ == "__main__":
    import doctest
    doctest.testmod()

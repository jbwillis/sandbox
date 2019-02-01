"""
    doctest is a python module that searches for and runs example code embedded in 
    documentation comments, directly within the python file it is testing. This is 
    a way to document the use for and to test a program with one effort.
    >>> a = 30
"""

import math
print(__name__)
def distance(a1, b1, c1, a2, b2, c2):
    """ calculate the distance between two points
        Examples:
        >>> distance(0, 0, 0, 1, 0, 0)
        1.0
        >>> distance(0, 0, 0, 3, 4, 0)
        5.0
        >>> distance(0, 0, 34, 3, 4, 0) # this one should fail
        5.0
        >>> a
        30
    """
    return math.sqrt((a2-a1)**2 + (b2-b1)**2 + (c2-c1)**2)


if __name__ == "__main__":
    import doctest
    # doctest won't print anything if it succeeds and verbose isn't set to true
    doctest.testmod(verbose=True)

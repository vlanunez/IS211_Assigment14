def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


"""Examples:
    >> > fibonnaci(1)
    1
    >> > fibonnaci(10)
    55
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


"""
 Examples:
        >>> gcd(252, 105)
        21
        >>> gcd(100, 27)
        1
 """


def compareTo(s1, s2):
    if s1 == '' and s2 == '':
        return 0
    elif ord(s1[0]) > ord(s2[0]):
        return 0 + ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return 0 - ord(s2[0])
    elif s1[1:2] == '' and not s2[1:2] == '':
        return 0 - ord(s2[0])
    elif s2[1:2] == '' and not s1[1:2] == '':
        return 0 + ord(s1[0])
    elif s1[1:2] == '' and s2[1:2] == '':
        return 0
    else:
        return compareTo(s1[1:], s2[1:])


"""
    Examples:
            >>> compareTo("abracadabra", "poof")
            -112
            >>> compareTo("lmno", "hijkl")
            108
            >>> compareTo("", "")
            0
            >>> compareTo("boo", "book")
            -111
     """

""" Group Exercise 2 x n tiles """


def tiles(n):
    """

    :param n: width of 2 x n rectangle
    :return: The number of ways to fill up the rectangle
    """
    # O(2^n), how to improve
    if n <= 2:
        return n
    else:
        return tiles(n - 1) + tiles(n - 2)


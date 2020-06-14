""" Bonus Question """


def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1


def gcd_of_strings(str1: str, str2: str):
    """
    For strings S and T, we say "T divides S" if and only if S = T + ... + T
    (T concatenated with itself 1 or more times)

    return the largest string that divides both str1 and str2.

    e.g.
    gcd_of_strings("ABCABC", "ABC") -> "ABC"
    gcd_of_strings("ABABAB", "ABAB") -> "AB"
    gcd_of_strings("LAMP", "CODE") -> ""

    :param str1: string.
    :param str2: string.
    :return: the largest string that divides str1 and str2.
    """
    if len(str1) == 0 or len(str2) == 0:
        return ""
    while len(str2) != 0:
        if len(str2) > len(str1):
            mid = str1
            str1 = str2
            str2 = mid
        mid = str1
        str1 = str2
        if mid.find(str2) != -1:
            str2 = mid[0:mid.find(str2)] + mid[mid.find(str2)+len(str2):]
        else:
            str1 = ""
            str2 = ""
    return str1


print(gcd_of_strings("ABABC", "ABC"))
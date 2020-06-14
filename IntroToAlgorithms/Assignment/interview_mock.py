# how to reverse a string


def revers_string(str):
    res = ""
    for i in range(len(str)-1, -1, -1):
        res += str[i]
    return res


def revers_string_swap(str):
    # string in python, they are immutable
    l = list(str)
    for i in range(0, len(str)//2):
        temp = l[i]
        l[i] = l[len(str)-i-1]
        l[len(str)-i-1] = temp
    return "".join(l)


print(revers_string_swap("hello"))

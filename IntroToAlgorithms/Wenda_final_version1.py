""" Final Exam V1 """


# please submit your python file upon completion.

def binary_search(l: list, target: int, start: int, end: int):
    """
    Write the binary search algorithm recursively without using loops.
    It returns location(index) of target in given list l[start:end] is present,
    otherwise return -1

    :param l: collection of elements
    :param target: element we are searching for
    :param start: start index for searching range
    :param end: end index for searching range
    :return: the index of target in the list or -1 (if target is not in the list)
    """
    try:
        if start > end:
            return -1
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        if l[mid] < target:
            start = mid + 1
            return binary_search(l, target, start, end)
        if l[mid] > target:
            end = mid - 1
            return binary_search(l, target, start, end)
    except IndexError as e:
        print(e)


print(binary_search([1, 5, 6, 9, 10, 15, 17, 20, 34], 5, 0, 8))


def is_vowel(s: str):
    """
    [This is a helper function you can use to solve the reverse_vowels problem.]
    Check if s is a vowel.

    i.e.
    is_vowel("A") -> True
    is_vowel("a") -> True
    is_vowel("b") -> False
    """
    return s in "aeiouAEIOU"


def reverse_vowels(s: str):
    """
    Write an algorithm to remove all vowels from a string without replace() built-in method.
    You can write iteratively or recursively.

    e.g.
    reverse_vowels("hello") -> "holle"
    reverse_vowels("world") -> "world"
    reverse_vowels("awihatu") -> "uwahita"
    reverse_vowels("hello world") -> "hollo werld"
    reverse_vowels("") -> ""
    reverse_vowels("a") -> "a"

    :param s: string
    :return: string with vowels in reversed order.
    """
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    if is_vowel(s[0]) and is_vowel(s[-1]):
        a = s[0]
        b = s[-1]
        s = s[-1] + s[1:-1] + s[0]
        return s[0] + reverse_vowels(s[1:-1]) + s[-1]
    if not is_vowel(s[0]):
        return s[0] + reverse_vowels(s[1:])
    if not is_vowel(s[-1]):
        return reverse_vowels(s[:-1]) + s[-1]


print(reverse_vowels("awihatu"))



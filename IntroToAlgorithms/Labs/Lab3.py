"""
 String, List - Level 2.0
"""
import re


def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    times = 0
    while string != "":
        if string.find("hi") == -1:
            return times
        else:
            string = string[string.find("hi")+len("hi"):]
            times += 1
    return times


def count_hi_derrick(string: str):
    return string.count("hi")


if __name__ == "__main__":
    print(count_hi("h"))


def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    return string.count("cat") == string.count("dog")


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    times = 0
    while string != "":
        start = string.find("co")
        end = string.find("e")
        if start == -1 or end == -1:
            return times
        elif end - start == 3:
            string = string[end + 1:]
            times += 1
        elif start < end:
            string = string[start + 1:]
        elif end < start:
            string = string[end + 1:]
    return times


if __name__ == "__main__":
    print(count_code("AcdeBcoleccoreDD"))


def count_code_derrick(string: str):
    total = 0
    for i in range(len(string) - 3):
        if string[i:i+2] == "co" and string[i+4]:
            total += 1
    return total

    # return len(re.findall("co.e", string))


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    a = a.lower()
    b = b.lower()
    return (a.find(b) != -1 and a.find(b) == len(a)-len(b)) or (b.find(a) != -1 and b.find(a) == len(b)-len(a))


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    max_num = max(nums)
    min_num = min(nums)
    return max_num - min_num


if __name__ == "__main__":
    print(big_diff([10, 3, 5, 6]))


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    res = 0
    for i in range(len(nums)):
        if i == 0:
            if nums[i] != 13:
                res += nums[i]
        else:
            if nums[i] != 13 and nums[i-1] != 13:
                res += nums[i]
    return res


if __name__ == "__main__":
    print(sum13([13, 1, 2, 13, 2, 1, 13]))


def sum13_derrick(nums):
    i = 0
    total = 0
    while i < len(nums):
        if nums[i] != 13:
            total += nums[i]
            i += 1
        else:
            i += 2
    return total


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    # I learn this "light on and off" thought form Anzu.
    res = 0
    light = False
    for i in range(len(nums)):
        if not light:
            if nums[i] != 6:
                res += nums[i]
            else:
                light = True
        else:
            if nums[i] == 7:
                light = False
    return res


print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    for i in range(len(nums)):
        if i == 0:
            continue
        else:
            if nums[i] == 2 and nums[i-1] == 2:
                return True
    return False

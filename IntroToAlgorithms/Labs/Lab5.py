""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def selection_sort_ascending(alist):
    for scan in range(len(alist)-1):
        min_index = scan
        for j in range(scan+1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != scan:
            alist[scan], alist[min_index] = alist[min_index], alist[scan]


def selection_sort_descending(alist):
    for scan in range(len(alist)-1):
        max_index = scan
        for j in range(scan+1, len(alist)):
            if alist[j] > alist[max_index]:
                max_index = j
        if max_index != scan:
            alist[scan], alist[max_index] = alist[max_index], alist[scan]


def sort_half(alist):
    list_1 = alist[:len(alist)//2]
    list_2 = alist[len(alist)//2:]
    selection_sort_ascending(list_1)
    selection_sort_descending(list_2)
    alist = list_1 + list_2
    return alist


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    # https://www.youtube.com/watch?v=xF3TU-QlhJQ
    i = 0
    j = 0
    merged = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    if i < len(A):
        merged += A[i:]
    if j < len(B):
        merged += B[j:]
    return merged


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    for i in range(len(mylist)):
        if mylist[i] < 0:
            mylist[i] = 0
    return mylist


from Labs import Lab5

""" Merge Sort ALgorithem"""

# Time Complexity: O(nlogn)


def merge_sort(l):
    if len(l) <= 1:
        return l

    # devide
    left = l[:len(l)//2]
    right = l[len(l)//2:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # conquer (merge)
    return Lab5.merge_two(sorted_left, sorted_right)


print(merge_sort([2, 5, 8, 5, 3, 67, 45]))

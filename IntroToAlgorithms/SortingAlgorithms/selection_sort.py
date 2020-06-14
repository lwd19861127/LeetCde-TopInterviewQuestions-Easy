# Selection Sort
# pseudo-code
# for each scan from 0 to len(alist)
#   find the min element
#   swap the min element with alsit(scan)

# Time Complexity
# O(n^2)


def selection_sort(alist):
    steps = 0
    for scan in range(len(alist)-1):
        min_index = scan
        for j in range(scan+1, len(alist)):
            steps += 1
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != scan:
            alist[scan], alist[min_index] = alist[min_index], alist[scan]
    print("steps:", steps)


a = [5, 1, 4, 2, 3]
selection_sort(a)
print(a)

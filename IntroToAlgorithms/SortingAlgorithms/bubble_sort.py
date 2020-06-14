# Bubble sort
# (pseudo-code)
# List = [...]
# for each i from 1 to len(list)
#   compare two adjacent elements
#   if the first element is greater than the second element
#       wap two elements

# Time Complexity
# O(n^2) algorithm
def bubble_sort(alist):
    for scan in range(len(alist)):
        #swap_counts = 0
        swapped = False
        for j in range(len(alist)-1-scan):
            if alist[j] > alist[j+1]:
                # swap_counts += 1
                swapped = True
                # alist[j], alist[j+1] = alist[j+1], alist[j]
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
        #if swap_counts == 0:
        if not swapped:
            break
    #print("steps:", swap_counts)


a = [5, 1, 4]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bubble_sort(a)
print(a)

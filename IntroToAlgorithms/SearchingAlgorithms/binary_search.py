alist = ["Australia", "Brazil", "Canada",
         "Denmark", "Ecuador", "France",
         "Germany", "Honduras", "Iran",
         "Japan", "Korea", "Latvia",
         "Mexico", "Netherlands", "Oman",
         "Philippines", "Qatar", "Russia",
         "Spain", "Turkey", "Uruguay",
         "Vietnam", "Wales", "Xochimilco",
         "Yemen", "Zambia"]


def binary_search(collection, target):
    """
    - how you look up a word in dictionary or a contact in phone book.
    * Items have to be sorted!
    :param collection:
    :param target:
    :return:
    """
    start = 0
    end = len(collection) - 1
    while start <= end:
        middle = (start + end) // 2
        if target > collection[middle]:
            start = middle + 1
        elif target < collection[middle]:
            end = middle - 1
        elif target == collection[middle]:
            return middle
    return -1

    # for _ in range(len(collection)):
    #    if start > end:
    #        break
    #    middle = (start + end) // 2
    #    if target > collection[middle]:
    #        start = middle+1
    #    elif target < collection[middle]:
    #        end = middle-1
    #    elif target == collection[middle]:
    #        return middle
    # return -1


print(binary_search(alist, "Xochimilco"))



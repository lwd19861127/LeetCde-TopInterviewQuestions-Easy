# Linear Search

alist = ["Apple", "Banana", "Kiwi", "Peach",
         "Watermelon", "Mango", "Pears",
         "Grapes", "Mangosteen", "Strawberry"]

def linear_search(collection, target):
    """
    Return the index of target object from collection.
    Return -1 if the target does not exist in the collection.
    """

    for i in range(len(collection)):
        if collection[i] == target:
            return i
    return -1


print(linear_search(alist, "Strawberry"))
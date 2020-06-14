# Data structure
# list: A sequence of items (elements)

# 1. creat a list
squares = [1, 4, 9, 16, 25, 36, 49]
print(squares)

# 2. list operations
animals = ["Eagle", "Snake", "Panda", "lion", "Tiger", "Bear"]
animals += ["Koala", "Dog"]  # add two items to the list
print(animals)

animals.append("Cat")  # add "Cat" item to the list, and return None
print(animals)
animals.insert(0, "Monkey")  # insert "Monkey" at 0 index, and return None
print(animals)

animals.remove("Snake")
print(animals)
print(animals.pop(0))  # pop the element at index 0, and return the removed element

animals.count("Cat")  # 1

# index: returns the index of the first element in the list
print(animals.index("lion"))
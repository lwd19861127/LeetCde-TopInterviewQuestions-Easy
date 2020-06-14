# lists, string, tuples - index-based (0,1,2,...)
# Dictionary: A collection of key-value pairs
# A dictionary is similar to a list, except that you access its values by looking up
# a key instead of an index. A key can be any string or a number.

contacts = {"John": "778-123-1234",
            "Dan": "604-123-1234",
            "Max": "778-123-1234",
            "John": "213-1234-1234"}
# Key has to be "unique"
print(contacts["John"])

contacts["Silva"] = "780-123-1234"  # add a new item to dictionary
contacts["Silva"] = "483-123-1234"  # update the value

del contacts["Silva"]  # remove key-value pair form the dictionary
print(contacts)

# Get the keys as list
print(list(contacts.keys()))

# Get the values as list
print(list(contacts.values()))

# 'in' keyword
# The in keyword is used to check if a list or dictionary contains a specific item.
print("John" in contacts)

# Extra: Set

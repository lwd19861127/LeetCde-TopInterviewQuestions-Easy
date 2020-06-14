# String (str) : A sequence of charafcters in "" or ''

# + Concatenation: combining two strings
print("hello" + "world")

# * multiplication: repeat stings
print("hello" * 5)

# String indexing (position)
singer = "Justin Bieber"
print(singer[7])  # "B"
print(singer[-1])  # last char
# print(singer[-14])  # Error (out of index)


# String slicing
# index
# syntax => [start index : end index]
# end index is not inclusive
actor = "Brad Pitt"
print(actor[0:4])

# shortcuts
# starting at 0 index
print(actor[:4])
# starting at 5 to the end.
print(actor[5:])
# from 0 to the end(copy).
print(actor[:])

# How to get the number of characters
print(len(actor))  # 9
print(actor[-1])
print(actor[len(actor)-1])
print(actor[8])
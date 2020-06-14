# Tuples are almost identical to lists.
# The only big difference between lists and tuples is that
# tuples cannot be modified (immutable)
# You cannot add(append), change, or delete elements from the tuple.

# Tuples = 'immutable lists'
vowel_alphabets = ("a", "e", "i", "o", "u")

# vowel_alphabets[0] = "k"  # Error

# Use Cases
# 1. return multiple values form a function


def a():
    x = (1_000_000, "Don")  # 1_000_000 is just number (syntactic sugar)
    return x

# 2. check if an item is in a collection


print("a" in vowel_alphabets)

# 3. multiple assignments
year, country = (2019, "Canada")

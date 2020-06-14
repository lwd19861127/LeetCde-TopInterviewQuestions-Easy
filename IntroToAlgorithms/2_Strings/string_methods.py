city = "vancouver"
print(city.upper())  # VANCOUVER
print(city.lower())  # vancouver
print(city.capitalize())  # Vancouver

# Index: returns the index of substring, but if it doesn't exist, error
# Find: returns the index of fist occurrence of substring, no match will return -1
print(city.index("v"))  # 0
print(city.index("cou"))  # 3 (it always returns the starts)
print(city.find("V"))  # -1
print(city.find("cou"))  # 3

# count: returns the occurrences of substring in string
# case-sensitive (O) vs case-insensitive (X)
greetings = "Hello Hello Hello"
print(greetings.count("Hello"))  # 3

# Checking characters in string
my_str = "Hello"
my_int = "123"

# isalnum(): checks alphanumeric characters (alphabets + numbers)
# isalpha(): checks if all characters are alphabets
# isdigit(): checks digit characters
# isupper(): checks if characters are uppercase
# islower(): checks if characters are lowercase
# isspace(): checks whitespace characters (space, tab \t, newline \n)
print(my_int.isdigit())

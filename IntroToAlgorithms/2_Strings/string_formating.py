# 'in' operator
# If you want check whether a string contains a specific letter or a substring, you can use 'in' keyword.

favorite = "ice cream" "helado"

print("ice" in favorite)  # True

# Escaping characters (\)(\",\')
dont_worry = "Don't worry about the \"weather\""
print(dont_worry)
message = "Hi, \nHow are you? \nI'm doing good!"
print(message)

# Multi-line strings
phrase = """
It is a really long string
trple-quoted strings are used
to define multi-line strings
"""
print(phrase)

# string formatting
# %s: string
# %d: decimal (integer)
name = "Derrick"
message = "Hello, pycharm! Myname is %s" % name
print(message)
current_year = 2019
year = "It's %d" % current_year
print(year)

info = "name = %s, year = %d" % (name, current_year)
print(info)

# string interpolation (from python 3.6) (more common)
a = 3
b = 4
print(f"{a} multiply {b} is {a * b}")
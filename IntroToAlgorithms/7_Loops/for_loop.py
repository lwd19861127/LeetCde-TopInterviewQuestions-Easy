# Loops - to repeat code
"""
# for loops are used to iterate over a given sequence.
# On each iteration, the variable (loop variable) defined in the for loop will be
# assigned to the next value(sequence).

# Numbers: a range of numbers
# range(end): 0 to end-1
for i in range(10):  # range(10): 0...9
    print(i)
# range(start, end): start to end-1
for i in range(3, 10):  # range(3, 10): 3...9
    print(i)
# range(start, end, steps)
for i in range(0, 10, 2):  # range(0, 10, 2): from 0...9 go 2 steps at a time
    print(i)  # 0, 2, 4, 8

# Function Overloading
# "overloading a function with a different set of parameters"

# Exercises
# 1. Write a loop to print all even numbers from 0 to 100
for i in range(0, 101, 2):
    print(i, end=", ")
print()
for i in range(101):
    if i % 2 == 0:
        print(i, end=", ")
print()
# 2. Write a loop to print all odd numbers from 0 to 100
for i in range(1, 100, 2):
    print(i, end=", ")
print()
for i in range(101):
    if i % 2 == 1:
        print(i, end=", ")
print()

# Strings: a sequence of characters
for ch in "Hello":
    print(ch)

# lists: a sqeuence of items
for item in ["hello", "hola", "world"]:
    print(item)

print()
# Exercises
# Print the names that have less than 5 characters from the given list.
names = ["Derrick", "Diego", "Rick",
         "Richard", "Anzu", "Wenda",
         "Yusuke", "Ryo", "Biance",
         "Tae", "Kam", "Elen",
         "Naoki", "Daniel", "Shohei",
         "Hotsuma", "Yuka", "Mika",
         "Yuki", "Douglas", "Gabriel"]
for name in names:
    if len(name) < 5:
        print(name)
print()
"""
# What is the value of (2^0 + 2^1 + ... + 2^30)
answer = 0
for power in range(0, 31):
    a = 1
    for _ in range(power):
        a *= 2
    answer += a
print(answer)

answer1 = 0
for i in range(31):
    answer1 += (2 ** i)
print(answer1)

answer3 = 2 ** 31 - 1
print(answer3)




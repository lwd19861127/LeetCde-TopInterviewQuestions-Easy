# A while loop is similar to an if statment.
# it executes some code if some condition is true.
# it will continue to execute the code for as long as the condition is true.

num = 1
while num <= 10:
    print(num, end=", ")
    num += 1
print()

# Exercises
# Print all squares from 1 to 99.(1**2, 2**2, 3**2, ...)

num = 1
num1 = 1
while num <= 99:
    num = num1 ** 2
    if num <= 99:
        print(num, end=", ")
    num1 += 1
print()

n = 1
while (n * n) < 100:
    print(n * n, end=", ")
    n += 1
print()
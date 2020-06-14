# Prints the given number of starts in the consol
# assume n >= 1


def print_starts(n):
    # base case
    if n == 1:
        print("*", end="")
    # recursive case
    else:
        print("*", end="")
        print_starts(n-1)


print_starts(5)
print()
print_starts(2)
print()


# Factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# Factorial recursively - without using a loop
def factorial_recur(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    else:
        return n * factorial_recur(n - 1)


#   n'th position Sequence
# fib seq: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# position:0, 1, 2, 3, 4, 5, 6,  7,  8,  9,  10, ...
def fibonacci(n):
    """Iteratively (loop)"""
    a = 1
    b = 1
    res = 0
    for _ in range(n-1):
        res = a + b
        a = b
        b = res
    return res


print(fibonacci(5))


def fibonacci_recur(n):
    """Recursively (loop)"""
    res = 0
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive
    else:
        return fibonacci_recur(n-2) + fibonacci_recur(n-1)


print(fibonacci_recur(5))


# pow exercise
def power_recur(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power_recur(base, exp-1)


print(power_recur(2, 10))

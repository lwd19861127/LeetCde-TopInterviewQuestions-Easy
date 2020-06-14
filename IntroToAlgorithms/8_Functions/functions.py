# Functions are a convenient way to divide your code into useful blocks, make it more
# readable and help 'reuse' it.
# In Python, functions are defined using the keyword 'def', followed by function's name.

# "A reusable block of code"

# define a function
def print_menu():
    print("MENU")
    print("1. Tacos")
    print("2. Brazilian BBQ")
    print("3. Kebab")
    print("4. Hotpot")
    print("5. Sashimi")
    print("6. Sinigang")
    print("7. Kimchi")

# call, run, execute the function
print_menu()


# Parameters vs Arguments


def add_two(a, b):
    return a + b


result = add_two(10, 20) # 10, 20: arguments
print(result)

# Define a function similar to 'range' function


def my_range(start, end, steps=1):  # Default parameters
    """
    Returns a list of numbers of integers from start to end
    by steps.
    :param start:
    :param end:
    :param steps:
    :return:
    """

    m = []
    i = start
    while i < end:
        m.append(i)
        i += steps
    return m


print(my_range(1, 10, 2))


def your_range(*args):
    if len(args) == 1:
        m = []
        i = 0
        while i < args[0]:
            m.append(i)
            i += 1
        return m
    elif len(args) == 2:
        m = []
        i = args[0]
        while i < args[1]:
            m.append(i)
            i += 1
        return m
    elif len(args) == 3:
        m = []
        i = args[0]
        while i < args[1]:
            m.append(i)
            i += args[2]
        return m
    else:
        print("Invalid number of arguments")
        return


print(your_range(10))
print(your_range(0, 10))
print(your_range(0, 10, 1))
print(your_range(0, 10, 1, 4))


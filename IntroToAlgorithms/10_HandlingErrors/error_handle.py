# Errors
# syntax(grammar) Error: happens when Python cannot interpret your code,
# since we didn't follow the correct syntax for Python.
# These errors you're likely to get when you make a typo.
# (red underline) - (compile-time)

# Exceptions: happens when unexpected things happen during the execution
# of a program (run-time), even if the code is syntactically correct.
# There are different types of built-in exceptions in Python, and you can
# see which exception is 'thrown' in the error message.
# -> please read the error message!
# -> the are not supposed to scare you.
# -> they are trying to help you!


# try-except block
# ValueError: wrong invalid chars
# KeyboardInterrupt: ^ + c
# EOF: ^ + d
while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        c = a / b
        print(c)
        break
    except ValueError as err:
        print(err)
        print("Invalid input. Please enter a number")
    except KeyboardInterrupt:
        print("No input taken.")
        break
    except EOFError as e:
        print(f"{e}")
        break
    except ZeroDivisionError as e:
        print(f"Invalid input: {e}")
    finally:
        print("Done!")
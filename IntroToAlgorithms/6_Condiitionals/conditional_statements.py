# Getting user input
# input(prompt) - it prints the prompt message and waits for the user input
#                 and whe user hits enter, it returns the user input as 'string'.

user_input = input("Enter your age?")
print(type(user_input))

if int(user_input) >= 21:
    print("You can start drinking.")
elif 13 < int(user_input) < 21:
    print("Study hard!")
else:
    print("Play video games!")

""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    lower_bound = 1
    upper_bound = 1000
    count = 0
    found = False
    while not found and upper_bound >= lower_bound:
        try:
            guess = int(input(f"Enter your guess from {lower_bound} to {upper_bound}: "))
            count += 1
            if guess < lower_bound or guess > upper_bound:
                raise Exception
            if guess == answer:
                print("You got it! The hidden number is", guess)
                print(f"It took you {count} guess(es).")
                break
            elif guess > answer:
                upper_bound = guess - 1
            else:
                lower_bound = guess + 1
            print(f"Wrong! Guess count: {count}")

        except:
            print("Invalid Input.")


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()




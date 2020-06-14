""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    print(f"\'{answer}\' Cover your eyes, you can't see this!\n")
    # your code goes here.

    step = 0
    start = 1
    end = 1000
    while True:
        try:
            guss = int(input(f"1 dollar for one shot! Get the number, get the same money\nEnter your guss number form {start} to {end}:\n"))
            if guss < start or guss > end:
                print("Bed Boy! Please notice the Range! This does't count\n")
                continue
            if guss == answer:
                step += 1
                print(f"Good Boy, You got it! the hidden number is {answer}")
                if step < answer:
                    print(f"You just cost {step} to get {answer}")
                else:
                    print(f"You got {answer}, but lost {step}")
                break
            else:
                step += 1
                if guss < answer:
                    start = guss + 1
                elif guss > answer:
                    end = guss - 1
                print(f"Come on! Give another tyr! You've cost: {step}\n")
        except ValueError as e:
            print(f"Invalid Input: {e}")
        except KeyboardInterrupt:
            print("No input taken.")
            break
        except EOFError as e:
            print(f"{e}")
            break


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()




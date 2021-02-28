import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting
    the user, until a valid 'int' (single quotes) is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print(f"{temp} is an invalid number.")


help(get_integer)
highest = int(input("Please enter a number to be the highest value for guessing: "))
answer = random.randint(1, highest)

print("If you want to quit the game, please press 0.")
print(f"I have guessed a number, from the range 1-{highest}, now you got to guess what it is!")
input(f"Please guess a number from 1-{highest}: ")
guess = int(input())
guesses = 0
while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        print("Ok, maybe next time we can play")
        break
    elif guess < answer:
        print("Please guess higher")
        guesses += 1
    elif guess > answer:
        print("Please guess lower")
        guesses += 1
print(f"Well Done, my number was indeed {answer}")
print(f"You guessed it in {guesses} guesses!")



















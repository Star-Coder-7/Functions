def fizz_buzz(number: int) -> str:
    """
    Play Fizz Buzz

    :param number: The number (i) to check.
    :return: "fizz buzz!!!" if number is divisible by 3 and 5 (by 15).
       "fizz!" if the number is divisible only by 3.
       "buzz!" if the number is divisible only by 5.
       if the number isn't by 5, 3, or both (15), just the number is returned in its normal numeric-string form.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


print("Type stop or quit to terminate immediately whenever you want.")
input("We are going to play Fizz Buzz. Press enter to begin: ")
print()
firstTurn = input("Who will take the first turn, you or me?\nType 'user' for you to go first, or 'python' for me to go"
                  " first.\nAlternatively, type stop or quit to not play: ")

next_num = 0
while next_num <= 100:
    if firstTurn == 'stop'.casefold() or firstTurn == 'quit'.casefold():
        print("Alright, maybe next time")
        break
    elif firstTurn == 'python'.casefold():
        next_num += 1
        print(fizz_buzz(next_num))
        next_num += 1
        correct_answer = fizz_buzz(next_num)
        user_answer = input("Your turn: ").casefold()
        if user_answer == "stop" or user_answer == "quit".casefold():
            print("Alright, maybe we can play next time.")
            break
        elif user_answer == correct_answer:
            print("My turn: ")
        else:
            print("Oh dear, you have entered a wrong answer. Try again next time!")
            print("The correct response was", correct_answer)
            break
    elif firstTurn == 'user'.casefold():
        next_num += 1
        correct_answer = fizz_buzz(next_num)
        user_answer = input("Your turn: ").casefold()
        if user_answer == "stop" or user_answer == "quit".casefold():
            print("Alright, maybe we can play next time.")
            break
        elif user_answer == correct_answer:
            print("My turn: ")
        else:
            print("Oh dear, you have entered a wrong answer. Try again next time!")
            print("The correct response was", correct_answer)
            break
        next_num += 1
        print(fizz_buzz(next_num))
    else:
        print("Sorry, that is an invalid response.")
        firstTurn = input("Who will take the first turn, you or me?\nType 'user' for you to go first, or 'python' for "
                          "me to go first.\nAlternatively, type stop or quit to not play: ")
else:
    print("Well done, you and I made no errors and crossed 100!")




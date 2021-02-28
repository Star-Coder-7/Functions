LOW = 1
HIGH = int(input("Please enter a maximum number to make the range: "))

print("Type stop or quit to end the game.")
# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print(f"\tGuessing in the range {low} to {high}")
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h" or high_low == "higher".casefold():
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l" or high_low == "lower".casefold():
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c" or high_low == "correct".casefold():
        elif guess == answer:
            # print(f"I got it in {guesses} guesses!")
            # break
            return guesses
        # else:
        #     print(f"Sorry, but {high_low} is invalid, please enter h, l or c")

        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print(f"{number} guessed in {number_of_guesses}!")

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print(f"Yes! I guessed without being told {correct_count} times. The max is {max_guesses} guesses.")

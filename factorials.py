def factorial(number: int) -> int:
    """
    To work out the factorials of the number the user enters.
    A factorial of a number is all the numbers from 1-itself up to that number multiplied together
    (e.g 5 = 1 * 2 * 3 * 4 * 5 = 120)

    :param number: the number `i` to factorise
    :return: 1 if `number` is 0 and 1
    factorial of `number`, if above 1.
    """
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


def float_factorial(float_number: float) -> float:
    """
    To work out the factorials of the number the user enters.
    A factorial of a number is all the numbers from 1-itself up to that number multiplied together
    (e.g 5 = 1 * 2 * 3 * 4 * 5 = 120)

    :param float_number: the number `i` to factorise
    :return: 0 if `number` is 0
    factorial of `number`, if above 0.
    """
    if float_number == 1.0:
        return 1
    else:
        return float_number * float_factorial(float_number - 0.1)


user = input("Do you want to put an integer, decimal or stop playing? Press i for integer, d for decimal "
             "number and enter to stop playing: ")

while user != "":
    if user == "d".casefold() or user == "decimal".casefold():
        user_number = float(input("Please enter a decimal number in its numeric form to factorise: "))
        print(float_factorial(user_number))
        user = input("Do you want to put an integer, decimal or stop playing? Press i for integer, "
                     "d for decimal "
                     "number and enter to stop playing: ")
    elif user == "i".casefold() or user == "integer".casefold():
        user_input = int(input("Please enter an integer in its numeric form to factorise: "))
        print(factorial(user_input))
        user = input("Do you want to put an integer, decimal or stop playing? Press i for integer, "
                     "d for decimal "
                     "number and enter to stop playing: ")
    else:
        print("Sorry, that is invalid.")
        user = input("Do you want to put an integer, decimal or stop playing? Press i for integer, "
                     "d for decimal "
                     "number and enter to stop playing: ")
else:
    print("Thank you for playing factorials with me!")

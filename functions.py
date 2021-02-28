def is_palindrome(string: str) -> bool:
    """
    This checks if a string is a palindrome.
    A palindrome is a word or sentence reading the same backwards
    and ignoring punctuation and spaces, as well as turning capital to lowercase
    (e.g race car, radar, do geese see God?)
    :param string: To check the string
    :return: True if the string is a palindrome, otherwise False
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    This ckecks if a sentence is a palindrome
    It does the same thing as the function 'is_palindrome'.
    :param sentence: To check the sentence
    :return: True if palindrome, False otherwise
    """
    string = "".join(char for char in sentence if char.isalnum())
    print(string.casefold())
    return is_palindrome(string)


word_sentence = input("Please enter a word or sentence to check: ")

while word_sentence != "" or word_sentence != 0:
    if palindrome_sentence(word_sentence):
        print(f"{word_sentence} is a palindrome")
        word_sentence = input("Please enter a word or sentence to check: ")
    else:
        print(f"{word_sentence} is not a palindrome")
        word_sentence = input("Please enter a word or sentence to check: ")
else:
    print("You have chosen to quit the program")

p = palindrome_sentence()


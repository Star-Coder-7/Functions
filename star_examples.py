numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_asterisk(*args):
    print(args)
    for x in args:
        print(x)


test_asterisk(0, 1, 2, 3, 4, 5)
print()
test_asterisk()

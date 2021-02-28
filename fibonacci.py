def fibonacci(n: int) -> int:
    """Return the `nth` Fibonacci number, or positive `n`.
    By the way, a fibonacci number is a number made by adding the previous two values.
    This means the first thirteen Fibonacci numbers, starting from 0 are:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


x = int(input("Please enter how many Fibonacci numbers you want to see. The first: "))
for i in range(x):
    print(i + 1, fibonacci(i))


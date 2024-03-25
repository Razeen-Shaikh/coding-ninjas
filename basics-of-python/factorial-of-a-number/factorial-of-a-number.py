n = int(input())

def factorial(n):
    """Calculate the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if n < 0:
    print("Error")
else:
    print(factorial(n))

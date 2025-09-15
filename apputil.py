import seaborn as sns
import pandas as pd


# update/add code below ...
# Exercise 1
def fib(n):
    """ 
    Calculate the nth Fibonacci number using recursion.

    Parameters
    --------
    n : int
        The position in the Fibonacci sequence (must be non-negative).

    Returns
    ------
    int
        The nth Fibonacci number.
    """
    # Base case: stop recursion when n is 0 or 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fib(n - 1) + fib(n - 2)

# Test cases
print(fib(0))  # Expected 0
print(fib(1))  # Expected 1
print(fib(5))  # Expected 5
print(fib(9))  # Expected 34



# Exercise 2
def to_binary(n):
    """
    Convert a non-negative integer to its binary representation as a string.
    
    Parameters
    ----------
    n : int
        A non-negative integer (Must be >= 0).

    Returns
    ----------
    str
        The binary representation of the integer as a string.

    Raises
    ------
    ValueError
        If the input is not a non-negative integer.
    """
    #Input validation
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case: stop recursion when n is 0 or 1
    if n == 0:
        return '0'
    elif n == 1:
        return '1'

    # Recursive case: divide n by 2 and concatenate the remainder
    return to_binary(n // 2) + str(n % 2)



# Exercise 3

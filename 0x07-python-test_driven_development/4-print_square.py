#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of a specified size using the character '#'.

    :param size: The size length of the square.
    :raises TypeError: If size is not an integer or if it is a float less than 0.
    :raises ValueError: If size is less than 0.
    """
    # Check if size is an integer or a float
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)

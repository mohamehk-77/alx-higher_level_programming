#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    :param text: The input text.
    :raises TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the input text
    for char in text:
        # Add the character to the result string
        result += char

        # Check if the character is '.', '?', or ':'
        if char in ['.', '?', ':']:
            # Add two new lines after the character
            result += '\n\n'

    # Print the result string with leading and trailing whitespaces removed
    print(result.strip())

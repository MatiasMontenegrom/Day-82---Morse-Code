def convert_to_morse():
    """
    Converts a given string to Morse code.

    Args:
        string (str): The input string to be converted.

    Returns:
        list: A list containing the Morse code representation of each character in the string.
    """
    string = input("Introduce a string: ")
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    words = []
    morse_list = []

    for char in string:
        words.append(char)

    for word in words:
        if word != " ":
            morse_list.append(morse_code[word.upper()])
        else:
            morse_list.append(" ")
    return morse_list



print(convert_to_morse())
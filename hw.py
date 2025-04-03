import string


def caesar_cipher(text, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift % 26:] + alphabet[:shift % 26]
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(table)

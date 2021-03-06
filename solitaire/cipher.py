from collections import deque


def add_modulo(keystream_int, text_char):
    text_int = ord(text_char) - 65
    add = (keystream_int + text_int) % 26
    return chr(add + 65)


def encrypt(plaintext, deck):
    """
    Encrypts a message with a key
    """
    plaintext = plaintext.upper()
    plaintext = [char for char in plaintext if char != ""]
    while len(plaintext) % 5 != 0:
        plaintext.append("X")

    keystream = deck.generate_keystream(len(plaintext))
    ciphertext = [
        add_modulo(keystream[i], char) for i, char in enumerate(plaintext)
    ]

    blocks = [
        "".join(ciphertext[i : i + 5]) for i in range(0, len(ciphertext), 5)
    ]
    return " ".join(blocks)


def substract_modulo(keystream_int, text_char):
    text_int = ord(text_char) - 65
    sub = (text_int - keystream_int) % 26
    return chr(sub + 65)


def decrypt(ciphertext, deck):
    """
    Decrypts a message with a key
    """
    ciphertext = ciphertext.upper()
    ciphertext = [char for char in ciphertext if char != " "]

    keystream = deck.generate_keystream(len(ciphertext))
    plaintext = [
        substract_modulo(keystream[i], char)
        for i, char in enumerate(ciphertext)
    ]

    blocks = [
        "".join(plaintext[i : i + 5]) for i in range(0, len(plaintext), 5)
    ]
    return " ".join(blocks)

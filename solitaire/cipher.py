from collections import deque

from solitaire.deck import derivate_deck


def add_modulo(keystream_int, text_char):
    keystream_int = keystream_int % 26
    text_int = ord(text_char)
    return chr(keystream_int + text_int)


def encrypt(plaintext, key):
    """
    Encrypts a message with a key
    """
    plaintext = plaintext.upper()
    plaintext = [char for char in plaintext if char != ""]
    while len(plaintext) % 5 != 0:
        plaintext.append("X")

    deck = derivate_deck(key)
    keystream = deck.generate_keystream(len(plaintext))
    ciphertext = [
        add_modulo(keystream[i], char) for i, char in enumerate(plaintext)
    ]

    blocks = [
        "".join(ciphertext[i : i + 5]) for i in range(0, len(ciphertext), 5)
    ]
    return " ".join(blocks)


def substract_modulo(keystream_int, text_char):
    keystream_int = keystream_int % 26
    text_int = ord(text_char)
    return chr(text_int - keystream_int)


def decrypt(ciphertext, key):
    """
    Decrypts a message with a key
    """
    ciphertext = ciphertext.upper()
    ciphertext = [char for char in ciphertext if char != " "]

    deck = derivate_deck(key)
    keystream = deck.generate_keystream(len(ciphertext))
    plaintext = [
        substract_modulo(keystream[i], char)
        for i, char in enumerate(ciphertext)
    ]

    blocks = [
        "".join(plaintext[i : i + 5]) for i in range(0, len(plaintext), 5)
    ]
    return " ".join(blocks)

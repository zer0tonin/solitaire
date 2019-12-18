from collections import deque

from solitaire.keystream import swap_a_joker, swap_b_joker, triple_cut, count_cut, generate_keystream

def derivate_deck(key):
    """
    Creates a deck from a string key
    """

    deck = deque([i for i in range(1, 53)])
    deck.append('A')
    deck.append('B')

    for char in key:
        swap_a_joker(deck)
        swap_b_joker(deck)
        triple_cut(deck)
        count_cut(deck)
        count_cut(deck, count=(ord(char) - 64))
    return deck


def add_modulo(keystream_int, text_char):
    keystream_int = keystream_int % 26
    text_int = ord(text_char)
    return chr(keystream_int + text_int)

def encrypt(plaintext, key):
    """
    Encrypts a message with a key
    """
    plaintext = plaintext.upper()
    while len(plaintext) % 5 != 0:
        plaintext = plaintext + "X"

    deck = derivate_deck(key)
    keystream = generate_keystream(deck, len(plaintext))
    print(keystream)
    ciphertext = [add_modulo(keystream[i], char) for i, char in enumerate(plaintext)]

    blocks = [''.join(ciphertext[i:i+5]) for i in range(0, len(ciphertext), 5)]
    return ' '.join(blocks)

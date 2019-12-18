from collections import deque

from solitaire.keystream import swap_a_joker, swap_b_joker, triple_cut, count_cut, generate_keystream

def derivate_deck(key):
    """
    Creates a deck from a string key
    """
    deck = deque([i for i in range(1, 55)])
    swap_a_joker(deck)
    swap_b_joker(deck)
    triple_cut(deck)
    count_cut(deck)
    [count_cut(deck, count=(ord(char) - 64)) for char in key]
    return deck


def encrypt(plaintext, key):
    """
    Encrypts a message with a key
    """
    deck = derivate_deck(key)
    keystream = generate_keystream(deck, len(plaintext))
    ciphertext = deque([chr(64 + ((keystream[i] + ord(char) - 64) % 26)) for i, char in enumerate(plaintext)])

    blocks = []
    while ciphertext:
        block = []
        for _ in range(5):
            if ciphertext:
                block.append(ciphertext.popleft())
            else:
                block.append("X")
        blocks.append(''.join(block))
    return ' '.join(blocks)

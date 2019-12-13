import sys
from random import shuffle
from collections import deque

from solitaire.keystream import get_next_keystream_char

# totally unsafe
def get_pseudorandom_deck():
    deck = [i+1 for i in range(53)]
    shuffle(deck)
    return deque(deck)

if __name__ == "__main__":
    get_next_keystream_char(get_pseudorandom_deck())

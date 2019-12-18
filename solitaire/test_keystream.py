from collections import deque

import pytest

import solitaire.keystream as keystream
from solitaire.cipher import derivate_deck

"""
The firt test case are taken from Bruce Shneier article: https://www.schneier.com/academic/solitaire/ (Sample Output part)
"""

@pytest.mark.parametrize(
    "deck,expected_deck",
    [
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B']),
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'B', 'A']),
        ),
        (
            deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B', 1]),
            deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'B', 'A', 1]),
        ),
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'B', 'A']),
            deque([1, 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'B']),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 'B', 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 'A', 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 'B', 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 19, 'A', 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
        ),
    ],
)
def test_swap_a_joker(deck, expected_deck):
    keystream.swap_a_joker(deck)
    assert deck == expected_deck


@pytest.mark.parametrize(
    "deck,expected_deck",
    [
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'B', 'A']),
            deque([1, 'B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A']),
        ),
        (
            deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'B', 'A', 1]),
            deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 1, 'B']),
        ),
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B']),
            deque([1, 2, 'B', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A']),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 'B', 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 'A', 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 36, 33, 'B', 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 'A', 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
        ),
    ],
)
def test_swap_b_joker(deck, expected_deck):
    keystream.swap_b_joker(deck)
    assert deck == expected_deck


@pytest.mark.parametrize(
    "deck,expected_deck",
    [
        (
            deque([1, 'B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A']),
            deque(['B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 1]),
        ),
        (
            deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 1, 'B']),
            deque(['A', 1, 'B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]),
        ),
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B']),
            deque(['A', 'B', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 'B', 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 'A', 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21, 'B', 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 'A', 32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1]),
        ),
    ],
)
def test_triple_cut(deck, expected_deck):
    keystream.triple_cut(deck)
    assert deck == expected_deck


@pytest.mark.parametrize(
    "deck,expected_deck",
    [
        (
            deque(['B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 1]),
            deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B', 1]),
        ),
        (
            deque(['A', 1, 'B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]),
            deque([51, 'A', 1, 'B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52]),
        ),
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B']),
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B']),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 'B', 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 'A', 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([1, 'B', 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 'A', 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 21]),
        ),
    ],
)
def test_count_cut(deck, expected_deck):
    keystream.count_cut(deck)
    assert deck == expected_deck


@pytest.mark.parametrize(
    "deck,output",
    [
        (
            deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 'A', 'B', 1]),
            4,
        ),
        (
            deque([51, 'A', 1, 'B', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52]),
            49,
        ),
    ],
)
def test_get_output_card(deck, output):
    assert output == keystream.get_output_card(deck)



@pytest.mark.parametrize(
    "key,expected",
    [
        (
            "",
            [4, 49, 10, 24, 8, 51, 44, 6, 4, 33, 20, 39, 19, 34, 42],
        ),
        (
            "F",
            [49, 24, 8, 46, 16, 1, 12, 33, 10, 10, 9, 27, 4, 32, 24],
        ),
        (
            "FO",
            [19, 46, 9, 24, 12, 1, 4, 43, 11, 32, 23, 39, 29, 34, 22],
        ),
        (
            "FOO",
            [8, 19, 7, 25, 20, 9, 8, 22, 32, 43, 5, 26, 17, 38, 48],
        ),
        (
            "A",
            [49, 14, 3, 26, 11, 32, 18, 2, 46, 37, 34, 42, 13, 18, 28],
        ),
        (
            "AA",
            [14, 7, 32, 22, 38, 23, 23, 2, 26, 8, 12, 2, 34, 16, 15],
        ),
        (
            "AAA",
            [3, 28, 18, 42, 24, 33, 1, 16, 51, 39, 6, 29, 43, 46, 45],
        ),
        (
            "B",
            [49, 16, 4, 30, 12, 40, 8, 19, 37, 25, 47, 29, 18, 16, 18],
        ),
        (
            "BC",
            [16, 13, 32, 17, 10, 42, 34, 7, 2, 37, 6, 48, 44, 28, 4],
        ),
        (
            "BCD",
            [5, 38, 20, 27, 50, 1, 38, 26, 49, 33, 39, 42, 49, 2, 35],
        ),
    ],
)
def test_generate_keystream(key, expected):
    deck = derivate_deck(key)
    assert keystream.generate_keystream(deck, len(expected)) == expected

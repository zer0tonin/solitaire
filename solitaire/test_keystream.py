from collections import deque

import pytest

import solitaire.keystream as keystream

@pytest.mark.parametrize(
    "deck,expected_deck",
    [
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 53]),
            deque([1, 53, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54]),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 19, 53, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
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
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]),
            deque([1, 2, 54, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]),
        ),
        (
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 53]),
            deque([1, 54, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 36, 33, 54, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
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
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]),
            deque([53, 54, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1]),
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
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]),
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]),
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            deque([1, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 21]),
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
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]),
            "A",
        ),
        (
            deque([32, 42, 38, 18, 43, 16, 41, 26, 24, 51, 20, 14, 40, 45, 34, 29, 39, 9, 7, 5, 48, 1, 54, 36, 33, 6, 35, 52, 44, 37, 22, 47, 25, 23, 15, 10, 30, 17, 4, 31, 53, 19, 13, 12, 28, 50, 49, 46, 2, 3, 11, 27, 8, 21]),
            "U",
        ),
    ],
)
def test_get_output_card(deck, output):
    assert output == chr(keystream.get_output_card(deck) + 64)

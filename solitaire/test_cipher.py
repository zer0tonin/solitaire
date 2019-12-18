import pytest

from solitaire.cipher import encrypt, derivate_deck
from solitaire.keystream import generate_keystream

# source: https://www.schneier.com/code/sol-test.txt
@pytest.mark.parametrize(
    "plaintext,key,keystream,ciphertext",
    [
        (
            "AAAAAAAAAAAAAAA",
            "",
            [4, 49, 10, 24, 8, 51, 44, 6, 4, 33, 20, 39, 19, 34, 42],
            "EXKYI ZSGEH UNTIQ",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "F",
            [49, 24, 8, 46, 16, 1, 12, 33, 10, 10, 9, 27, 4, 32, 24],
            "XYIUQ BMHKK JBEGY",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "FO",
            [19, 46, 9, 24, 12, 1, 4, 43, 11, 32, 23, 39, 29, 34, 22],
            "TUJYM BERLG XNDIW",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "FOO",
            [8, 19, 7, 25, 20, 9, 8, 22, 32, 43, 5, 26, 17, 38, 48],
            "ITHZU JIWGR FARMW",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "A",
            [49, 14, 3, 26, 11, 32, 18, 2, 46, 37, 34, 42, 13, 18, 28],
            "XODAL GSCUL IQNSC",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "AA",
            [14, 7, 32, 22, 38, 23, 23, 2, 26, 8, 12, 2, 34, 16, 15],
            "OHGWM XXCAI MCIQP",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "AAA",
            [3, 28, 18, 42, 24, 33, 1, 16, 51, 39, 6, 29, 43, 46, 45],
            "DCSQY HBQZN GDRUT",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "B",
            [49, 16, 4, 30, 12, 40, 8, 19, 37, 25, 47, 29, 18, 16, 18],
            "XQEEM OITLZ VDSQS",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "BC",
            [16, 13, 32, 17, 10, 42, 34, 7, 2, 37, 6, 48, 44, 28, 4],
            "QNGRK QIHCL GWSCE",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "BCD",
            [5, 38, 20, 27, 50, 1, 38, 26, 49, 33, 39, 42, 49, 2, 35],
            "FMUBY BMAXH NQXCJ",
        ),
        (
            "AAAAAAAAAAAAAAAAAAAAAAAAA",
            "CRYPTONOMICON",
            None,
            "SUGSR SXSWQ RMXOH IPBFP XARYQ",
        ),
    ],
)
def test_encrypt(plaintext, key, keystream, ciphertext):
    if keystream:
        deck = derivate_deck(key)
        assert generate_keystream(deck, len(plaintext)) == keystream
    assert encrypt(plaintext, key) == ciphertext

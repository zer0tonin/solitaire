import pytest

from solitaire.cipher import decrypt, encrypt, derivate_deck
from solitaire.keystream import generate_keystream

# source: https://www.schneier.com/code/sol-test.txt
@pytest.mark.parametrize(
    "plaintext,key,ciphertext",
    [
        (
            "AAAAAAAAAAAAAAA",
            "",
            "EXKYI ZSGEH UNTIQ",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "F",
            "XYIUQ BMHKK JBEGY",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "FO",
            "TUJYM BERLG XNDIW",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "FOO",
            "ITHZU JIWGR FARMW",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "A",
            "XODAL GSCUL IQNSC",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "AA",
            "OHGWM XXCAI MCIQP",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "AAA",
            "DCSQY HBQZN GDRUT",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "B",
            "XQEEM OITLZ VDSQS",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "BC",
            "QNGRK QIHCL GWSCE",
        ),
        (
            "AAAAAAAAAAAAAAA",
            "BCD",
            "FMUBY BMAXH NQXCJ",
        ),
        (
            "AAAAAAAAAAAAAAAAAAAAAAAAA",
            "CRYPTONOMICON",
            "SUGSR SXSWQ RMXOH IPBFP XARYQ",
        ),
    ],
)
def test_encrypt(plaintext, key, ciphertext):
    assert encrypt(plaintext, key) == ciphertext


@pytest.mark.parametrize(
    "ciphertext,key,plaintext",
    [
        (
            "EXKYI ZSGEH UNTIQ",
            "",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "XYIUQ BMHKK JBEGY",
            "F",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "TUJYM BERLG XNDIW",
            "FO",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "ITHZU JIWGR FARMW",
            "FOO",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "XODAL GSCUL IQNSC",
            "A",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "OHGWM XXCAI MCIQP",
            "AA",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "DCSQY HBQZN GDRUT",
            "AAA",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "XQEEM OITLZ VDSQS",
            "B",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "QNGRK QIHCL GWSCE",
            "BC",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "FMUBY BMAXH NQXCJ",
            "BCD",
            "AAAAA AAAAA AAAAA",
        ),
        (
            "SUGSR SXSWQ RMXOH IPBFP XARYQ",
            "CRYPTONOMICON",
            "AAAAA AAAAA AAAAA AAAAA AAAAA",
        ),
    ],
)
def test_decrypt(ciphertext, key, plaintext):
    assert decrypt(ciphertext, key) == plaintext

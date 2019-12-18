import pytest

from solitaire.cipher import encrypt

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

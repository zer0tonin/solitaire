import sys

from solitaire.cipher import encrypt

if __name__ == "__main__":
    try:
        ciphertext = encrypt(sys.argv[1], sys.argv[2])
    except IndexError:
        ciphertext = encrypt(sys.argv[1], "")
    print(ciphertext)

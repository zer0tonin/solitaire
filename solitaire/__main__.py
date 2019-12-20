import argparse

from solitaire.cipher import encrypt, decrypt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypts and decrypts strings using the solitaire algorithm")
    parser.add_argument("action", choices=["encrypt", "decrypt"], type=str)
    parser.add_argument("key", type=str)
    parser.add_argument("text", type=str)

    args = parser.parse_args()
    if args.action == "encrypt":
        print(encrypt(args.text, args.key))
    if args.action == "decrypt":
        print(decrypt(args.text, args.key))

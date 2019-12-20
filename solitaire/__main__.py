import argparse

from solitaire.cipher import encrypt, decrypt
from solitaire.deck import derivate_deck

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encrypts and decrypts strings using the solitaire algorithm"
    )
    parser.add_argument("action", choices=["encrypt", "decrypt"], type=str)
    parser.add_argument("key", type=str)
    parser.add_argument("text", type=str)
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--pretty", "-p", action="store_true")

    args = parser.parse_args()
    deck = derivate_deck(args.key, verbose=args.verbose, pretty=args.pretty)
    if args.action == "encrypt":
        print(encrypt(args.text, deck))
    elif args.action == "decrypt":
        print(decrypt(args.text, deck))

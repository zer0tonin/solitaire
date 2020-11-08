# Solitaire

An implementation of Bruce Schneier's Solitaire.

Original specifications: https://www.schneier.com/academic/solitaire/

Description and review: https://alicegg.tech/2020/01/03/solitaire.html

DO NOT EVER USE THIS IN A PRODUCTION SYSTEM

## Usage

`python -m solitaire [encrypt/decrypt] [key] [text] [--verbose/--pretty]`

Example:

`solitaire encrypt FOO ABCDE` -> `IUJCY`

`solitaire decrypt FOO IUJCY` -> `ABCDE`

The verbose and pretty flags allow you to visualize the state of the deck, using either numbers or unicode cards.

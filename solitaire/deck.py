from collections import deque
from solitaire.output import CARD_MAP
from solitaire.card import Card


def derivate_deck(key):
    """
    Creates a deck from a string key
    """

    deck = Deck([i for i in range(1, 53)])
    deck.cards.append(Card("A"))
    deck.cards.append(Card("B"))

    for char in key:
        deck.swap_a_joker()
        deck.swap_b_joker()
        deck.triple_cut()
        deck.count_cut()
        deck.count_cut(count=(ord(char) - 64))
    return deck


class Deck:
    def __init__(self, cards, verbose=False, pretty=False):
        self.cards = deque([Card(i) for i in cards])
        self.verbose = verbose
        self.pretty = pretty

    def __eq__(self, o):
        return isinstance(o, Deck) and self.cards == o.cards

    def print_state(self, label):
        if self.pretty:
            state = " ".join([CARD_MAP[c.value] for c in self.cards])
        elif self.verbose:
            state = " ".join([c.value for c in self.cards])

        if self.verbose or self.pretty:
            print(state)
            print(label)

    def generate_keystream(self, length):
        """
        Generates a keystream from a deck of card
        """
        return [self.get_next_keystream_char() for i in range(length)]

    def get_next_keystream_char(self):
        while True:
            self.print_state("--- Start ---")

            self.swap_a_joker()
            self.print_state("--- Step 1 ---")

            self.swap_b_joker()
            self.print_state("--- Step 2 ---")

            self.triple_cut()
            self.print_state("--- Step 3 ---")

            self.count_cut()
            self.print_state("--- Step 4 ---")

            result = self.get_output()
            if result:
                return result

    def swap_a_joker(self):
        """
        First step of the keystream generation
        Swaps joker A with the card below it
        """
        for i, card in enumerate(self.cards):
            if card.is_joker_a() and i == 53:
                cut = [self.cards.pop(), self.cards.popleft()]
                self.cards.extendleft(cut)
                return
            if card.is_joker_a():
                j = (i + 1) % 54
                swap = self.cards[j]
                self.cards[j] = card
                self.cards[i] = swap
                return

    def swap_b_joker(self):
        """
        Second step of the keystream generation
        Swaps joker B with the two cards below it
        """
        for i, card in enumerate(self.cards):
            if card.is_joker_b() and i == 53:
                top = self.cards.popleft()
                cut = [self.cards.pop(), self.cards.popleft(), top]
                self.cards.extendleft(cut)
                return
            if card.is_joker_b() and i == 52:
                bottom = self.cards.pop()
                cut = [self.cards.pop(), self.cards.popleft()]
                self.cards.append(bottom)
                self.cards.extendleft(cut)
                return
            if card.is_joker_b():
                j = (i + 1) % 54
                k = (i + 2) % 54
                swap = (self.cards[j], self.cards[k])
                self.cards[k] = card
                self.cards[j] = swap[1]
                self.cards[i] = swap[0]
                return

    def triple_cut(self):
        """
        Third step of the keystream generation
        Swap the cards above the first joker with the cards below the second joker
        """
        current_card = self.cards[0]
        before = deque()
        while not current_card.is_joker():
            before.append(self.cards.popleft())
            current_card = self.cards[0]

        current_card = self.cards[-1]
        after = deque()
        while not current_card.is_joker():
            after.appendleft(self.cards.pop())
            current_card = self.cards[-1]

        while before:
            self.cards.append(before.popleft())

        while after:
            self.cards.appendleft(after.pop())

    def count_cut(self, count=None):
        """
        Fourth step of the keystream generation
        Cuts after the number of the first card
        """
        bottom_card = self.cards.pop()
        if count is None:
            count = (
                53 if bottom_card.is_joker() else bottom_card.value
            )  # either joker counts 53

        cut = deque()
        for _ in range(count):
            cut.append(self.cards.popleft())

        while cut:
            self.cards.append(cut.popleft())

        self.cards.append(bottom_card)

    def get_output(self):
        """
        Fifth and last step, get the output using the top card
        """
        top_card = self.cards[0]
        if top_card.is_joker():
            output_card = self.cards[53]
        else:
            output_card = self.cards[top_card.value]
        if output_card.is_joker():
            return None
        return output_card.value

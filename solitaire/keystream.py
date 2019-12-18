from collections import deque

from solitaire.output import print_deck_state, is_verbose

def generate_keystream(deck, length):
    """
    Generates a keystream from a deck of card
    """
    return [get_next_keystream_char(deck) for i in range(length)]


def get_next_keystream_char(deck):
    while True:
        if is_verbose():
            print("--- Starting deck ---")
            print_deck_state(deck)

        swap_a_joker(deck)
        if is_verbose():
            print("--- Step 1 ---")
            print_deck_state(deck)

        swap_b_joker(deck)
        if is_verbose():
            print("--- Step 2 ---")
            print_deck_state(deck)

        triple_cut(deck)
        if is_verbose():
            print("--- Step 3 ---")
            print_deck_state(deck)

        count_cut(deck)
        if is_verbose():
            print("--- Step 4 ---")
            print_deck_state(deck)

        result = get_output_card(deck)
        if result:
            return result


def is_joker(card):
    return card in ('A', 'B')


def is_joker_a(card):
    return card == 'A'


def is_joker_b(card):
    return card == 'B'


def swap_a_joker(deck):
    """
    First step of the keystream generation
    Swaps joker A with the card below it
    """
    for i, card in enumerate(deck):
        if is_joker_a(card) and i == len(deck) - 1:
            top = deck.popleft()
            deck.pop()
            deck.appendleft(card)
            deck.appendleft(top)
            return
        if is_joker_a(card):
            j = (i + 1) % 54
            swap = deck[j]
            deck[j] = card
            deck[i] = swap
            return


def swap_b_joker(deck):
    """
    Second step of the keystream generation
    Swaps joker B with the two cards below it
    """
    for i, card in enumerate(deck):
        if is_joker_b(card) and i == len(deck) - 1:
            top = deck.popleft()
            top2 = deck.popleft()
            deck.pop()
            deck.appendleft(card)
            deck.appendleft(top2)
            deck.appendleft(top)
            return
        if is_joker_b(card) and i == len(deck) - 2:
            top = deck.popleft()
            bottom = deck.pop()
            deck.pop()
            deck.append(bottom)
            deck.appendleft(card)
            deck.appendleft(top)
            return
        if is_joker_b(card):
            j = (i + 1) % 54
            k = (i + 2) % 54
            swap = deck[j]
            swap2 = deck[k]
            deck[k] = card
            deck[j] = swap2
            deck[i] = swap
            return


def triple_cut(deck):
    """
    Third step of the keystream generation
    Swap the cards above the first joker with the cards below the second joker
    """
    current_card = deck[0]
    before = deque()
    while not is_joker(current_card):
        before.append(deck.popleft())
        current_card = deck[0]

    current_card = deck[-1]
    after = deque()
    while not is_joker(current_card):
        after.appendleft(deck.pop())
        current_card = deck[-1]

    while before:
        deck.append(before.popleft())

    while after:
        deck.appendleft(after.pop())


def count_cut(deck, count=None):
    """
    Fourth step of the keystream generation
    Cuts after the number of the first card
    """
    bottom_card = deck.pop()
    if count is None:
        count = 53 if is_joker(bottom_card) else bottom_card # either joker counts 53

    cut = deque()
    for _ in range(count):
        cut.append(deck.popleft())

    while cut:
        deck.append(cut.popleft())

    deck.append(bottom_card)


def get_output_card(deck):
    """
    Fifth and last step, get the output using the top card
    """
    top_card = deck[0]
    if is_joker(top_card):
        output_card = deck[53]
    else:
        output_card = deck[top_card]
    if is_joker(output_card):
        return None
    return output_card

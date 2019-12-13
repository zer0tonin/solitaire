from output import print_deck_state

def generate_keystream(deck, length):
    return [get_next_keystream_char(deck) for i in range(length)]


def get_next_keystream_char(deck):
    print("--- Starting deck ---")
    print_deck_state(deck)

    swap_a_joker(deck)
    print("--- Step 1 ---")
    print_deck_state(deck)

#    swap_b_joker(deck)
#    print("--- Step 3 ---")
#    print_deck_state(deck)


def swap_a_joker(deck):
    for i, card in enumerate(deck):
        if card == 53:
            next_card_index = (i + 1) % 54
            swap = deck[next_card_index]
            deck[next_card_index] = 53
            deck[i] = swap
            return

#def swap_b_joker(deck):
#    for i, card in enumerate(deck):
#        if card == 54 and i == 54:

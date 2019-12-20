class Card:
    def __init__(self, value):
        self.value = value

    def __eq__(self, o):
        return isinstance(self, Card) and self.value == o.value

    def is_joker(self):
        return self.value in ("A", "B")

    def is_joker_a(self):
        return self.value == "A"

    def is_joker_b(self):
        return self.value == "B"

class Card:

    def __init__(self, color, number, original=False, published=False):
        assert color == 'white' or color == 'black'
        self.color = color
        assert isinstance(number, int)
        assert 0 <= number <= 11
        self.number = number
        assert isinstance(published, bool)
        self.published = published
        assert isinstance(original, bool)
        self.original_card = original
        self.wrong_guess_history = set()

    def guess_number(self, number):
        if self.published:
            raise Exception('it has been published')
        if self.number == number:
            self.published = True
            return True
        self.wrong_guess_history.add(number)
        return False

    def __eq__(self, other):
        return self.color == other.color and self.number == other.number

    def __lt__(self, other):
        if self.number == other.number:
            return self.color < other.color
            # self.color is black and other.color is white
        else:
            return self.number < other.number

    def __hash__(self):
        return hash((self.color, self.number))

    def card_str(self):
        return ('B' if self.color == 'black' else 'W') + f"{self.number:02d}"

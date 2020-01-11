from unittest import TestCase

from GameModule.Card import Card


class TestCard(TestCase):

    def test_init(self):
        c = Card('white', 5)
        self.assertEqual(c.color, 'white')
        self.assertEqual(c.number, 5)
        self.assertEqual(c.published, False)
        with self.assertRaises(AssertionError):
            Card('red', 5)
        with self.assertRaises(AssertionError):
            Card('black', 15)
        with self.assertRaises(AssertionError):
            Card('black', 15, 1)
        with self.assertRaises(AssertionError):
            Card('black', 15, False, 1)

    def test_guess_number(self):
        c = Card('white', 5)
        self.assertEqual(c.published, False)
        c.guess_number(5)
        self.assertEqual(c.published, True)

        with self.assertRaises(Exception) as cm:
            c.guess_number(5)
        self.assertEqual(
            'it has been published',
            str(cm.exception)
        )

    def test_guess_number_for_wrong_guess_history(self):
        c = Card('white', 5)
        c.guess_number(6)
        c.guess_number(7)
        c.guess_number(7)

        self.assertSetEqual({6, 7}, c.wrong_guess_history)

    def test_sorted(self):
        hand = [Card('white', 10), Card('black', 5), Card('white', 5)]
        hand_sorted = sorted(hand)
        self.assertEqual(hand_sorted[0].color, 'black')
        self.assertEqual(hand_sorted[0].number, 5)
        self.assertEqual(hand_sorted[1].color, 'white')
        self.assertEqual(hand_sorted[1].number, 5)
        self.assertEqual(hand_sorted[2].color, 'white')
        self.assertEqual(hand_sorted[2].number, 10)

    def test_print_card(self):
        c = Card('white', 5)
        self.assertEqual('W05', c.card_str())
        c = Card('black', 5)
        self.assertEqual('B05', c.card_str())
        c = Card('black', 11)
        self.assertEqual('B11', c.card_str())

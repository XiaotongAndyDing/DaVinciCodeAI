from unittest import TestCase

from GameModule.Card import Card


class TestCard(TestCase):

    def test_init(self):
        c = Card('white', 5)
        self.assertEquals(c.color, 'white')
        self.assertEquals(c.number, 5)
        self.assertEquals(c.published, False)
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
        self.assertEquals(c.published, False)
        c.guess_number(5)
        self.assertEquals(c.published, True)

        with self.assertRaises(Exception) as cm:
            c.guess_number(5)
        self.assertEqual(
            'it has been published',
            str(cm.exception)
        )

    def test_sorted(self):
        hand = [Card('white', 10), Card('black', 5), Card('white', 5)]
        hand_sorted = sorted(hand)
        self.assertEquals(hand_sorted[0].color, 'black')
        self.assertEquals(hand_sorted[0].number, 5)
        self.assertEquals(hand_sorted[1].color, 'white')
        self.assertEquals(hand_sorted[1].number, 5)
        self.assertEquals(hand_sorted[2].color, 'white')
        self.assertEquals(hand_sorted[2].number, 10)

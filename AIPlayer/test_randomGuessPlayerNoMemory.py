from unittest import TestCase

from GameModule.AIPlayer.RandomGuessPlayerNoMemoey import RandomGuessPlayerNoMemory
from GameModule.Card import Card


class TestRandomGuessPlayerNoMemory(TestCase):
    def test_guess_next(self):
        p = RandomGuessPlayerNoMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [None, Card('white', 11), None, None]]

        card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [])
        self.assertIn(card_index_guessed, [0, 1])
        self.assertIn(number_guessed, [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11])

        card_index_guessed, number_guessed = p.guess_next(2, public_view_list, [])
        self.assertIn(card_index_guessed, [0, 2, 3])
        self.assertIn(number_guessed, [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11])

    def test_guess_all(self):
        p = RandomGuessPlayerNoMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [Card('white', 1), Card('white', 11)]]

        player_index, card_index_guessed, number_guessed = p.guess_all(public_view_list, [])

        self.assertEqual(player_index, 1)
        self.assertIn(card_index_guessed, [0, 1])
        self.assertIn(number_guessed, [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11])

    def test_guess_history(self):
        p = RandomGuessPlayerNoMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [None, Card('white', 11), None, None]]

        card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [])
        self.assertIn(number_guessed, p.guess_other_history)
        card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [])
        self.assertIn(number_guessed, p.guess_other_history)
        card_index_guessed, number_guessed = p.guess_next(0, public_view_list, [])
        self.assertIn(number_guessed, p.guess_other_history)
        card_index_guessed, number_guessed = p.guess_next(0, public_view_list, [])
        self.assertIn(number_guessed, p.guess_other_history)

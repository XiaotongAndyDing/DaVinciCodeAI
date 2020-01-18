from unittest import TestCase

from GameModule.AIPlayer.GreedyPlayerAdvancedLogicMemory import GreedyPlayerAdvancedLogicMemory
from GameModule.Card import Card


class TestGreedyPlayerAdvancedLogicMemory(TestCase):
    def test_guess_next_implementation(self):
        p = GreedyPlayerAdvancedLogicMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [None, None, None]]
        public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3, 4}, None], [{1, 2, 3}, set(), set()]]

        for _ in range(20):
            card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [[], public_card_guess_history])
            self.assertEqual(card_index_guessed, 1)  # index 1 has 2*2 candidates while index 0 has 3*2 candidates (046)
            self.assertIn(number_guessed, [0, 6])  # 5 has been in own hands, 1234 are in guess history

        public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3}, None], [{1, 2, 3}, set(), set()]]

        for _ in range(20):
            card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [[], public_card_guess_history])
            self.assertIn(card_index_guessed, [0, 1])
            self.assertIn(number_guessed, [0, 4, 6])

    def test_guess_all(self):
        p = GreedyPlayerAdvancedLogicMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))
        public_view_list = [[None, None, None], [None, None, Card('black', 7)],
                            [Card('white', 1), None, Card('white', 11)]]
        public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3, 4}, None],
                                     [None, set(), None]]
        for _ in range(20):
            player_index, card_index_guessed, number_guessed = p.guess_all(public_view_list,
                                                                           [[], public_card_guess_history])
            self.assertEqual(player_index, 1)
            self.assertEqual(card_index_guessed, 1)
            self.assertIn(number_guessed, [0, 6])

        public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3}, None],
                                     [None, set(), None]]
        for _ in range(20):
            player_index, card_index_guessed, number_guessed = p.guess_all(public_view_list,
                                                                           [[], public_card_guess_history])
            self.assertEqual(player_index, 1)
            self.assertIn(card_index_guessed, [0, 1])
            self.assertIn(number_guessed, [0, 4, 6])

        public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3}, None],
                                     [None, {2, 3, 4, 5, 6, 7, 8, 9, 11}, None]]
        for _ in range(20):
            player_index, card_index_guessed, number_guessed = p.guess_all(public_view_list,
                                                                           [[], public_card_guess_history])
            self.assertEqual(player_index, 2)
            self.assertEqual(card_index_guessed, 1)
            self.assertEqual(number_guessed, 10)

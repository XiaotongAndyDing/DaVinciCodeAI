from unittest import TestCase

from GameModule.AIPlayer.RandomGuessPlayerLogicMemory import RandomGuessPlayerLogicMemory
from GameModule.Card import Card


class TestRandomGuessPlayerLogicMemory(TestCase):
    def test_guess_next_memory_only(self):
        p = RandomGuessPlayerLogicMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [None, None, None]]
        public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3}, None], [{1, 2, 3}, set(), set()]]

        for _ in range(20):
            card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [[], public_card_guess_history])
            self.assertIn(card_index_guessed, [0, 1])
            self.assertIn(number_guessed, [0, 4, 6, 7, 8, 9, 10, 11])

    def test_guess_next_memory_and_logic(self):
        p = RandomGuessPlayerLogicMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        """has both lower limit and upper limit"""
        for _ in range(20):
            public_view_list = [[None, None, None], [Card('white', 0), None, Card('black', 7)], [None, None, None]]
            public_card_guess_history = [[set(), set(), set()], [None, {1, 2, 3}, None], [{1, 2, 3}, set(), set()]]
            card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [[], public_card_guess_history])
            self.assertEqual(card_index_guessed, 1)
            self.assertIn(number_guessed, [4, 6])

        """has only upper limit"""
        for _ in range(20):
            public_view_list = [[None, None, None], [None, None, Card('black', 7)], [None, None, None]]
            public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3}, None], [{1, 2, 3}, set(), set()]]
            card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [[], public_card_guess_history])
            self.assertIn(card_index_guessed, [0, 1])
            self.assertIn(number_guessed, [0, 4, 6])

        """has only lower limit"""
        for _ in range(20):
            public_view_list = [[None, None, None], [Card('white', 0), None, None], [None, None, None]]
            public_card_guess_history = [[set(), set(), set()], [None, {1, 2, 3}, {1, 2, 3}], [{1, 2, 3}, set(), set()]]
            card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [[], public_card_guess_history])
            self.assertIn(card_index_guessed, [1, 2])
            self.assertIn(number_guessed, [4, 6, 7, 8, 9, 10, 11])

        """has no limits"""
        for _ in range(20):
            public_view_list = [[None, None, None], [None, None, None], [None, None, None]]
            public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3}, {1, 2, 3}],
                                         [{1, 2, 3}, set(), set()]]
            card_index_guessed, number_guessed = p.guess_next(1, public_view_list, [[], public_card_guess_history])
            self.assertIn(card_index_guessed, [0, 1, 2])
            self.assertIn(number_guessed, [0, 4, 6, 7, 8, 9, 10, 11])

    def test_guess_all(self):
        p = RandomGuessPlayerLogicMemory(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))
        for _ in range(20):
            public_view_list = [[None, None, None], [None, None, Card('black', 7)],
                                [Card('white', 1), Card('white', 11)]]
            public_card_guess_history = [[set(), set(), set()], [{1, 2, 3}, {1, 2, 3}, None],
                                         [None, None]]

            player_index, card_index_guessed, number_guessed = p.guess_all(public_view_list,
                                                                           [[], public_card_guess_history])

            self.assertEqual(player_index, 1)
            self.assertIn(card_index_guessed, [0, 1])
            self.assertIn(number_guessed, [0, 4, 6])

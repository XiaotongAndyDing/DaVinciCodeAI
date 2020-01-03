from unittest import TestCase

from GameModule.AIPlayer.Player import Player
from GameModule.Card import Card


class TestPlayer(TestCase):

    def test_add_card(self):
        p = Player()
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        self.assertEqual(p.num_of_card, 3)

        self.assertEqual(p._card_list[0].color, 'black')
        self.assertEqual(p._card_list[0].number, 5)
        self.assertEqual(p._card_list[1].color, 'white')
        self.assertEqual(p._card_list[1].number, 5)
        self.assertEqual(p._card_list[2].color, 'white')
        self.assertEqual(p._card_list[2].number, 10)

    def test_is_guessed(self):
        p = Player()
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        self.assertFalse(p.is_guessed(0, 3))
        self.assertFalse(p._card_list[0].published)
        self.assertTrue(p.is_guessed(0, 5))
        self.assertTrue(p._card_list[0].published)

        with self.assertRaises(IndexError):
            p.is_guessed(4, 3)

    def test_public_view(self):
        p = Player()
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        v = p.public_view()
        self.assertEqual(v[0], None)
        self.assertEqual(v[1], None)
        self.assertEqual(v[2], None)

        self.assertFalse(p.is_guessed(0, 3))
        v = p.public_view()
        self.assertEqual(v[0], None)
        self.assertTrue(p.is_guessed(0, 5))
        v = p.public_view()
        self.assertEqual(v[0], Card('black', 5))

    def test_public_card_guessed_history(self):
        p = Player()
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        self.assertFalse(p.is_guessed(0, 3))
        v = p.public_card_guessed_history()
        self.assertIn(3, v[0])
        self.assertFalse(p.is_guessed(0, 4))
        v = p.public_card_guessed_history()
        self.assertIn(3, v[0])
        self.assertIn(4, v[0])
        self.assertTrue(p.is_guessed(0, 5))
        v = p.public_card_guessed_history()
        self.assertIsNone(v[0])

    def test_card_pool(self):
        p = Player(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [None, Card('white', 11), None, None]]

        private_card_pool = p._card_pool(public_view_list)
        self.assertEqual(len(private_card_pool), 12 * 2 - 5)

    def test_other_player_available_position_to_be_guessed(self):
        p = Player(0)

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [None, Card('white', 11), None, None]]

        available_position_list = p._other_player_available_position_to_be_guessed(0, public_view_list)
        self.assertListEqual(available_position_list, [0, 1, 2])

        available_position_list = p._other_player_available_position_to_be_guessed(1, public_view_list)
        self.assertListEqual(available_position_list, [0, 1])

        available_position_list = p._other_player_available_position_to_be_guessed(2, public_view_list)
        self.assertListEqual(available_position_list, [0, 2, 3])

    def test_available_player_name_to_be_guessed(self):
        p = Player(0)
        p.add_card(Card('white', 10))
        p.add_card(Card('black', 5))
        p.add_card(Card('white', 5))

        public_view_list = [[None, None, None], [None, None, Card('black', 7)], [Card('white', 1), Card('white', 11)]]

        available_list = p._available_player_name_to_be_guessed(public_view_list)

        self.assertListEqual(available_list, [1])
        """0 cannot be choose, because it is self. 2 cannot be chosen because all cards have been published"""

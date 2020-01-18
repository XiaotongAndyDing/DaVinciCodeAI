import unittest
from unittest import TestCase

from GameModule.AIPlayer.RandomGuessPlayerLogicMemory import RandomGuessPlayerLogicMemory
from GameModule.AIPlayer.RandomGuessPlayerNoMemoey import RandomGuessPlayerNoMemory
from GameModule.Game import Game


class TestGame(TestCase):

    def test_init(self):
        g = Game([RandomGuessPlayerNoMemory(i) for i in range(4)])  # four players, named

        self.assertEqual(len(g.card_pool), 12 * 2 - 4 * 3)
        """from 0 to 11 totally 22 cards, three players with each one 3 cards"""

        self.assertEqual(g.player_list[0].num_of_card, 3)

    def test_run(self):

        for _ in range(100):
            g = Game([RandomGuessPlayerNoMemory(i) for i in range(4)])
            turn, winner_name = g.run()

        for _ in range(100):
            g = Game([RandomGuessPlayerNoMemory(i) for i in range(5)])
            turn, winner_name = g.run()

        for _ in range(100):
            g = Game([RandomGuessPlayerNoMemory(i) for i in range(3)])
            turn, winner_name = g.run()

        """4 players 1000 games about 5 s"""

    @unittest.skip("has been tested in Battle.py")
    def test_run_two_kinds_players(self):
        result = {0: 0, 1: 0, 2: 0, 3: 0}
        is_guessed_count = {0: 0, 1: 0, 2: 0, 3: 0}
        is_guessed_right = {0: 0, 1: 0, 2: 0, 3: 0}
        guess_other_count = {0: 0, 1: 0, 2: 0, 3: 0}
        guess_right_count = {0: 0, 1: 0, 2: 0, 3: 0}

        num_of_game = 1000

        for _ in range(num_of_game):
            g = Game([RandomGuessPlayerNoMemory(0), RandomGuessPlayerNoMemory(1), RandomGuessPlayerLogicMemory(2),
                      RandomGuessPlayerLogicMemory(3)])
            turn, winner_name = g.run()
            result[winner_name] += 1
            for i in range(4):
                is_guessed_count[i] += g.player_list[i].is_guessed_count
                is_guessed_right[i] += g.player_list[i].is_guessed_right
                guess_other_count[i] += g.player_list[i].guess_other_count
                guess_right_count[i] += g.player_list[i].guess_right_count

        round_digit = 3

        print('Player\t\t', 'win rate\t\t', 'defence(is_guessed)\t\t', 'offence(guess_other)\t\t')
        print('Player 1 Golden Fish 1:\t\t', round(result[0] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[0] / is_guessed_count[0], round_digit), '\t\t',
              round(guess_right_count[0] / guess_other_count[0], round_digit))
        print('Player 2 Golden Fish 2:\t\t', round(result[1] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[1] / is_guessed_count[1], round_digit), '\t\t',
              round(guess_right_count[1] / guess_other_count[1], round_digit))
        print('Player 3 Smart Parrot 3:\t\t', round(result[2] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[2] / is_guessed_count[2], round_digit), '\t\t',
              round(guess_right_count[2] / guess_other_count[2], round_digit))
        print('Player 4 Smart Parrot 4:\t\t', round(result[3] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[3] / is_guessed_count[3], round_digit), '\t\t',
              round(guess_right_count[3] / guess_other_count[3], round_digit))

    @unittest.skip("has been tested in Battle.py")
    def test_how_order_influence_win_rates(self):
        result = {0: 0, 1: 0, 2: 0, 3: 0}
        is_guessed_count = {0: 0, 1: 0, 2: 0, 3: 0}
        is_guessed_right = {0: 0, 1: 0, 2: 0, 3: 0}
        guess_other_count = {0: 0, 1: 0, 2: 0, 3: 0}
        guess_right_count = {0: 0, 1: 0, 2: 0, 3: 0}

        num_of_game = 1000

        for _ in range(num_of_game):
            g = Game([RandomGuessPlayerLogicMemory(0), RandomGuessPlayerLogicMemory(1), RandomGuessPlayerLogicMemory(2),
                      RandomGuessPlayerLogicMemory(3)])
            turn, winner_name = g.run()
            result[winner_name] += 1
            for i in range(4):
                is_guessed_count[i] += g.player_list[i].is_guessed_count
                is_guessed_right[i] += g.player_list[i].is_guessed_right
                guess_other_count[i] += g.player_list[i].guess_other_count
                guess_right_count[i] += g.player_list[i].guess_right_count

        round_digit = 3

        print('Player\t\t', 'win rate\t\t', 'defence(is_guessed)\t\t', 'offence(guess_other)\t\t')
        print('Player 1 Smart Parrot 1:\t\t', round(result[0] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[0] / is_guessed_count[0], round_digit), '\t\t',
              round(guess_right_count[0] / guess_other_count[0], round_digit))
        print('Player 2 Smart Parrot 2:\t\t', round(result[1] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[1] / is_guessed_count[1], round_digit), '\t\t',
              round(guess_right_count[1] / guess_other_count[1], round_digit))
        print('Player 3 Smart Parrot 3:\t\t', round(result[2] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[2] / is_guessed_count[2], round_digit), '\t\t',
              round(guess_right_count[2] / guess_other_count[2], round_digit))
        print('Player 4 Smart Parrot 4:\t\t', round(result[3] / num_of_game, round_digit), '\t\t',
              round(is_guessed_right[3] / is_guessed_count[3], round_digit), '\t\t',
              round(guess_right_count[3] / guess_other_count[3], round_digit))

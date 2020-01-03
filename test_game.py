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
            g = Game([RandomGuessPlayerNoMemory(i) for i in range(5)])
            turn, winner_name = g.run()

        for _ in range(100):
            g = Game([RandomGuessPlayerNoMemory(i) for i in range(3)])
            turn, winner_name = g.run()

        for _ in range(100):
            g = Game([RandomGuessPlayerNoMemory(i) for i in range(4)])
            turn, winner_name = g.run()

        """4 players 1000 games about 5 s"""

    def test_run_two_kinds_players(self):
        result = {0: 0, 1: 0, 2: 0, 3: 0}
        for _ in range(100):
            g = Game([RandomGuessPlayerNoMemory(0), RandomGuessPlayerNoMemory(1), RandomGuessPlayerLogicMemory(2),
                      RandomGuessPlayerLogicMemory(3)])
            turn, winner_name = g.run()
            result[winner_name] += 1
        print(result)
        print('win rate', (result[2]+result[3]) / 10000)
        """10000 tests about 40s, LogicMemory win rate 62% compared with RandomGuesser"""

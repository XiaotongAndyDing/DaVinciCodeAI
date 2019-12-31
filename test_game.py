from unittest import TestCase

from GameModule.Game import Game


class TestGame(TestCase):

    def test_init(self):
        g = Game(4)  # four players

        self.assertEquals(len(g.card_pool), 12 * 2 - 4 * 3)
        """from 0 to 11 totally 22 cards, three players with each one 3 cards"""

        self.assertEquals(g.player_list[0].num_of_card, 3)

    def test_run(self):
        g = Game(4)
        turn, winner_name = g.run()


        end = 1

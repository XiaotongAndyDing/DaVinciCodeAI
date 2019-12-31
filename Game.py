import random
from GameModule.Card import Card
from GameModule.Player import Player


class GuessHistory:

    def __init__(self, player_index, number_guessed):
        self.player_index = player_index
        self.number_guessed = number_guessed


class Game:
    NUM_CARDS_INITIAL = 3
    MAX_CARDS_HOLDING = 6
    MAX_TURN = 100

    def __init__(self, num_of_player=4):
        self.num_of_player = num_of_player
        self.player_list = [Player(i) for i in range(num_of_player)]
        self.card_pool = [Card('black', i) for i in range(0, 12)] + [Card('white', i) for i in range(0, 12)]
        random.shuffle(self.card_pool)
        self.guess_history = []
        self.public_view_list = []

        for player in self.player_list:
            for _ in range(Game.NUM_CARDS_INITIAL):
                player.add_card(self.card_pool.pop())

        self._update_public_view()

    def run(self):

        for turn in range(Game.MAX_TURN):

            for player_index, player in enumerate(self.player_list):

                if len(list(filter(lambda x: x.all_card_published, self.player_list))) == self.num_of_player - 1:
                    winner_name = self._end_game()
                    return turn, winner_name

                if not player.all_card_published:  # not all card published
                    if not self._next_player(player).all_card_published:
                        card_index, number = player.guess_next(self._next_player_id(player), self.public_view_list,
                                                               self.guess_history)
                        if not self._next_player(player).is_guessed(card_index, number):
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                new_card = self.card_pool.pop()
                                new_card.published = True
                                player.add_card(new_card)
                        else:
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                new_card = self.card_pool.pop()
                                player.add_card(new_card)
                    else:
                        player_index, card_index, number = player.guess_all(self.public_view_list, self.guess_history)
                        if not self.player_list[player_index].is_guessed(card_index, number):
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                new_card = self.card_pool.pop()
                                new_card.published = True
                                player.add_card(new_card)
                        else:
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                new_card = self.card_pool.pop()
                                player.add_card(new_card)
                    self._update_public_view()

        raise Exception('Turns more than max')

    def _next_player_id(self, player):
        if player.name + 1 == self.num_of_player:
            return 0
        else:
            return player.name + 1

    def _next_player(self, player):
        if player.name + 1 == self.num_of_player:
            return self.player_list[0]
        else:
            return self.player_list[player.name + 1]

    def _end_game(self):
        return [i for i in self.player_list if not i.all_card_published][0].name

    def _update_public_view(self):
        self.public_view_list = [player.public_view() for player in self.player_list]

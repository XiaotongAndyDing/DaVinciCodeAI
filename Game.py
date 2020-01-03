import random
from GameModule.Card import Card


class GuessHistory:

    def __init__(self, guessing_player_index, guessed_player_index, number_guessed):
        self.guessing_player_index = guessing_player_index
        self.guessed_player_index = guessed_player_index
        self.number_guessed = number_guessed


class Game:
    NUM_CARDS_INITIAL = 3
    MAX_CARDS_HOLDING = 6
    MAX_TURN = 100

    def __init__(self, player_list):
        self.num_of_player = len(player_list)
        self.player_list = player_list
        self.card_pool = [Card('black', i) for i in range(0, 12)] + [Card('white', i) for i in range(0, 12)]
        random.shuffle(self.card_pool)
        self.public_view_list = []
        self.each_player_guess_history = []
        self.public_card_guess_history = []

        for player in self.player_list:
            for _ in range(Game.NUM_CARDS_INITIAL):
                card = self.card_pool.pop()
                card.original_card = True
                player.add_card(card)

        self._update_public_view()

    def run(self):

        for turn in range(Game.MAX_TURN):

            for player_index, player in enumerate(self.player_list):

                if self._check_game_finish():
                    winner_name = self._end_game()
                    return turn, winner_name

                if not player.all_card_published:  # not all card published
                    if not self._next_player(player).all_card_published:
                        card_index, number = player.guess_next(self._next_player_id(player), self.public_view_list,
                                                               [self.each_player_guess_history,
                                                                self.public_card_guess_history])

                        if not self._next_player(player).is_guessed(card_index, number):
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                new_card = self.card_pool.pop()
                                new_card.published = True
                                player.add_card(new_card)
                        else:
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                player.add_card(self.card_pool.pop())
                    else:
                        player_index_guess, card_index, number = player.guess_all(self.public_view_list,
                                                                                  [self.each_player_guess_history,
                                                                                   self.public_card_guess_history])
                        if not self.player_list[player_index_guess].is_guessed(card_index, number):
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                new_card = self.card_pool.pop()
                                new_card.published = True
                                player.add_card(new_card)
                        else:
                            if self.card_pool and player.num_of_card < Game.MAX_CARDS_HOLDING:
                                player.add_card(self.card_pool.pop())
                    self._update_public_view()
                    self._update_each_player_guess_history()
                    self._update_public_card_guess_history()

        raise Exception('Max Turns')

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

    def _update_each_player_guess_history(self):
        self.each_player_guess_history = [player.guess_other_history for player in self.player_list]

    def _update_public_card_guess_history(self):
        self.public_card_guess_history = [player.public_card_guessed_history() for player in self.player_list]

    def _check_game_finish(self):
        return len(list(filter(lambda x: x.all_card_published, self.player_list))) == self.num_of_player - 1

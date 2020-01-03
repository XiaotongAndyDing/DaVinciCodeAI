import random

from GameModule.AIPlayer.Player import Player


class RandomGuessPlayerNoMemory(Player):
    def guess_next(self, next_player_id, public_view_list, guess_history):
        card_index_guessed = random.choice(
            self._other_player_available_position_to_be_guessed(next_player_id, public_view_list))
        number_guessed = random.choice(self._card_pool(public_view_list)).number
        self.guess_other_history.add(number_guessed)

        return card_index_guessed, number_guessed

    def guess_all(self, public_view_list, guess_history):
        player_index = random.choice(self._available_player_name_to_be_guessed(public_view_list))
        card_index_guessed, number_guessed = self.guess_next(player_index, public_view_list, guess_history)
        self.guess_other_history.add(number_guessed)

        return player_index, card_index_guessed, number_guessed

import random

from GameModule.AIPlayer.Player import Player


class RandomGuessPlayerNoMemory(Player):
    def guess_next_implementation(self, next_player_id, public_view_list, guess_history):
        card_index_guessed = random.choice(
            self._other_player_available_position_to_be_guessed(next_player_id, public_view_list))
        number_guessed = random.choice(self._card_pool(public_view_list)).number

        return card_index_guessed, number_guessed

    def guess_all_implementation(self, public_view_list, guess_history):
        player_index = random.choice(self._available_player_name_to_be_guessed(public_view_list))
        card_index_guessed, number_guessed = self.guess_next(player_index, public_view_list, guess_history)

        return player_index, card_index_guessed, number_guessed

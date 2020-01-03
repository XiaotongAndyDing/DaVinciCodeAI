import random

from GameModule.AIPlayer.Player import Player


class RandomGuessPlayerLogicMemory(Player):
    def guess_next(self, next_player_id, public_view_list, guess_history):
        each_player_guess_history = guess_history[0]
        public_card_guess_history = guess_history[1]
        card_index_guessed = random.choice(
            self._other_player_available_position_to_be_guessed(next_player_id, public_view_list))
        card_candidate = [card for card in self._card_pool(public_view_list) if
                          card.number not in
                          public_card_guess_history[next_player_id][card_index_guessed]]

        if [i for i in public_view_list[next_player_id][:card_index_guessed] if i is not None]:
            lower_limit = [i for i in public_view_list[next_player_id][:card_index_guessed] if i is not None][-1]
            card_candidate = [card for card in card_candidate if lower_limit < card]

        if [i for i in public_view_list[next_player_id][card_index_guessed:] if i is not None]:
            upper_limit = [i for i in public_view_list[next_player_id][card_index_guessed:] if i is not None][0]
            card_candidate = [card for card in card_candidate if card < upper_limit]

        number_guessed = random.choice(card_candidate).number

        self.guess_other_history.add(number_guessed)

        return card_index_guessed, number_guessed

    def guess_all(self, public_view_list, guess_history):
        player_index = random.choice(self._available_player_name_to_be_guessed(public_view_list))
        card_index_guessed, number_guessed = self.guess_next(player_index, public_view_list, guess_history)
        self.guess_other_history.add(number_guessed)

        return player_index, card_index_guessed, number_guessed

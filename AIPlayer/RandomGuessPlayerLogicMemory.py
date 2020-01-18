import random

from GameModule.AIPlayer.Player import Player


class RandomGuessPlayerLogicMemory(Player):
    """
    Parrot

    it has basic memory and logic, memory means if a card is guessed wrong on 1, she would not guesses again
    the card is 1 again. Logic means it only consider public view and holding card, if two One cards are published
    she would not guess 1 again. If one 1 is published and she holds 1, (no more 1), she would not guess 1. Also,
    if she want to guess [?, 2], she knows ? is smaller than 2, and would not guess 3.

    She would first uniformly randomly pick an agent can be guessed, then randomly pick an index to guess, then randomly
    choose card from available candidate cards.

    """

    def guess_next_implementation(self, next_player_id, public_view_list, guess_history):
        each_player_guess_history = guess_history[0]
        public_card_guess_history = guess_history[1]
        card_index_guessed = random.choice(
            self._other_player_available_position_to_be_guessed(next_player_id, public_view_list))
        try:
            card_candidate = [card for card in self._card_pool(public_view_list) if
                              card.number not in
                              public_card_guess_history[next_player_id][card_index_guessed]]
        except IndexError:
            card_candidate = [card for card in self._card_pool(public_view_list)]

        if [i for i in public_view_list[next_player_id][:card_index_guessed] if i is not None]:
            lower_limit = [i for i in public_view_list[next_player_id][:card_index_guessed] if i is not None][-1]
            card_candidate = [card for card in card_candidate if lower_limit < card]

        if [i for i in public_view_list[next_player_id][card_index_guessed:] if i is not None]:
            upper_limit = [i for i in public_view_list[next_player_id][card_index_guessed:] if i is not None][0]
            card_candidate = [card for card in card_candidate if card < upper_limit]

        number_guessed = random.choice(card_candidate).number

        return card_index_guessed, number_guessed

    def guess_all_implementation(self, public_view_list, guess_history):
        player_index = random.choice(self._available_player_name_to_be_guessed(public_view_list))
        card_index_guessed, number_guessed = self.guess_next(player_index, public_view_list, guess_history)

        return player_index, card_index_guessed, number_guessed

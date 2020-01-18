import random

from GameModule.AIPlayer.Player import Player


class GreedyPlayerAdvancedLogicMemory(Player):
    """
    Greedy Shylock

    it is very greedy. it would evaluate all agents, all index and all card candidates (using logic and memory to
    remove all wrong answers), with prior that each cards are distributed uniformly.

    Basic logic means  f she want to guess [?, 2], she knows ? is smaller than 2, and would not guess 3. Advanced Logic
    means in [?, x, x] she would not guess 11, because she knows it should be 2 more cards greater than ?. So the
    Maximum of ? is 10.

    She has some basic memory. If someone guesses agent 1 card 1 is 1, which was wrong. She would not make the same
    mistake. But she cannot extract more information from other people's guessing. In other words, she does not how to
     use other agents guessing result more efficiently. Bayesian will focus on it.

    """

    def guess_next_implementation(self, next_player_id, public_view_list, guess_history):

        guessed_index, number_guessed, probability_correct = self.guess_next_implementation_with_probability(
            next_player_id, public_view_list, guess_history)

        return guessed_index, number_guessed

    def guess_next_implementation_with_probability(self, next_player_id, public_view_list, guess_history):
        """we also provides our estimation of guessing correct probability if we guess his player"""
        each_player_guess_history = guess_history[0]
        public_card_guess_history = guess_history[1]
        available_card_index = self._other_player_available_position_to_be_guessed(next_player_id, public_view_list)
        each_index_how_many_candidate = {}

        def find_candidates_given_index(index):
            try:
                card_candidate = [card for card in self._card_pool(public_view_list) if
                                  card.number not in
                                  public_card_guess_history[next_player_id][index]]
            except IndexError:
                card_candidate = [card for card in self._card_pool(public_view_list)]

            if [i for i in public_view_list[next_player_id][:index] if i is not None]:
                lower_limit = [i for i in public_view_list[next_player_id][:index] if i is not None][-1]
                card_candidate = [card for card in card_candidate if lower_limit < card]

            if [i for i in public_view_list[next_player_id][index:] if i is not None]:
                upper_limit = [i for i in public_view_list[next_player_id][index:] if i is not None][0]
                card_candidate = [card for card in card_candidate if card < upper_limit]
            return card_candidate

        for card_index in available_card_index:
            each_index_how_many_candidate[card_index] = len(find_candidates_given_index(card_index))

        guessed_index = random.choice([i for i in each_index_how_many_candidate.keys() if
                                       each_index_how_many_candidate[i] == min(each_index_how_many_candidate.values())])

        number_guessed = random.choice(find_candidates_given_index(guessed_index)).number

        probability_correct = 1 / each_index_how_many_candidate[guessed_index]

        return guessed_index, number_guessed, probability_correct

    def guess_all_implementation(self, public_view_list, guess_history):
        player_index_list = self._available_player_name_to_be_guessed(public_view_list)
        guess_each_player_result = []
        for player in player_index_list:
            guessed_index, number_guessed, probability_correct = \
                self.guess_next_implementation_with_probability(player, public_view_list, guess_history)
            guess_each_player_result.append((player, guessed_index, number_guessed, probability_correct))
        highest_prob = max([i[3] for i in guess_each_player_result])
        player_index_number_guessed = random.choice([i for i in guess_each_player_result if i[3] == highest_prob])
        player_index, guessed_index, number_guessed = \
            player_index_number_guessed[0], player_index_number_guessed[1], player_index_number_guessed[2]

        return player_index, guessed_index, number_guessed

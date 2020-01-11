from GameModule.Card import Card


class Player:

    def __init__(self, name=0, print_screen=False):
        self.name = name
        self._card_list = []
        self.num_of_card = 0
        self.all_card_published = False
        self.guess_other_history = set()
        self.print_screen = print_screen
        self.is_guessed_count = 0
        self.is_guessed_right = 0
        self.guess_other_count = 0
        self.guess_right_count = 0

    def _sort_cards(self):
        self._card_list = sorted(self._card_list)

    def add_card(self, card):
        self.num_of_card += 1
        self._card_list.append(card)
        self._sort_cards()

    def is_guessed(self, index, number):
        self.is_guessed_count += 1
        if self._card_list[index].guess_number(number):
            self.is_guessed_right += 1
            if self.print_screen:
                print('this guess is CORRECT!')
            if len([card for card in self._card_list if card.published]) == self.num_of_card:
                self.all_card_published = True
            return True
        else:
            if self.print_screen:
                print('this guess is WRONG')
            return False

    def guess_next(self, next_player_id, public_view_list, guess_history):
        """other methods are supporting methods while the main difference are these two guess methods"""
        card_index_guessed, number_guessed = self.guess_next_implementation(next_player_id, public_view_list,
                                                                            guess_history)
        self.guess_other_history.add(number_guessed)
        if self.print_screen:
            print('Player ' + str(self.name) + ' guesses next player card ' + str(card_index_guessed) + ' is ' + str(
                number_guessed))
        self.guess_other_count += 1
        return card_index_guessed, number_guessed

    def guess_next_implementation(self, next_player_id, public_view_list, guess_history):
        return 0, 0

    def guess_all(self, public_view_list, guess_history):
        player_index, card_index_guessed, number_guessed = self.guess_all_implementation(public_view_list,
                                                                                         guess_history)
        self.guess_other_history.add(number_guessed)
        if self.print_screen:
            print('Player ' + str(self.name) + ' guesses Player ' + str(player_index) + ' card ' + str(
                card_index_guessed) + ' is ' + str(
                number_guessed))
        self.guess_other_count += 1
        return player_index, card_index_guessed, number_guessed

    def guess_all_implementation(self, public_view_list, guess_history):
        return 0, 0, 0

    def public_view(self):
        return [i if i.published else None for i in self._card_list]

    def public_card_guessed_history(self):
        return [None if i.published else i.wrong_guess_history for i in self._card_list]

    def _card_pool(self, public_view_list):
        private_view_list = public_view_list.copy()
        private_view_list[self.name] = self._card_list
        card_pool = [Card('black', i) for i in range(0, 12)] + [Card('white', i) for i in range(0, 12)]
        card_pool = set(card_pool)
        for player in private_view_list:
            card_pool -= set(player)
        return sorted(list(card_pool))

    @staticmethod
    def _other_player_available_position_to_be_guessed(player_id, public_view_list):
        return [i for i in range(len(public_view_list[player_id])) if public_view_list[player_id][i] is None]

    def _available_player_name_to_be_guessed(self, public_view_list):
        return [i for i in range(len(public_view_list)) if
                i != self.name and len(self._other_player_available_position_to_be_guessed(i, public_view_list)) != 0]

    def print_public_view_of_the_player(self):
        return 'Player ' + str(self.name) + ': ' + ', '.join(
            [i.card_str() if i.published else '???' for i in self._card_list])

    @property
    def is_guessed_right_rate(self):
        """as a defence measure"""
        return 0 if self.is_guessed_count == 0 else self.is_guessed_right / self.is_guessed_count

    def guess_other_right(self):
        """as an offence measure"""
        self.guess_right_count += 1

    @property
    def guess_other_right_rate(self):
        """as a defence measure"""
        return 0 if self.guess_other_count == 0 else self.guess_right_count / self.guess_other_count

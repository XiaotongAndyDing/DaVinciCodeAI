import random
from GameModule.Card import Card


class Player:

    def __init__(self, name=0):
        self.name = name
        self._card_list = []
        self.num_of_card = 0
        self.all_card_published = False

    def _sort_cards(self):
        self._card_list = sorted(self._card_list)

    def add_card(self, card):
        self.num_of_card += 1
        self._card_list.append(card)
        self._sort_cards()

    def is_guessed(self, index, number):
        if self._card_list[index].guess_number(number):
            if len([card for card in self._card_list if card.published]) == self.num_of_card:
                self.all_card_published = True
            return True
        else:
            return False

    def guess_next(self, next_player_id, public_view_list, guess_history):
        card_index_guessed = random.choice(
            self._other_player_available_position_to_be_guessed(next_player_id, public_view_list))
        number_guessed = random.choice(self._card_pool(public_view_list)).number

        return card_index_guessed, number_guessed

    def guess_all(self, public_view_list, guess_history):
        player_index = random.choice(self._available_player_name_to_be_guessed(public_view_list))
        card_index_guessed, number_guessed = self.guess_next(player_index, public_view_list, guess_history)

        return player_index, card_index_guessed, number_guessed

    def public_view(self):
        return [i if i.published else None for i in self._card_list]

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

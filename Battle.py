"""to compare two agents in different aspects, the default setting is 4 players game, 2v2, but can be customized"""
import time

from GameModule.AIPlayer.GreedyPlayerAdvancedLogicMemory import GreedyPlayerAdvancedLogicMemory
from GameModule.AIPlayer.RandomGuessPlayerLogicMemory import RandomGuessPlayerLogicMemory
from GameModule.AIPlayer.RandomGuessPlayerNoMemoey import RandomGuessPlayerNoMemory
from GameModule.Game import Game

start_time = time.time()
result = {'agent_1': 0, 'agent_2': 0}
is_guessed_count = {'agent_1': 0, 'agent_2': 0}
is_guessed_right = {'agent_1': 0, 'agent_2': 0}
guess_other_count = {'agent_1': 0, 'agent_2': 0}
guess_right_count = {'agent_1': 0, 'agent_2': 0}
game_turn = 0

num_of_game = 1000

agent_1 = RandomGuessPlayerLogicMemory
agent_1_name = 'Player 1 Smart Parrot'  # Parrot has good memory and logic

# agent_2 = RandomGuessPlayerNoMemory
# agent_2_name = 'Player 2 Golden Fish'  # Golden Fish has no memory nor logic

agent_2 = GreedyPlayerAdvancedLogicMemory
agent_2_name = 'Player 2 Greedy Shylock'  # Greedy Shylock use greedy prior probability with advanced logic and memory

"""to reduce the influence of ordering, we set two games with ordering [1, 2, 1, 2] and [2, 1, 2, 1]"""

for _ in range(int(num_of_game / 2)):
    g = Game([agent_1(0), agent_2(1), agent_1(2), agent_2(3)])
    turn, winner_name = g.run()
    result['agent_1' if winner_name in [0, 2] else 'agent_2'] += 1
    game_turn += turn
    for i in range(4):
        is_guessed_count['agent_1' if i in [0, 2] else 'agent_2'] += g.player_list[i].is_guessed_count
        is_guessed_right['agent_1' if i in [0, 2] else 'agent_2'] += g.player_list[i].is_guessed_right
        guess_other_count['agent_1' if i in [0, 2] else 'agent_2'] += g.player_list[i].guess_other_count
        guess_right_count['agent_1' if i in [0, 2] else 'agent_2'] += g.player_list[i].guess_right_count

for _ in range(num_of_game - int(num_of_game / 2)):
    g = Game([agent_2(0), agent_1(1), agent_2(2), agent_1(3)])
    turn, winner_name = g.run()
    result['agent_1' if winner_name in [1, 3] else 'agent_2'] += 1
    game_turn += turn
    for i in range(4):
        is_guessed_count['agent_1' if i in [1, 3] else 'agent_2'] += g.player_list[i].is_guessed_count
        is_guessed_right['agent_1' if i in [1, 3] else 'agent_2'] += g.player_list[i].is_guessed_right
        guess_other_count['agent_1' if i in [1, 3] else 'agent_2'] += g.player_list[i].guess_other_count
        guess_right_count['agent_1' if i in [1, 3] else 'agent_2'] += g.player_list[i].guess_right_count
round_digit = 3

print()
print('Battle between ' + agent_1_name + ' and ' + agent_2_name + '\n')
print('Based on ' + str(num_of_game) + ' games\n')
print('Player\t\t\t\t\t\t', 'win rate\t\t', 'defence(is_guessed)\t', 'offence(guess_other)\t')
print(agent_1_name + '\t\t', round(result['agent_1'] / num_of_game, round_digit), '\t\t\t',
      round(is_guessed_right['agent_1'] / is_guessed_count['agent_1'], round_digit), '\t\t\t\t\t',
      round(guess_right_count['agent_1'] / guess_other_count['agent_1'], round_digit))
print(agent_2_name + '\t\t', round(result['agent_2'] / num_of_game, round_digit), '\t\t\t',
      round(is_guessed_right['agent_2'] / is_guessed_count['agent_2'], round_digit), '\t\t\t\t\t',
      round(guess_right_count['agent_2'] / guess_other_count['agent_2'], round_digit))

print('\nAverage turns per game: ' + str(round(game_turn / num_of_game, round_digit)) + '\n')

print("--- running time %s seconds ---" % (time.time() - start_time))

end = None

while True:
    player_one_input = input('Player one:Choose rock, paper or scissors=>')
    player_two_input = input('Player two:Choose rock, paper or scissors=>')
    if player_one_input == player_two_input:
        print("It's a draw.")
    else:
        if (
            (player_one_input == 'rock' and player_two_input == 'scissors') or
            (player_one_input == 'paper' and player_two_input == 'rock') or
            (player_one_input == 'scissors' and player_two_input == 'paper')
        ):
            print('Player one wins!Congratulations!')
        else:
            print('Player two wins!Congratulations!')
    play_again = input('Play again?(y/n)=>')
    if play_again == 'n':
        break

#Solution with dictionaries:

# win_table = {
#     'rock': {
#         'rock': 'draw',
#         'paper': 'lose',
#         'scissors': 'win'
#     },
#     'paper': {
#         'rock': 'win',
#         'paper': 'draw',
#         'scissors': 'lose'
#     },
#     'scissors': {
#         'rock': 'lose',
#         'paper': 'win',
#         'scissor': 'draw'
#     }
# }

# result_to_message = {
#     'win': 'p1 wins',
#     'lose': 'p2 wins',
#     'draw': 'draw'
# }

# player_one_result = win_table[player_one_input][player_two_input]
# result_message = result_to_message[player_one_result]
# print(result_message)
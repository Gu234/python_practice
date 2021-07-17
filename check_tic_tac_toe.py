from collections import Counter

PLAYER_ONE = 1
PLAYER_TWO = 2
GAME_SIZE = 3
NO_WINNER = 0


def tic_tac_toe(game):
    for i in range(GAME_SIZE):
        yield game[i]
        yield list(zip(*game))[i]
    yield [game[0][0], game[1][1], game[2][2]]
    yield [game[0][2], game[1][1], game[2][0]]


def check_tic_tac_toe(game):
    for i in tic_tac_toe(game):
        c = Counter(i)
        if c[PLAYER_ONE] == GAME_SIZE:
            return PLAYER_ONE
        if c[PLAYER_TWO] == GAME_SIZE:
            return PLAYER_TWO
    return NO_WINNER


game = [[2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

result = check_tic_tac_toe(game)
print(result)

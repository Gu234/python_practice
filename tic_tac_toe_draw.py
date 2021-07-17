game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
PLAYER_ONE = 1
PLAYER_TWO = 2
EMPTY_TILE = 0

PROMPT_MSG = {
    0: 'Player one move, type coordinates x,y:',
    1: 'Player two move, type coordinates x,y:'
}


def make_move(player, game):
    while True:
        coords = input(PROMPT_MSG[player])
        coords = coords.split(',')
        coords = [int(coords[0]), int(coords[1])]
        if game[coords[0]][coords[1]] != EMPTY_TILE:
            print('Place already taken')
        else:
            game[coords[0]][coords[1]] = player
            break


while True:
    make_move(PLAYER_ONE, game)
    make_move(PLAYER_TWO, game)
    print(game)

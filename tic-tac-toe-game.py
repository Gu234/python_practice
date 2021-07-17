from collections import Counter
from itertools import chain, cycle

PLAYER_ONE = 1
PLAYER_TWO = 2
GAME_SIZE = 3
NO_WINNER = 0
EMPTY_TILE = 0

PROMPT_MSG = {
    PLAYER_ONE: 'Player one move, type coordinates x,y:',
    PLAYER_TWO: 'Player two move, type coordinates x,y:'
}

ENDGAME_MSG = {
    PLAYER_ONE: 'Player one wins! Congratulations!',
    PLAYER_TWO: 'Player two wins! Congratulations!'
}

game_state_to_symbol = {
    EMPTY_TILE: '   ',
    PLAYER_ONE: ' X ',
    PLAYER_TWO: ' O '
}


class TicTacToe():

    def __init__(self):
        self.game_state = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    def draw_horizontal(self):
        to_print = [' '] * (GAME_SIZE + 1)
        print('---'.join(to_print))

    def draw_vertical(self, row):
        to_print = [game_state_to_symbol[i] for i in row]
        print('|' + '|'.join(to_print) + '|')

    def draw(self):
        for row in self.game_state:
            self.draw_horizontal()
            self.draw_vertical(row)
        self.draw_horizontal()

    def make_a_move(self, player):
        while True:
            coords = input(PROMPT_MSG[player])
            coords = coords.split(',')
            coords = [int(coords[0]), int(coords[1])]
            if self.game_state[coords[0]][coords[1]] != EMPTY_TILE:
                print('Place already taken')
            else:
                self.game_state[coords[0]][coords[1]] = player
                break

    def check_if_board_is_full(self):
        return EMPTY_TILE not in chain(*self.game_state)

    def iterate_win_conditions(self):
        for i in range(GAME_SIZE):
            yield self.game_state[i]
            yield list(zip(*self.game_state))[i]
        yield [self.game_state[0][0], self.game_state[1][1], self.game_state[2][2]]
        yield [self.game_state[0][2], self.game_state[1][1], self.game_state[2][0]]

    def check_tic_tac_toe(self):
        for i in self.iterate_win_conditions():
            c = Counter(i)
            if c[PLAYER_ONE] == GAME_SIZE:
                return PLAYER_ONE
            if c[PLAYER_TWO] == GAME_SIZE:
                return PLAYER_TWO
        return NO_WINNER

    def play(self):
        self.draw()
        for player in cycle([PLAYER_ONE, PLAYER_TWO]):
            if self.check_if_board_is_full():
                print("It's a draw!")
                break
            self.make_a_move(player)
            self.draw()
            if self.check_tic_tac_toe() == player:
                print(ENDGAME_MSG[player])
                break


if __name__ == '__main__':
    tic = TicTacToe()
    tic.play()

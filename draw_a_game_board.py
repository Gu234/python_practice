class Board():

    def __init__(self, size):
        self.size = size

    def draw_horizontal(self):
        to_print = [' '] * (self.size + 1)
        print('---'.join(to_print))

    def draw_vertical(self):
        to_print = ['|'] * (self.size + 1)
        print('   '.join(to_print))

    def draw(self):
        for _ in range(self.size):
            self.draw_horizontal()
            self.draw_vertical()
        self.draw_horizontal()


if __name__ == '__main__':
    user_input = input('Enter a board size:')
    size = int(user_input)
    board = Board(size)
    board.draw()

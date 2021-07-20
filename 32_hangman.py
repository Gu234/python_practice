from random import choice

class Hangman:
    NUMBER_OF_TRIES = 6

    def __init__(self) -> None:
        self.target_word = self.initialize_word()
        self.clue_word = ['-'] * len(self.target_word)
        self.letters_tried = set()
        self.incorrect_answers = 0
        self.input_letter = None

    def initialize_word(self):
        with open('sowpods.txt') as file:
            words = file.read().splitlines()
        return choice(words)

    def get_letter(self):
        while True:
            player_input = input('Guess your letter: ')
            input_letter = player_input.upper()
            if input_letter in self.letters_tried:
                print('You tried this letter already.')
            else:
                self.input_letter = input_letter
                self.letters_tried.add(self.input_letter)
                break

    def update_clue_word(self):
        for index, letter in enumerate(self.target_word):
            if letter == self.input_letter:
                self.clue_word[index] = letter

    def check_win_condition(self):
        return '-' not in self.clue_word

    def check_loose_condition(self):
        return self.incorrect_answers >= Hangman.NUMBER_OF_TRIES

    def play(self):
        while True:
            self.get_letter()
            self.update_clue_word()

            if self.check_win_condition():
                print('Congratulations! You win!')
                break

            if self.input_letter in self.target_word:
                print('Correct!')
            else:
                self.incorrect_answers += 1
                if self.check_loose_condition():
                    print('You loose!')
                    print(f'Word to guess was {self.target_word}')
                    break
                print('Incorrect!')
                print(f'You have {Hangman.NUMBER_OF_TRIES - self.incorrect_answers} chances left.')
            
            print(''.join(self.clue_word))

if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()

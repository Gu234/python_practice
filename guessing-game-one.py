from random import randint
num = randint(1, 9)
guesses = 0
while True:
    user_input = input(
        'Enter a number between 1 and 9 or exit to end the game=>')
    if user_input == 'exit':
        print(f'You guessed {guesses} times')
        break
    guesses += 1
    if int(user_input) > num:
        print('You guessed too high')
    elif int(user_input) < num:
        print('You guessed too low')
    else:
        print('You guessed right! Congratulations!')
        print(f'You guessed {guesses} times')
        break

max_number_to_guess = 101
min_number_to_guess = 0
guess_counter = 0
print('Think of a number between 0 and 100, I will try to guess it!')
while True:
    guess = (min_number_to_guess + max_number_to_guess) // 2
    print(f'Your number is {guess}')
    guess_counter += 1
    user_input = input('too (h)igh/too (l)ow/(c)orrect?:')
    if user_input == 'c':
        print(f'It took me {guess_counter} tries to guess your number!')
        break
    elif user_input == 'h':
        max_number_to_guess = guess
    elif user_input == 'l':
        min_number_to_guess = guess
    else:
        print('Expected input h/l/c')
        continue

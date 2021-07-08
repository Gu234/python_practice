from random import randint

def get_cows_and_bulls(num, target):
    cows = 0
    bulls = 0
    pairs_to_compare = list(zip(str(target), str(num)))
    for target_digit, number_digit in pairs_to_compare:
        if target_digit == number_digit:
            cows += 1
        elif target_digit in str(num) :
            bulls += 1
    
    return cows, bulls

target_number = randint(1000, 9999)
guess_counter = 0
print(target_number)

while True:
    user_input = input('Enter 4-digit a number:')
    input_number = int(user_input)
    guess_counter += 1

    if input_number == target_number:
        print(
            f'You guessed correctly with {guess_counter} guesses!Congratulations!')
        break
    cows, bulls = get_cows_and_bulls(input_number, target_number)
    print(f'{cows} cows, {bulls} bulls')

target_word = 'EVAPORATE'
clue_word = ['-'] * len(target_word)
letters_tried = set()

while True:
    player_input = input('Guess your letter: ')
    input_letter = player_input.upper()
    if input_letter in letters_tried:
        print('You tried this letter already.')
        continue
    letters_tried.add(input_letter)
    if input_letter in target_word:
        print('Correct!')
    else:
        print('Incorrect!')
    for index, letter in enumerate(target_word):
        if letter == input_letter:
            clue_word[index] = letter
    print(''.join(clue_word))
    if '-' not in clue_word:
        print('Congratulations! You win!')
        break

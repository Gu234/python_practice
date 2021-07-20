from random import choice

with open('sowpods.txt') as file:
    words = file.read().splitlines()

random_word = choice(words)

print(random_word)

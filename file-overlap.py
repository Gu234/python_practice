with open('happynumbers.txt') as happynumbers:
    happy_nums = happynumbers.read().splitlines()
with open('primenumbers.txt') as primenumbers:
    prime_nums = primenumbers.read().splitlines()
print(set(happy_nums).intersection(set(prime_nums)))

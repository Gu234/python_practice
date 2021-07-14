from collections import Counter

with open('nameslist.txt') as file:
    nameslist = file.read().splitlines()

c = Counter(nameslist)
print(c)

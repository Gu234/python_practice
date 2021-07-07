from random import randint
a = [randint(1, 100) for _ in range(10)]
b = [randint(1, 100) for _ in range(12)]

print(a)
print(b)
print(set(a).intersection(set(b)))

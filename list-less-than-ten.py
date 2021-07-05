a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

# extras

# 1
new_a = list(filter(lambda x: x < 5, a))
print(new_a)

# 3
input_number = input('Enter an integer =>')
number = int(input_number)
new_list = [i for i in a if i < number]
print(new_list)

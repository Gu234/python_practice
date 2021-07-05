input_num = input('Enter an integer=>')
num = int(input_num)
dividers = [i for i in range(2, num + 1) if num % i == 0]
print(dividers)

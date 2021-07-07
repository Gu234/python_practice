def is_prime(num):
    dividers = [i for i in range(2, num) if num % i == 0]
    return dividers == []

input_num = input('Enter an integer=>')
num = int(input_num)

if is_prime(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')


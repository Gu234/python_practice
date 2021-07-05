input_number = input('Enter an intiger =>')
number = int(input_number)
if number % 4 == 0:
    print('Number is multiple of 4!')
else:
    if number % 2 == 0:
        print('Number in even')
    else:
        print('Number in odd')

num = input('Enter an intiger to be divided =>')
check = input('Enter an intiger to divide with =>')

if int(num) % int(check) == 0:
    print(f'Number {check} divides {num} evenly')
else:
    print(f'Number {check} fails to divide {num} evenly')

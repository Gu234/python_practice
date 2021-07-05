from datetime import date
name = input('Enter your name =>')

age = input('Enter your age =>')
message_count = input('Enter number of messages to print out =>')
current_year = date.today().year
try:
    target_year = current_year + 100 - int(age)
    for i in range(int(message_count)):
        print(f'{name}! In year {target_year} you will turn 100 years old!')
except ValueError as e:
    print("Error: wrong number provided:", e)
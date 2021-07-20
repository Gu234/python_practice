people_birthdays = {
    'Albert Einstein': 'March 14',
    'Benjamin Franklin': 'January 17',
    'Ada Lovelace': 'December 10'
}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for person in people_birthdays:
    print(person)
user_input = input("Who's birthday do you want to look up? ")
try:
    print(f"{user_input}'s birthday is {people_birthdays[user_input]}")
except KeyError:
    print('No such name in the database.')

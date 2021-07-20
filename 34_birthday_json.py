import json
with open('people_birthdays.json') as file:
    people_birthdays = json.load(file)

MSG = {
    'user_input':'Check person birthday or add a new person to database?(chk/add): ',
    'person_input':"Who's birthday do you want to look up? ",
    'welcome_msg':'Welcome to the birthday dictionary. We know the birthdays of:',
    'key_error_msg':'No such name in the database.',
    'new_birthday':'Enter his/her birthday: ',
    'new_name':'Enter a name: ',
}

user_input = input(MSG['user_input'])
if user_input == 'chk':
    print(MSG['welcome_msg'])
    for person in people_birthdays:
        print(person)
    person_input = input(MSG['person_input'])
    try:
        print(f"{person_input}'s birthday is {people_birthdays[person_input]}")
    except KeyError:
        print(MSG['key_error_msg'])
elif user_input == 'add':
    new_name = input(MSG['new_name'])
    new_birthday = input(MSG['new_birthday'])
    with open('people_birthdays.json', 'w') as file:
        people_birthdays[new_name] = new_birthday
        json.dump(people_birthdays, file, indent=3)

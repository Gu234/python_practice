import json
from calendar import month_abbr, month_name
import matplotlib.pyplot as plt
from collections import Counter

with open('people_birthdays.json') as file:
    people_birthdays = json.load(file)

MONTHS = [month_name[i] for i in range(1, 13)]
SHORT_MONTHS = [month_abbr[i] for i in range(1, 13)]
people_birthday_months = (birthday.split()[0]
                          for birthday in people_birthdays.values())
temporary_counter = Counter(people_birthday_months)
amount_of_same_months = {month: 0 for month in MONTHS}
amount_of_same_months.update(temporary_counter)

x_axis_names = SHORT_MONTHS
y_axis_values = list(amount_of_same_months.values())
plt.bar(x_axis_names, y_axis_values)
plt.show()

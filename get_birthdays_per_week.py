from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=7)

    birthdays = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        if start_of_week <= birthday_this_year < end_of_week:
            day_of_week = birthday_this_year.strftime("%A")
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Usage example
users_example = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    # Add more users as needed
]

get_birthdays_per_week(users_example)
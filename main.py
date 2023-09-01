from datetime import date, datetime, timedelta
from collections import Counter, defaultdict


def get_birthdays_per_week(users):
    #  Реалізуйте тут домашнє завдання
    #  {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}
    #  {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}

    dict_births = {}
    # today = datetime(year=2023, month=8, day=28).date()
    today = datetime.today().date()
    print(today)
    time_delta = timedelta(days=7)
    date_end = today + time_delta
    print(date_end)

    for dict_user in users:
        for day_match in range(0, time_delta.days+1):
            dat_delta = timedelta(days=day_match)
            dat_birth = dict_user['birthday']

            if dict_user['birthday'].year == (dict_user['birthday']-dat_delta).year:
                print('No change year')
                dat_birth = datetime(
                    year=today.year, month=dat_birth.month, day=dat_birth.day)
            else:
                print('Change year')
                dat_birth = datetime(
                    year=today.year+1, month=dat_birth.month, day=dat_birth.day)
            if dat_birth.date() == today + dat_delta:
                print('Yeah')
                print((today+dat_delta).strftime('%A'))
                if (today+dat_delta).strftime('%A') not in dict_births:
                    dict_births[(today+dat_delta).strftime('%A')] = []
                dict_births[(today+dat_delta).strftime('%A')].append(dict_user['name'])
                break
    print(dict_births)
    return dict_births


if __name__ == "__main__":
    users = [
        #  {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

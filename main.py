from datetime import date, datetime, timedelta
from collections import Counter, defaultdict


def get_birthdays_per_week(users):
    #  Реалізуйте тут домашнє завдання
    #  {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}
    #  {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}

    dict_births = {}
    today = datetime(year=2023, month=12, day=26).date()
    # today = datetime.today().date()
    # print(today)
    time_delta = timedelta(days=7)
    date_end = today + time_delta
    # print(date_end)

    for dict_user in users:
        for day_match in range(0, time_delta.days):
            dat_delta = timedelta(days=day_match)
            dat_birth = dict_user['birthday']

            if dict_user['birthday'].year == (dict_user['birthday']-dat_delta).year:
                dat_birth = datetime(
                    year=today.year, month=dat_birth.month, day=dat_birth.day)
            else:
                dat_birth = datetime(
                    year=today.year+1, month=dat_birth.month, day=dat_birth.day)

            if dat_birth.date() == today + dat_delta:
                if (today+dat_delta).strftime('%A') == 'Monday':
                    if ('Monday') not in dict_births:
                        dict_births['Monday'] = []
                    dict_births['Monday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Tuesday':
                    if ('Tuesday') not in dict_births:
                        dict_births['Tuesday'] = []
                    dict_births['Tuesday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Wednesday':
                    if ('Wednesday') not in dict_births:
                        dict_births['Wednesday'] = []
                    dict_births['Wednesday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Thursday':
                    if ('Thursday') not in dict_births:
                        dict_births['Thursday'] = []
                    dict_births['Thursday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Friday':
                    if ('Friday') not in dict_births:
                        dict_births['Friday'] = []
                    dict_births['Friday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Saturday':
                    if ('Monday') not in dict_births:
                        dict_births['Monday'] = []
                    dict_births['Monday'].append(dict_user['name'])
                    break
                elif (today+dat_delta).strftime('%A') == 'Sunday':
                    if ('Monday') not in dict_births:
                        dict_births['Monday'] = []
                    dict_births['Monday'].append(dict_user['name'])
                    break






                # print((today+dat_delta).strftime('%A'))
                # if (today+dat_delta).strftime('%A') == 'Saturday' or (today+dat_delta).strftime('%A') == 'Sunday':
                #     if ('Monday') not in dict_births:
                #         dict_births['Monday'] = []
                #     dict_births['Monday'].append(dict_user['name'])
                #     break
                # if (today+dat_delta).strftime('%A') not in dict_births:
                #     dict_births[(today+dat_delta).strftime('%A')] = []
                # dict_births[(today+dat_delta).strftime('%A')
                #             ].append(dict_user['name'])
                # break

    # print(dict_births)
    return dict_births


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 9, 1).date()},
        {"name": "Alice", "birthday": datetime(2023, 9, 5).date()},
        {"name": "John", "birthday": datetime(2023, 9, 3).date()},
        {"name": "Doe", "birthday": datetime(2024, 9, 4).date()},
        {"name": "Maria", "birthday": datetime(1976, 9, 2).date()},
        {"name": "Sylvia", "birthday": datetime(1976, 9, 1).date()},
        {"name": "Jessica", "birthday": datetime(1976, 9, 6).date()},
        {"name": "Pamela", "birthday": datetime(1976, 9, 7).date()},
        {"name": "Cortny", "birthday": datetime(1990, 9, 8).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

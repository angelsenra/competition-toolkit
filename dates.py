DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def date(day, month, year):
    """Returns the number of days since 1/1/1"""
    isLeap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    y = year - 1
    untilYear = y * 365 + y // 4 - y // 100 + y // 400
    untilMonth = sum(DAYS[:month]) + (month > 2 and isLeap)
    return untilYear + untilMonth + day

print(date(28, 2, 2018))

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").title().strip()
    try:
        month, day, year = date.split('/')
    except ValueError:
        try:
            monthday, year = date.split(', ')
        except ValueError:
            continue
        else:
            month, day = monthday.split(' ')
            try:
                month = (months.index(month)) + 1
            except ValueError:
                continue
            day = int(day)
            if month < 13 and day < 32:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
    else:
        try:
            month = int(month)
        except ValueError:
            continue
        day = int(day)
        if month < 13 and day < 32:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue




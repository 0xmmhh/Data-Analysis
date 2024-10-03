import csv
from datetime import datetime

with open('przykladowe_dane.csv', mode='r', encoding='utf-8') as pesel_file:
        reader = csv.reader(pesel_file)
        next(reader)
        pesel = []
        for row in reader:
            pesel.append(row[2])

def pesel_decrypt(pesel):
    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    gender = pesel[9]

    if int(gender) % 2 == 0:
        sex = "Kobieta"
    else:
        sex = "Mężczyzna"

    if 81 <= int(month) <= 92:
        month = month - 80
        year = year + 1800
    elif 21 <= int(month) <= 32:
        month = month - 20
        year = year + 2000
    elif 41 <= int(month) <= 52:
        month = month - 40
        year = year + 2100
    elif 61 <= int(month) <= 72:
        month = month - 60
        year = year + 2200
    elif 1 <= int(month) <= 12:
        year = year + 1900

    return [day, month, year, sex]
    # birth_date = datetime(year, month, day).date() # do wyjebania

    # wynik = f"{birth_date}, {sex}"

    # return wynik

def zodiac_signs(birth_date):
    zodiac_signs = [
        ('Koziorożec', (12, 22), (1, 19)),
        ('Wodnik', (1, 20), (2, 18)),
        ('Ryby', (2, 19), (3, 20)),
        ('Baran', (3, 21), (4, 19)),
        ('Byk', (4, 20), (5, 20)),
        ('Bliźnięta', (5, 21), (6, 20)),
        ('Rak', (6, 21), (7, 22)),
        ('Lew', (7, 23), (8, 22)),
        ('Panna', (8, 23), (9, 22)),
        ('Waga', (9, 23), (10, 22)),
        ('Skorpion', (10, 23), (11, 21)),
        ('Strzelec', (11, 22), (12, 21)),
        ('Koziorożec', (12, 22), (12, 31)),
    ]

    month = birth_date.month
    day = birth_date.day

    for znak, (start_m, start_d), (end_m, end_d) in zodiac_signs:
        if (start_m == month and day >= start_d) or (end_m == month and day <= end_d):
            return znak
#linijke nizej zamiast recznego wpisywania daty trzeba zrobic tak, zeby bralo z listy "pesel" bo nie wiem jak
# birth_date = datetime(2000, 7, 14).date()
# znak = zodiac_signs(birth_date)
# print(znak)
# print(birth_date)
print(pesel_decrypt(pesel[0]))
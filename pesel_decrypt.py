import csv
from datetime import datetime

with open('przykladowe_dane.csv', mode='r', encoding='utf-8') as pesel_plik:
        reader = csv.reader(pesel_plik)
        next(reader)
        pesele = []
        for row in reader:
            pesele.append(row[2])

def pesel_decrypt(pesele):
    rok = int(pesele[:2])
    miesiac = int(pesele[2:4])
    dzien = int(pesele[4:6])
    gender = pesele[9]

    if int(gender) % 2 == 0:
        sex = "Kobieta"
    else:
        sex = "Mężczyzna"

    if 81 <= int(miesiac) <= 92:
        miesiac = miesiac - 80
        rok = rok + 1800
    elif 21 <= int(miesiac) <= 32:
        miesiac = miesiac - 20
        rok = rok + 2000
    elif 41 <= int(miesiac) <= 52:
        miesiac = miesiac - 40
        rok = rok + 2100
    elif 61 <= int(miesiac) <= 72:
        miesiac = miesiac - 60
        rok = rok + 2200
    elif 1 <= int(miesiac) <= 12:
        rok = rok + 1900

    data_urodzenia = datetime(rok, miesiac, dzien).date()

    wynik = f"{data_urodzenia}, {sex}"

    return wynik

def znak_zodiaku(data_urodzenia):
    znaki_zodiaku = [
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

    miesiac = data_urodzenia.month
    dzien = data_urodzenia.day

    for znak, (start_m, start_d), (end_m, end_d) in znaki_zodiaku:
        if (start_m == miesiac and dzien >= start_d) or (end_m == miesiac and dzien <= end_d):
            return znak
#linijke nizej zamiast recznego wpisywania daty trzeba zrobic tak, zeby bralo z listy "pesele" bo nie wiem jak
data_urodzenia = datetime(2000, 7, 14).date()
znak = znak_zodiaku(data_urodzenia)
print(znak)
print(data_urodzenia)
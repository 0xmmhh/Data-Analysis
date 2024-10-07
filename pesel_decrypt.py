import csv
import matplotlib as plt
import matplotlib.pyplot as plt
from collections import Counter

with open('przykladowe_dane.csv', mode='r', encoding='utf-8') as pesel_file:
    reader = csv.reader(pesel_file)
    next(reader)
    pesel = []
    names = []
    last_names = []
    for row in reader:
        pesel.append(row[2])
        names.append(row[0])
        last_names.append(row[1])


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

    pesel_data = [day, month, year, sex]

    return pesel_data


def zodiac_signs(day, month):
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

    for sign, (st_m, st_d), (end_m, end_d) in zodiac_signs:
        if (st_m == month and day >= st_d) or (end_m == month and day <= end_d):
            return sign


Koz = 0
Wod = 0
Ryb = 0
Bar = 0
Byk = 0
Bli = 0
Rak = 0
Lew = 0
Pan = 0
Wag = 0
Sko = 0
Stz = 0

for i in range(2302):
    pesel_data = pesel_decrypt(pesel[i])
    birth_date = [pesel_data[2] - pesel_data[1] - pesel_data[0]]
    zodiac = zodiac_signs(pesel_data[0], pesel_data[1])
    if zodiac == 'Koziorożec':
        Koz += 1
    elif zodiac == 'Wodnik':
        Wod += 1
    elif zodiac == 'Ryby':
        Ryb += 1
    elif zodiac == 'Baran':
        Bar += 1
    elif zodiac == 'Byk':
        Byk += 1
    elif zodiac == 'Bliźnięta':
        Bli += 1
    elif zodiac == 'Rak':
        Rak += 1
    elif zodiac == 'Lew':
        Lew += 1
    elif zodiac == 'Panna':
        Pan += 1
    elif zodiac == 'Waga':
        Wag += 1
    elif zodiac == 'Skorpion':
        Sko += 1
    elif zodiac == 'Strzelec':
        Stz += 1

# for i in range(200):
#     pesel_data = pesel_decrypt(pesel[i])
#     birth_date = f'{pesel_data[2]}-{pesel_data[1]}-{pesel_data[0]}' 
#     zodiac = zodiac_signs(pesel_data[0], pesel_data[1]) 

# print(f"PESEL: {pesel[i]}, Data urodzenia: {birth_date}, Płeć: {pesel_data[3]}, Znak zodiaku: {zodiac}")
# print(pesel_decrypt(pesel[0]))
zodiac_names = ['Koziorożec', 'Wodnik', 'Ryby', 'Baran', 'Byk', 'Bliźnięta', 'Rak', 'Lew', 'Panna', 'Waga', 'Skorpion',
                'Strzelec']
zodiac_count = [Koz, Wod, Ryb, Bar, Byk, Bli, Rak, Lew, Pan, Wag, Sko, Stz]


def zodiac_analysis1():
    fig, ax = plt.subplots()
    ax.bar(zodiac_names, zodiac_count, color='tab:blue')

    ax.set_label('Liczba osób')
    ax.set_title('Liczba osób według znaków zodiaku')

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

def name_analysis1(start_decade, end_decade):
    names_in_decade = []

    for i, pesel_number in enumerate(pesel):
        pesel_data = pesel_decrypt(pesel_number)
        year = pesel_data[2]

        if start_decade <= year <= end_decade:
            names_in_decade.append(names[i])

    name_counter = Counter(names_in_decade)
    most_common_name = name_counter.most_common(10)

    if most_common_name:
        name_labels, name_counts = zip(*most_common_name)

        fig, ax = plt.subplots()
        ax.bar(name_labels, name_counts, color="tab:blue")

        ax.set_ylabel("Liczba wystąpień")
        ax.set_title(f"Top 10 najczęściej występujących imion w latach {start_decade}-{end_decade}")

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"Brak danych dla lat {start_decade}-{end_decade}")

def zodiac_analysis2():

    year_to_analyze = 2004 # tutaj wpisujemy rok jako Int
    zodiac_count_year = []


    labels = list(zodiac_count_year)
    sizes = list(zodiac_count_year)
    colors = plt.cm.Paired.colors

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    ax.set_title(f'Rozkład znaków zodiaku w roku {year_to_analyze}')

    plt.show()


zodiac_analysis2()
#zodiac_analysis1()
name_analysis1(1999, 2000)
import csv
import matplotlib as plt
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

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


def zodiac_analysis2(year_to_analyze):
    Koz2 = 0
    Wod2 = 0
    Ryb2 = 0
    Bar2 = 0
    Byk2 = 0
    Bli2 = 0
    Rak2 = 0
    Lew2 = 0
    Pan2 = 0
    Wag2 = 0
    Sko2 = 0
    Stz2 = 0

    zodiac_yr_arr = []

    for i, pesel_number in enumerate(pesel):
        pesel_data = pesel_decrypt(pesel_number)
        if pesel_data is None:
            continue
        year = pesel_data[2]
        if year == year_to_analyze:
            zodiac = zodiac_signs(pesel_data[0], pesel_data[1])
            zodiac_yr_arr.append(zodiac)

    for zodiac in zodiac_yr_arr:

        if zodiac == 'Koziorożec':
            Koz2 += 1
        elif zodiac == 'Wodnik':
            Wod2 += 1
        elif zodiac == 'Ryby':
            Ryb2 += 1
        elif zodiac == 'Baran':
            Bar2 += 1
        elif zodiac == 'Byk':
            Byk2 += 1
        elif zodiac == 'Bliźnięta':
            Bli2 += 1
        elif zodiac == 'Rak':
            Rak2 += 1
        elif zodiac == 'Lew':
            Lew2 += 1
        elif zodiac == 'Panna':
            Pan2 += 1
        elif zodiac == 'Waga':
            Wag2 += 1
        elif zodiac == 'Skorpion':
            Sko2 += 1
        elif zodiac == 'Strzelec':
            Stz2 += 1

    sizes = [Koz2, Wod2, Ryb2, Bar2, Byk2, Bli2, Rak2, Lew2, Pan2, Wag2, Sko2, Stz2]

    if sum(sizes) == 0:
        print(f"Brak danych dla roku {year_to_analyze}.")
        return

    labels = zodiac_names
    colors = plt.cm.Paired.colors

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    ax.set_title(f'Rozkład znaków zodiaku w roku {year_to_analyze}')

    plt.tight_layout()
    plt.show()


def name_analysis2(target_name):
    decades = list(range(1950, 2020, 10))
    decade_labels = [f"{decade}s" for decade in decades]
    decade_counts = {decade: 0 for decade in decades}

    for i, pesel_number in enumerate(pesel):
        pesel_data = pesel_decrypt(pesel_number)
        year = pesel_data[2]

        if 1950 <= year <= 2019:
            decade = (year // 10) * 10
            if decade in decade_counts:
                if names[i].strip().lower() == target_name.strip().lower():
                    decade_counts[decade] += 1

    counts = [decade_counts[decade] for decade in decades]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(decade_labels, counts, marker='o', linestyle='-', color='tab:blue')

    ax.set_xlabel('Dekada')
    ax.set_ylabel('Liczba osób')
    ax.set_title(f'Popularność imienia "{target_name}" na przestrzeni dekad (1950-2019)')

    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()


def zodiac_heatmap():
    decades = list(range(1950, 2019, 10))
    decade_labels = [f"{decade}s" for decade in decades]

    heatmap_data = {sign: {decade: 0 for decade in decades} for sign in zodiac_names}

    for i, pesel_number in enumerate(pesel):
        pesel_data = pesel_decrypt(pesel_number)
        if pesel_data is None:
            continue
        year = pesel_data[2]
        zodiac = zodiac_signs(pesel_data[0], pesel_data[1])

        if zodiac in zodiac_names and 1950 <= year <= 2020:
            decade = (year // 10) * 10
            if decade in decades:
                heatmap_data[zodiac][decade] += 1

    heatmap_matrix = []
    for sign in zodiac_names:
        row = [heatmap_data[sign][decade] for decade in decades]
        heatmap_matrix.append(row)
    heatmap_matrix = np.array(heatmap_matrix)

    fig, ax = plt.subplots(figsize=(8, 6))

    cax = ax.imshow(heatmap_matrix, aspect='auto', cmap='inferno', interpolation='bilinear')

    ax.set_xticks(np.arange(len(decades)))
    ax.set_xticklabels(decade_labels, rotation=45)
    ax.set_yticks(np.arange(len(zodiac_names)))
    ax.set_yticklabels(zodiac_names)

    cbar = fig.colorbar(cax)
    cbar.set_label('Liczba osób')

    ax.set_title('Heatmapa rozkładu znaków zodiaku na przestrzeni dekad (1950-2019)')

    plt.tight_layout()
    plt.show()


#zodiac_analysis2(2000)
#zodiac_analysis1()
#name_analysis1(1983, 2020)
#name_analysis2('Piotr')
#zodiac_heatmap()

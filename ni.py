import csv
import random
from datetime import datetime, timedelta


# pesel = 11 cyfr = yy mm dd PPP Płeć K, płeć : kobieta = płeć % 2 == 0, mężczyzna =! płeć % 2 == 0
def generuj_pesel(data_urodzenia, plec):
    rok, miesiac, dzien = data_urodzenia.strftime("%y"), data_urodzenia.strftime("%m"), data_urodzenia.strftime("%d")

    # tutaj zmienić jeżeli dziwne daty się pojawią, dodać warunki również dla 19, 20, 22, 23 wieku
    if data_urodzenia.year >= 2000:
        miesiac = str(int(miesiac) + 20)

    random_part = f"{random.randint(0, 999):03}"
    if plec == "M":
        numer_seryjny = random.choice([1, 3, 5, 7, 9])
    else:
        numer_seryjny = random.choice([0, 2, 4, 6, 8])

    pesel = f"{rok}{miesiac}{dzien}{random_part}{numer_seryjny}"

    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma_kontrolna = sum(int(pesel[i]) * wagi[i] for i in range(10))
    cyfra_kontrolna = (10 - suma_kontrolna % 10) % 10
    pesel += str(cyfra_kontrolna)

    return pesel


# tutaj można dorobić prawdopodobieństwo oparte na populacji danego imienia (np. Piotrów jest 1.2m na 40m ludzi: 1.2/40 = 0.03 \\
# czyli szansa na wystąpienie piotra to 3%)
def generuj_dane(n):
    imiona_meskie = []
    with open('same_imiona_M.csv', mode='r', encoding='utf-8') as imiona_plik:
        reader = csv.reader(imiona_plik)
        for row in reader:
            imiona_meskie.append(row[0])

    imiona_zenskie = []
    with open('same_imiona_K.csv', mode='r', encoding='utf-8') as imiona_plik:
        reader = csv.reader(imiona_plik)
        for row in reader:
            imiona_zenskie.append(row[0])

    nazwiska = []
    with open('same_nazwiska_K.csv', mode='r', encoding='utf-8') as nazwiska_plik:
        reader = csv.reader(nazwiska_plik)
        for row in reader:
            nazwiska.append(row[0])

    with open('same_nazwiska_M.csv', mode='r', encoding='utf-8') as nazwiska_plik:
        reader = csv.reader(nazwiska_plik)
        for row in reader:
            nazwiska.append(row[0])

    with open('przykladowe_dane.csv', mode='w', newline='', encoding='utf-8') as plik:
        writer = csv.writer(plik)
        writer.writerow(["Imię", "Nazwisko", "PESEL"])

        for _ in range(n):
            plec = random.choice(["M", "K"])
            if plec == "M":
                imie = random.choice(imiona_meskie)
            else:
                imie = random.choice(imiona_zenskie)
            nazwisko = random.choice(nazwiska)
            data_urodzenia = datetime(1950, 1, 1) + timedelta(days=random.randint(0, 365 * 70))
            pesel = generuj_pesel(data_urodzenia, plec)

            writer.writerow(
                [imie, nazwisko, pesel])


# tu numerek generuje plik z zadaną ilością wierszy
generuj_dane(2302)

import csv
import random
from datetime import datetime, timedelta


def generuj_pesel(data_urodzenia, plec):
    # PESEL składa się z 11 cyfr, gdzie 6 pierwszych to data urodzenia (RRMMDD)
    rok, miesiac, dzien = data_urodzenia.strftime("%y"), data_urodzenia.strftime("%m"), data_urodzenia.strftime("%d")

    # Modyfikacja miesiąca w zależności od wieku (dla XX wieku jest to oryginalna wartość, dla XXI + 20)
    if data_urodzenia.year >= 2000:
        miesiac = str(int(miesiac) + 20)

    # 4 cyfry losowe (z czego ostatnia zależy od płci: parzysta dla kobiet, nieparzysta dla mężczyzn)
    random_part = f"{random.randint(0, 999):03}"  # 3 losowe cyfry
    if plec == "M":
        numer_seryjny = random.choice([1, 3, 5, 7, 9])  # nieparzysta dla mężczyzn
    else:
        numer_seryjny = random.choice([0, 2, 4, 6, 8])  # parzysta dla kobiet

    pesel = f"{rok}{miesiac}{dzien}{random_part}{numer_seryjny}"

    # Oblicz cyfrę kontrolną
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma_kontrolna = sum(int(pesel[i]) * wagi[i] for i in range(10))
    cyfra_kontrolna = (10 - suma_kontrolna % 10) % 10
    pesel += str(cyfra_kontrolna)

    return pesel


def generuj_dane(n):
    imiona_meskie = ["Jan", "Adam", "Piotr", "Krzysztof", "Marek", "Tomasz", "Andrzej", "Michał", "Bartosz", "Łukasz", "Robert", "Kamil", "Karol", "Mateusz", "Paweł", "Damian"]
    imiona_zenskie = ["Anna", "Katarzyna", "Maria", "Ewa", "Magdalena", "Agnieszka", "Joanna", "Małgorzata", "Natalia", "Aleksandra", "Karolina", "Patrycja", "Weronika"]
    nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kaczmarek", "Lewandowski", "Wojciechowski", "Dąbrowski", "Kozłowski", "Jankowski", "Mazur", "Kwiatkowski", "Krawczyk"]

    with open('../../PycharmProjects/HelloWorld/przykladowe_dane.csv', mode='w', newline='') as plik:
        writer = csv.writer(plik)
        writer.writerow(["Imię", "Nazwisko", "PESEL", "Data urodzenia", "Płeć"])

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


# Generowanie pliku CSV z 100 przykładowymi rekordami
generuj_dane(2302)

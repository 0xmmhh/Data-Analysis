import csv

def decode_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        raise ValueError("PESEL musi składać się z 11 cyfr")

    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    
    if month > 12:
        year += 2000
        month -= 20
    elif month > 0:
        year += 1900
    else:
        raise ValueError("Niepoprawny miesiąc w PESEL")

    return year

def read_pesel_from_csv(file_path):
    years = set()
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                pesel = row[2]
                year = decode_pesel(pesel)
                years.add(year)
            except ValueError as e:
                print(f"Niepoprawny PESEL {pesel} w wierszu {row}: {e}")
    return years

file_path = 'przykladowe_dane.csv'

years_of_birth = read_pesel_from_csv(file_path)

sorted_years_of_birth = sorted(years_of_birth)

print(sorted_years_of_birth)

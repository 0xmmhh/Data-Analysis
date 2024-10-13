import PySimpleGUI as sg
from pesel_decrypt import zodiac_heatmap, name_analysis1, name_analysis2, zodiac_analysis1, zodiac_analysis2

tab1_layout = [
    [sg.Text('Wpisz imię, żeby zobaczyć jak występowało w różnych dekadach')],
    [sg.Text('Imię:'), sg.InputText(size=(15, 1), key='-NAME-')],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab1"), sg.Button('Anuluj', size=(10, 1))]
]

tab2_layout = [
    [sg.Text('Wpisz przedziały lat, dla których zobaczysz jakie imię było najpopularniejsze')],
    [sg.Text('Początkowy przedział:'), sg.InputText(size=(8, 1), key='-START_YEAR-'), 
     sg.Text('Końcowy przedział:'), sg.InputText(size=(8, 1), key='-END_YEAR-')],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab2"), sg.Button('Anuluj', size=(10, 1))]
]

tab3_layout = [
    [sg.Text('Liczba osób według znaków zodiaku')],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab3"), sg.Button('Anuluj', size=(10, 1))]
]

tab4_layout = [
    [sg.Text('Wpisz rok, żeby zobaczyć jak rozkładają się znaki zodiaku w danym roku')],
    [sg.Text('Rok:'), sg.InputText(size=(10, 1), key='-YEAR-')],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab4"), sg.Button('Anuluj', size=(10, 1))]
]

tab5_layout = [
    [sg.Text('Heatmapa rozkładu znaków na przestrzeni dekad (1950-2019)')],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab5"), sg.Button('Anuluj', size=(10, 1))]
]

layout = [
    [sg.TabGroup([[sg.Tab('Analiza imienia', tab1_layout),
                    sg.Tab('Analiza imion', tab2_layout),
                    sg.Tab("Analiza zodiakow1", tab3_layout),
                    sg.Tab("Analiza zodiakow2", tab4_layout),
                    sg.Tab("Heatmapa imion", tab5_layout)]])]
]

window = sg.Window("Analiza danych", layout, resizable=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Anuluj":
        break
    elif event == "tab1":
        name = values['-NAME-']
        name_analysis2(name)
    elif event == "tab2":
        start_year = int(values['-START_YEAR-'])
        end_year = int(values['-END_YEAR-'])
        name_analysis1(start_year, end_year)
    elif event == "tab3":
        zodiac_analysis1()
    elif event == "tab4":
        year = int(values['-YEAR-'])
        zodiac_analysis2(year)
    elif event == "tab5":
        zodiac_heatmap()

window.close()

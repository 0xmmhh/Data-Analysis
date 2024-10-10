import PySimpleGUI as sg

tab1_layout = [
    [sg.Text('Wpisz imię, żeby zobaczyć jak występowało w różnych dekadach')],
    [sg.Text('Imię:'), sg.InputText(size=(15, 1))],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab1"), sg.Button('Anuluj', size=(10, 1))]
]

tab2_layout = [
    [sg.Text('Wpisz przedziały lat, dla których zobaczysz jakie imie było najpopularniejsze')],
    [sg.Text('Początkowy przedział:'), sg.InputText(size=(8, 1)), sg.Text('Końcowy przedział:'), sg.InputText(size=(8, 1))],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab2"), sg.Button('Anuluj', size=(10, 1))]
]

tab3_layout = [
    [sg.Text('Liczba osób według znaków zodiaku')],
    [sg.Button('Stwórz wykres', size=(10, 1), key="tab3"), sg.Button('Anuluj', size=(10, 1))]
]

tab4_layout = [
    [sg.Text('Wpisz rok, żeby zobaczyć jak rozkładają się znaki zodiaku w danym roku')],
    [sg.Text('Rok:'), sg.InputText(size=(10, 1))],
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
    print("You entered ", values)

window.close()

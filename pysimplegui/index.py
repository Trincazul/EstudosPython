import PySimpleGUI as sg

sg.theme('DarkPurple')   # Tipos de temas já existentes na lib
# dentro da caixa do programa
layout = [  [sg.Text('Exemplo de texto')],
            [sg.Text('Digite alguma coisa'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')] ]

# Cria uma janela
window = sg.Window('Window Title', layout)
# evento de loop com values e inputs 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    print('Clicou ', values[0])

window.close()

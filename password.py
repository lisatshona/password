import random
import string
import PySimpleGUI as sg



upper = random.sample(string.ascii_uppercase, 3)
lower = random.sample(string.ascii_lowercase, 2)
digits = random.sample(string.digits, 2)
symbols = random.sample(string.punctuation, 2)

total = upper+lower+digits+symbols
total = random.sample(total, len(total))
total = ''.join(total)
print(total)

sg.theme('DarkBlue6')
sg.set_options(font='Arial 4')
layout = [
    [sg.Text('Uppercase: '),sg.Push(), sg.Input(size=15, key='-UP')],
    [sg.Text('Lowercase: '),sg.Push(), sg.Input(size=15, key='-LOW')],
    [sg.Text('Digits: '),sg.Push(), sg.Input(size=15, key='-DIG-')],
    [sg.Text('Symbols: '), sg.Push(),sg.Input(size=15, key='-SYM-')],
    [sg.Button('Ok'), sg.Button('Çancel')],
    [sg.Text('Password'), sg.Push(), sg.Multiline(size=15, no_scrollbar=True, disabled=True, key='-PASS')]
    
]
window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
    
    if event =='Ok':
        try:
             u_upper = int(values['-UP'])
             upper = random.sample(string.ascii_uppercase, u_upper)
             u_lower = int(values['-LOW'])
             lower = random.sample(string.ascii_lowercase, u_lower)
             u_digits = int(values['-DIG'])
             digits = random.sample(string.digits, u_digits)
             u_symbols = int(values['-SYM'])
             symbols = random.sample(string.punctuation, u_symbols)

             total = upper+lower+digits+symbols
             total = random.sample(total, len(total))
             total = ''.join(total)
             window['-PASS-'].update(total)
        except ValueError:
             window['-PASS'].update("No Valid Number")

window.close()
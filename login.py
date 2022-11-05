
import PySimpleGUI as sg
import os
from settings import Settings
# here is the login window

def login():
    # select the theme
    sg.theme('DarkAmber')
    # define the layout
    layout = [
        [sg.Text('Welcome to the Aircraft Platform')],
        # i haven't find a suitable image, so just wait until i find one
        # [sg.image('2DAircraftPlat\images\logo.png')],
        [sg.Text('Choose the blue aircraft number'), sg.InputText()],
        [sg.Text('Choose the red aircraft number'), sg.InputText()],
        [sg.Text('Choose the strategy for blue aircraft'), sg.InputCombo(('Random', 'Manual', 'AI'), key='-BLUE-')],
        [sg.Text('Choose the strategy for red aircraft'), sg.InputCombo(('Random', 'Manual', 'AI'), key='-RED-')],
        [sg.Button('Lets Go!'), sg.Button('Exit')]
    ]

    # create the window
    window = sg.Window('Aircraft Platform', layout)
    return window

if __name__ == '__main__':
    # define the settings
    # call the login function
    window = login()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Lets Go!':
            # get the settings
            settings = Settings()
            settings.ini['Aircraft']['blue'] = values[0]
            settings.ini['Aircraft']['red'] = values[1]
            settings.ini['Aircraft']['blue_strategy'] = values['-BLUE-']
            settings.ini['Aircraft']['red_strategy'] = values['-RED-']
            # save the settings
            settings.save()
            # close the window
            window.close()
            # start the game
            os.system('python 2DAircraftPlat\main.py')
            # call the login function
            window = login()

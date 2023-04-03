import PySimpleGUI as simpleGUI

#Definig the layout of GUI
layout = [[simpleGUI.Input(key='-TEXT-', size=(100, 1))],
          [simpleGUI.Text('Width'), simpleGUI.Input(key='-WIDTH-', size=(10, 1)), simpleGUI.Text('Height'),
           simpleGUI.Input(key='-HEIGHT-', size=(10, 1), enable_events=True)],
          [simpleGUI.Text('Version [1 - 10]'), simpleGUI.Input(key='-VERSION-', size=(10, 1), enable_events=True)],
          [simpleGUI.ColorChooserButton('Fill Color'), simpleGUI.Input(key='-FILL-', readonly=True, size=(10, 1))],
          [simpleGUI.ColorChooserButton('Background Color'),
           simpleGUI.Input(key='-BACK-', readonly=True, size=(10, 1))],
          [simpleGUI.Button('Create')],
          [simpleGUI.Image(key='-DISPLAY-QR-CODE-', expand_x=True, expand_y=True)]]

#Window which is the stage or the main frame where every thing is handled in the window
window = simpleGUI.Window('QR CODE GENERATOR', layout)

#Adding validations to all input boxes to ensure that only Accurate data can be captured and proccessed by the program
def validateAllInput(values):
    if values['-TEXT-'] == '':
        simpleGUI.popup('Error', 'Missing Data',
                        'Sorry you have enter a text in the first text box to create QR Code from.')
    else:
        if values['-WIDTH-'] == '':
            simpleGUI.popup('Error', 'Missing Data',
                            'Sorry you have to enter a dimension for width of the QR Code.')
        else:
            if values['-WIDTH-'][-1] not in '0123456789':
                simpleGUI.popup('Error', 'Wrong Value', 'Sorry the value for width can only be a positive number.')
            elif int(values['-WIDTH-']) <= 99 or int(values['-WIDTH-']) > 800:
                simpleGUI.popup('Error', 'Wrong Value',
                                f'Sorry the value for width can only be a positive number and greater than 99 and '
                                f'not greater than 800.')
            else:
                if values['-HEIGHT-'] == '':
                    simpleGUI.popup('Error', 'Missing Data',
                                    'Sorry you have to enter a dimension for the height of QR Code.')
                else:
                    if values['-HEIGHT-'][-1] not in '0123456789':
                        simpleGUI.popup('Error', 'Wrong Value',
                                        'Sorry the value for height can only be a positive number.')
                    elif int(values['-HEIGHT-']) <= 99 or int(values['-HEIGHT-']) > 800:
                        simpleGUI.popup('Error', 'Wrong Value',
                                        'Sorry the value for height can only be a positive number greater the 99 '
                                        'and not greater than 800.')
                    else:
                        if values['-VERSION-'] == '':
                            simpleGUI.popup('Error', 'Missing Data',
                                            'Sorry you have to enter a dimension for the height of QR Code.')
                        else:
                            if values['-VERSION-'][-1] not in '0123456789':
                                simpleGUI.popup('Error', 'Wrong Value',
                                                'Sorry the value for version can only be a positive number.')
                            elif int(values['-VERSION-']) <= 0 or int(values['-VERSION-']) > 10:
                                simpleGUI.popup('Error', 'Wrong Value',
                                                'Sorry the value for version can only be a positive number from '
                                                '1 - 10.')
                            else:
                                return True

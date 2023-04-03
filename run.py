import io

import PySimpleGUI as simpleGUI
from PIL import Image

import gui as graphics
import generate_qr_code

#This is generic function which display the genrated QR code on the window
def displayImage():
    image = Image.open(f'Codes/{file_name}.png')
    image.thumbnail((int(values['-HEIGHT-']), int(values['-WIDTH-'])))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    graphics.window['-DISPLAY-QR-CODE-'].update(data=bio.getvalue())


file_name = ''

#This function is meant to compliment the working of changing the color of QR codes
#The function for changig the color of QR codes take the color in name e.g. 'Black'
#Or RGB color scheme so this function converts the hex color gotten from ColorChooser and return RBG Color scheme
def hexToRGB(hex_val):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex_val[i:i + 2], 16)
        rgb.append(decimal)

    return tuple(rgb)


while True:
    event, values = graphics.window.read()

    if event == simpleGUI.WINDOW_CLOSED:
        break

    if event == "Create":
        if graphics.validateAllInput(values):
            file_name = generate_qr_code.generateNewName()
            if values['-FILL-'] == '' or values['-BACK-'] == '':
                fill = 'Black'
                background = 'white'
            else:
                fill = hexToRGB(values['-FILL-'][1:])
                background = hexToRGB(values['-BACK-'][1:])
            generate_qr_code.GenerateQRCodes(values['-TEXT-'], file_name, values['-VERSION-'], fill, background)
            displayImage()

graphics.window.close()

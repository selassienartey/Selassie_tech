import os

import qrcode


def generateNewName():
    # This function generates only 9 unique names the 10th one will always be overwritten
    file_name = "qr_code"
    if "Codes" not in os.listdir():
        os.mkdir('Codes')
        found_in_directory_already = os.listdir('Codes')
    else:
        found_in_directory_already = os.listdir('Codes')
    curr_num = 1
    if file_name+str(curr_num)+".png" not in found_in_directory_already:
        return file_name + str(curr_num)
    else:
        file = found_in_directory_already[-1]
        curr_num = int(file[7:-4]) + 1
        return file_name + str(curr_num)

#An oragnised class for genarating QR codes
#This take 5 arguments by only 4 are passed by user the last one is file name which is internally generated by the program
class GenerateQRCodes:
    def __init__(self, data, file_name, version, fill_color, back_color):
        self.data = data
        self.version = version
        self.fill_color = fill_color
        self.back_color = back_color
        self.file_name = file_name
        self.makeQRCode()

    def makeQRCode(self):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        self.saveQRCode(img)

    def saveQRCode(self, img):
        img.save(f'Codes/{self.file_name}.png')

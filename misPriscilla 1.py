import qrcode
import PySimpleGUI as sg

# Define the layout of the GUI
layout = [[sg.Text("Enter the text you want to encode:")],
        [sg.InputText(key='input')],
        [sg.Button('Generate QR Code'), sg.Button('Exit')],
        [sg.Image(key='-IMAGE-')]
    ]



window = sg.Window('QR Code Generator', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Generate QR Code':
        data = values['input']
        

        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        
        qr.add_data(data)
        
        qr.make(fit=True)
        
        img = qr.make_image(fill_color='blue', back_color='orange')
        

        img.save('qrcode.png')

        window['-IMAGE-'].update(filename="qrcode.png")
        

window.close()

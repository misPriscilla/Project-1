import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()
layout = [
    [sg.Text('Enter text to speak:')],
    [sg.InputText()],
    [sg.Radio('Male', 'voice', default=True, key='-MALE-'), sg.Radio('Female', 'voice', key='-FEMALE-')],
    [sg.Button('Speak'), sg.Button('Cancel')]
]


window = sg.Window('Text to Speech', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Speak':
        
        text = values[0]
        
        if values['-MALE-']:
            voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
        else:
            voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        
        engine.setProperty('voice', voice)
        
        engine.say(text)
        engine.runAndWait()



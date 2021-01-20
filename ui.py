import PySimpleGUI as sg
from main import getDomain
from main import create_rand_pass
from Database import appenddb
#from Database import checkdb

#checkdb()

def createui():
    layout = [  [sg.Text("Simple password manager")],
                [sg.Text("Website: ", size=(10,1)),
                sg.InputText("Web domain name", key='_DOMAIN_')],
                [sg.Text("Username: ", size=(10,1)),
                sg.InputText("username", key='_USERNAME_')],
                [sg.Text("Password: ", size=(10,1)),
                sg.InputText("password", key='_PASSWORD_')],
                [sg.Button("Get Domain"),sg.Button("Generate Pass"),sg.Button("Save"),sg.Button("Exit")] 
            ]
    window = sg.Window("window", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Get Domain":
            # Has to be called twice for some reason?
            window.Element('_DOMAIN_').update(getDomain())
            window.Element('_DOMAIN_').update(getDomain())
        elif event == "Generate Pass":
            window.Element('_PASSWORD_').update(create_rand_pass())
        elif event == "Save":
            appenddb(values['_DOMAIN_'],values['_USERNAME_'],values['_PASSWORD_'])
    window.close()

createui()

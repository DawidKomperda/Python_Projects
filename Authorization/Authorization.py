import PySimpleGUI as sg
import hashlib

def main():
    #Login
    login_login_hash = Szyfrowanie('Paweł')  # Paweł
    #Password  
    login_password_hash = Szyfrowanie('Pawłowski')  # Pawłowski
    def HashGeneratorGUI(): #Window to take input from user and translate it to show how encoded input looks like
        layout = [
            [sg.Text('Generacja Hasła', size=(30, 1), font='Any 13')],
            [sg.Text('Login'), sg.Input(key='-Login-')],
            [sg.Text('HashLogin'), sg.Input('', size=(40, 1), key='hashlogin')],
            [sg.Text('Hasło'), sg.Input(key='-Haslo-')],
            [sg.Text('HashHasło'), sg.Input('', size=(40, 1), key='hashhaslo')],
        ]
        #Hash generation
        window = sg.Window('SHA Generator', 
                            layout,
                            auto_size_text=False,
                            default_element_size=(10, 1),
                            text_justification='r',
                            return_keyboard_events=True,
                            grab_anywhere=True)
        while True: #While loop checking if window is still open and taking input from user,
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            hasło = values['-Haslo-']
            login = values["-Login-"]
            try:
                # Password
                window['hashhaslo'].update(Szyfrowanie(hasło)) #Update corect box with encoded input of password from user
                # Login
                window['hashlogin'].update(Szyfrowanie(login)) #Update corect box with encoded input of login from user
            except:
                pass
        window.close()

    
    def Szyfrowanie(xhash): #Encoding of the input data 
        xutf = xhash.encode('utf-8')
        sha1hashx = hashlib.sha1()
        sha1hashx.update(xutf)
        xhash = sha1hashx.hexdigest()
        return xhash
    
    def Matches(x, a_hash): #Checkin the input with encoded data
        xutf = x.encode('utf-8')
        sha1hashx = hashlib.sha1()
        sha1hashx.update(xutf)
        xhash = sha1hashx.hexdigest()
        return xhash == a_hash
    
    
    def Hasło(): # Function that ask for input and then compares input with encoded data

    haslo = sg.popup_get_text(   #Password input
    'Podaj Hasło', password_char='*',)
    if ((haslo and Matches(haslo,login_password_hash)) and (login and Matches(login, login_login_hash))): #Check if Password and Login are the same as encoded data
        print("Zalogowany")
    else:
        print("Niepoprawne hasło lub login")
    #Login input
    login = sg.popup_get_text(   
        'Podaj Login', password_char='*',)

    if (login == 'gui'):                  #Code for access to the encoding window
        HashGeneratorGUI()                              
        return                                         
        
    Hasło()

if __name__ == '__main__':
    sg.theme('DarkAmber')
    main()

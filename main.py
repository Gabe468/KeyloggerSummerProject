from pynput import keyboard
from pynput.keyboard import Controller
import os
import ast
class Logger:

    #take in key, saves it and then prints out key
    def record(key):
        try:
            if key != keyboard.Key.esc:
                keysave.append(key)
                print(key.char)
        except AttributeError:
            keysave.append(key)
            print(str(key)[4:])

    #recording stops when pressing esc
    def stopRecord(key):
        if key == keyboard.Key.esc:
            return False
        
    def recordAndStop(keysave):
        print("Recording... \nPress Esc to stop recording")
        #joins both record and stopRecord
        with keyboard.Listener(on_press=Logger.record, on_release=Logger.stopRecord) as listener:
            listener.join()
            print(keysave)
            Logger.createSave(keysave)
    
    def createSave(keysave):
        #selection to save
        while True:
            sel = input("Would you like to save the current keys? Y/N\n")
            if sel.upper() == "Y":
                name = input("Enter name for the file: \n")
                #saves file
                try:
                    save = open(name, "x")
                    save.write(str(keysave))
                    save.close()
                    print("Saved file named \"" + name +"\"" )
                    break
                #raises error if a file with the same name is created
                except FileExistsError as err:
                    print(str(err)[11:])
            if sel.upper() == "N":
                break
    
    #list the files of keylogs in folder keys
    def listKeys():
        print(os.listdir())

    #opens up the file you choose and plays keylog
    def playKeys():
        keyCont = Controller()
        while True:
            select = input("Select file to open\n")
            try:
                #opens file and reads it then converts to a list and plays each key
                key = open(select, "r")
                keys = ast.literal_eval(key.read())
                for x in keys:
                    keyCont.press(x)
                    keyCont.release(x)
                key.close()
                break
            except BaseException as err:
                print(err)

#menu title     
print("Welcome to Keylogger Project")

#selecting directory to keys folder
os.chdir("keys")

#input for menu selection
menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")

#list for keys saved
keysave = []

while True:
    #selection for recording
    if  menu == "1":
        Logger.recordAndStop(keysave)
        break
    #selection for record saving
    elif menu == "2":
        Logger.listKeys()
        Logger.playKeys()
        break
    else:
        print("Incorrect Number. Please choose a number from the selection.")
        menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")
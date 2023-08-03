from pynput import keyboard
class Logger:
    menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")

    def record(key):
        try:
            print(key.char)
        except AttributeError:
            print(str(key)[4:])

    def stopRecord(key):
        if key == keyboard.Key.esc:
            return False
    
    def saveRecording(recorded):
        recordName = input("Enter name of saved file")
        if recordName == None:
            print("Name for file cannot be empty")
        elif len(recordName) > 20:
            print("Name for file is too long")
        else: 
            f = open(recordName, "x")

print("Welcome to Keylogger Project")

while True:
    if  Logger.menu == "1":
        print("Recording... \nPress Esc to stop recording")
        with keyboard.Listener(on_press=Logger.record, on_release=Logger.stopRecord) as listener:
            listener.join()
        break

    elif menu == "2":
        pass
    else:
        print("Incorrect Number. Please choose a number from the selection.")
        menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")

    

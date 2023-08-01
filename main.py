import keyboard
class Logger:
    print("Welcome to Keylogger Project")

    def saveRecording(recorded):
        recordName = input("Enter name of saved file")
        if recordName == None:
            print("Name for file cannot be empty")
        elif len(recordName) > 20:
            print("Name for file is too long")
        else: 
            f = open(recordName, "x")

    menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")

    def record():
        recorded = keyboard.record(until='esc')

    while True:
        if  menu == "1":
            print("Recording... \nPress Esc to stop recording")
            record()
        elif menu == "2":
            pass
        else:
            print("Incorrect Number. Please choose a number from the selection.")
            menu = input("Press 1 to record Keys: \nPress 2 to see recorded Keys: \n")

    

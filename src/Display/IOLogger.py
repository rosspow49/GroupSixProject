from src.Display.IO import IO

class IOLogger(IO):

    logToFile = True

    def __init__(self, logToFile):
        self.logToFile = logToFile

    def takeInput(self, message):
        command = input(message)
        if self.logToFile:
            with open("Logs/InputLog.txt", "a")as log:
                log.write(command + "\n")
        return command

    def showOutput(self, message):
        if self.logToFile:
            with open("Logs/OutputLog.txt", "a")as log:
                log.write(message + "\n")
        print(message)
class IOLogger():

    logToFile = True

    def __init__(self, logToFile=True):
        self.logToFile = logToFile

    def TakeInput(self, message):
        command = input(message)
        if self.logToFile:
            with open("Logs/InputLog.txt", "a")as log:
                log.write(command + ",")
        return command

    def ShowOutput(self, message):
        if self.logToFile:
            with open("Logs/OutputLog.txt", "a")as log:
                log.write(message + ",")
        print(message)
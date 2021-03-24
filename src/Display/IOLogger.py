class IOLogger():

    def TakeInput(self, message):
        command = input(message)
        with open("Logs/InputLog.txt", "a")as log:
            log.write(command + ",")
        return command

    def ShowOutput(self, message):
        with open("Logs/OutputLog.txt", "a")as log:
            log.write(message + ",")
        print(message)
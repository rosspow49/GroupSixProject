from src.Data.ReadLogFile import readLogFile
from src.Display.IO import IO

class IOTest(IO):

    inputList = []
    outputList = []

    def setInputList(self, inputList):
        self.inputList = inputList

    def takeInput(self, message):
        command = self.inputList.pop(0)
        return command

    def showOutput(self, message):
        self.outputList.append(message)

    def getInputList(self):
        return self.inputList

    def getOutputList(self):
        return self.outputList

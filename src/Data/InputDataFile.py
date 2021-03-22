import os
from src.Data.IDataInput import IDataInput

class InputDataFile(IDataInput):

    def setDirectoryPath(self, directoryPath):
        self.directoryPath = directoryPath

    def getRawData(self):
        rawData = os.listdir(self.directoryPath)
        return rawData
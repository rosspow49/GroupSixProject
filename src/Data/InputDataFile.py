import os
from src.Data.IDataInput import IDataInput

class InputDataFile(IDataInput):

    def getRawData(self, directoryPath):
        rawData = os.listdir(directoryPath)
        return rawData
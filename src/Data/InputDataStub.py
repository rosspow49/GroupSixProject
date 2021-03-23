import os
from src.Data.IDataInput import IDataInput

class InputDataStub(IDataInput):

    def getRawData(self, directoryPath):
        inputDirectory = os.path.dirname(__file__)
        rawData = os.listdir(inputDirectory + "/stubMusic")
        return rawData
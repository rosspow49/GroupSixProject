import os
from src.Data.IDataInput import IDataInput

class InputDataStub(IDataInput):

    def getRawData(self, directoryPath):
        rawData = os.listdir("testMusic")
        return rawData
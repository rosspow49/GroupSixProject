from src.Data.IDataInput import IDataInput

class InputDataStub(IDataInput):

    def setDirectoryPath(self, directoryPath):
        pass

    def getRawData(self):
        rawData = ["track1", "track2", "track3"]
        return rawData
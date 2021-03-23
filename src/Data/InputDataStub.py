from src.Data.IDataInput import IDataInput

class InputDataStub(IDataInput):

    def getRawData(self):
        rawData = ["track1", "track2", "track3"]
        return rawData
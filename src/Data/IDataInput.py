from abc import ABC as abstractBaseClass, abstractmethod


class IDataInput(abstractBaseClass):

    @abstractmethod
    def getRawData(self, directoryPath):
        pass

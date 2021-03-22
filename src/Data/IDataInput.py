from abc import ABC, abstractmethod


class IDataInput(ABC):
    directoryPath = None

    @abstractmethod
    def setDirectoryPath(self, directoryPath):
        pass

    @abstractmethod
    def getRawData(self):
        pass

from abc import ABC, abstractmethod


class IDataInput(ABC):

    @abstractmethod
    def getRawData(self, directoryPath):
        pass

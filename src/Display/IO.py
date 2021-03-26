from abc import ABC as abstractBaseClass, abstractmethod

class IO(abstractBaseClass):
    @abstractmethod
    def TakeInput(self, message):
        pass

    @abstractmethod
    def ShowOutput(self, message):
        pass
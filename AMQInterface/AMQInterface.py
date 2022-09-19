from abc import ABC, abstractmethod


class AMQInterface(ABC):

    @abstractmethod
    def sendPacket(self, msg):
        pass

    @abstractmethod
    def getPacket(self):
        pass

    
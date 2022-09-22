from abc import ABC, abstractmethod


class AMQInterface(ABC):

    @abstractmethod
    def sendPacket(self, msg):
        pass

    @abstractmethod
    def getPacket(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    
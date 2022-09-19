from AMQInterface.AMQInterface import AMQInterface
import stomp
from .MsgListener import MsgListener
import time

class MsgHandler(AMQInterface):
    def __init__(self, port, ipaddr, passwd, user):
        self._msg = ""
        self._port = port
        self._ipaddr = ipaddr
        self._passwd = passwd
        self._user = user

    def connect(self):
        con = stomp.Connection([(self._ipaddr, self._port)])
        listener = MsgListener()
        con.set_listener('name_of_listener', listener)
        con.connect(self._user, self._passwd, wait=True)
        return con

    def sendPacket(self, msg):
        conn = self.connect()
        conn.send(body=msg, destination='/queue/test')
        conn.disconnect()

    def getPacket(self):
        conn = self.connect()
        conn.subscribe(destination='/queue/test', id=1, ack='auto')
        conn.disconnect()

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
        self._conn = None

    def connect(self):
        self._conn = stomp.Connection([(self._ipaddr, self._port)])
        listener = MsgListener()
        self._conn.set_listener('name_of_listener', listener)
        self._conn.connect(self._user, self._passwd, wait=True)

    def is_connected(self):
        self._conn.is_connected()

    def sendPacket(self, msg):
        conn = self.connect()
        conn.send(body=msg, destination='/queue/test')

    def getPacket(self):
        conn = self.connect()
        conn.subscribe(destination='/queue/test', id=1, ack='auto')

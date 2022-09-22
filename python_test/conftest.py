import pytest
from Module.MsgHandler import MsgHandler

@pytest.fixture
def amq_config():
    port = 61613
    ipaddr = "127.0.0.1"
    passwd = "admin"
    user = "admin"

    amq = MsgHandler(port, ipaddr, passwd, user)
    amq.connect()

    return amq

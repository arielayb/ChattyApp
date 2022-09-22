import pytest
from .TestMsgListener import TestMsgListener

def test_MsgHandlerConnect(amq_config):
    assert amq_config.is_connected() == True








import stomp
import logger

class TestMsgListener(stomp.ConnectionListener):
    def __init__(self):
        # to keep the count of messages received
        self.msg_received = 0
        self.msg = None

    def on_error(self, frame):
        logger.error('received an error "%s"' % frame)

    def on_message(self, frame):
        self.msg = frame
        self.msg_received += 1
        # add your logic based on the message received here

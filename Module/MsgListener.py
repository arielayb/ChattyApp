import logger
import json
import stomp

class MsgListener(stomp.ConnectionListener):
    def __init__(self):
        # to keep the count of messages received
        self.msg_recieved = 0

    def on_error(self, message):
        logger.error('received an error "%s"' %message)

    def on_message(self, message):
        message = json.loads(message)
        self.msg_received +=1
        # add your logic based on the message received here
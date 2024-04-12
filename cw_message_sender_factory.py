from cw_message_sender import CWMessageSender
from radio_controller import RadioFactory

class CWMessageSenderFactory:
    @staticmethod
    def create_cw_message_senders():
        available_radios = RadioFactory.detect_radios()
        return [CWMessageSender(RadioFactory.create_radio(port)) for port in available_radios]

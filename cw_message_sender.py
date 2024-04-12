class CWMessageSender:

    def __init__(self, radio_controller):
        self.radio_controller = radio_controller

    def send_cw_message(self, message):
        self.radio_controller.send_command(f"KYR1;TX2;MN080;{message};MN255;KYR0;")

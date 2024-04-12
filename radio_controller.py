import serial.tools.list_ports
import time

class RadioController:
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port, 9600, timeout=1)

    def send_command(self, command):
        self.ser.write(command.encode())
        time.sleep(0.1)  # Wait for the radio to process the command

    def read_cw_signal(self):
        # Implement logic to read CW signal from the radio
        # For example, read from serial port and interpret Morse code
        cw_signal = self.ser.readline().decode().strip()  # Example assuming Morse code is sent over serial
        return cw_signal

    def close(self):
        self.ser.close()

class RadioFactory:
    @staticmethod
    def detect_radios():
        return [port.device for port in serial.tools.list_ports.comports() if 'Icom' in port.description]

    @staticmethod
    def create_radio(port):
        return RadioController(port)

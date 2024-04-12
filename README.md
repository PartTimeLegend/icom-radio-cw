# Icom Radio CW Message Sender

This Python project allows you to send and receive CW (Morse code) messages using Icom radios. The project consists of separate modules responsible for radio communication, sending CW messages, and factory methods for creating message senders.

## Project Structure

The project is structured into the following files:

- `radio_controller.py`: Contains the `RadioController` class responsible for communication with Icom radios via serial port. It also includes the `RadioFactory` class for detecting attached Icom radios and creating radio controller instances.
- `cw_message_sender.py`: Defines the `CWMessageSender` class, which is responsible for sending CW messages through an Icom radio.
- `cw_message_sender_factory.py`: Implements the `CWMessageSenderFactory` class, which creates instances of `CWMessageSender` for each detected Icom radio.
- `main.py`: The main script of the project. It utilizes the `CWMessageSenderFactory` to create message senders for all detected Icom radios and allows the user to send and receive CW messages interactively.

## Usage

1. Install the necessary dependencies by running `pip install -r requirements.txt`.
2. Ensure that your Icom radio is connected to the computer via a serial port.
3. Run the `main.py` script using Python: `python main.py`.
4. Follow the on-screen prompts to send and receive CW messages. Type `exit` to quit the program.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

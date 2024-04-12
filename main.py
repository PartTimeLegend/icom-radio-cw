from cw_message_sender_factory import CWMessageSenderFactory

if __name__ == "__main__":
    cw_senders = CWMessageSenderFactory.create_cw_message_senders()
    
    if cw_senders:
        try:
            while True:
                message = input("Enter CW message to send (or type 'exit' to quit): ")
                if message.lower() == 'exit':
                    break
                
                for cw_sender in cw_senders:
                    cw_sender.send_cw_message(message)
                    
                # Read CW signals
                for cw_sender in cw_senders:
                    cw_signal = cw_sender.radio_controller.read_cw_signal()
                    print("Received CW signal from", cw_sender.radio_controller.port, ":", cw_signal)
                    
        except KeyboardInterrupt:
            pass
        finally:
            for cw_sender in cw_senders:
                cw_sender.radio_controller.close()
    else:
        print("No Icom radios detected.")

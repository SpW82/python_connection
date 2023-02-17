
from socket import *
from termcolor import colored as col

class Client:

    """
    Demo client, sends message to the demo server.
    Runs on a loop until a keyboard interrupt is detected
    """

    @staticmethod
    def con(msg):

        with socket(AF_INET, SOCK_STREAM) as s:

            try:
                s.connect(('127.0.0.1', 12345))
                s.sendall(msg.encode())
                print(f"[{col('*', 'green')}] Message sent")
            except Exception as e:
                print(f"[{col('*', 'red')}] Error : {e}")
                s.close()

def main(*args):

    while True:
        msg = input(f"[{col('*', 'blue')}] Enter message:\n >>> ")

        if msg == 'exit_client()':
            exit(0)

        Client.con(msg)

if __name__ == "__main__":
    main()

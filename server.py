from socket import *
from termcolor import colored as col
from datetime import datetime

class Server:

    def __init__(self, port):

        self.port = port

    def start_server(self):

        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind(('', self.port))
            s.listen()
            print(f"{col('[*]', 'yellow')} Server listening on {self.port}")

            try:
                while True:
                    c, a = s.accept()
                    print(f"{col('[+]', 'green')} Connection from {a[0]} : {datetime.now()}")
                    data = c.recv(1024).decode()
                    print(f"{col('[+]', 'green')} {data}")

            except KeyboardInterrupt:
                print(f"{col('[-]', 'red')} Server shutting down")
                exit(0)


def main():
    server = Server(12345)
    server.start_server()


if __name__ == '__main__':
    main()

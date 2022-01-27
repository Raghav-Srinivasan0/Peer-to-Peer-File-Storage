from importlib.resources import path
import socket

from black import main


class Server:
    def __init__(
        self,
        host="127.0.0.1",
        port=5000,
        path="C:/Users/binad/Peer-To-Peer File Storage/Peer-to-Peer-File-Storage/Test Destination/",
    ):
        self.HOST = host
        self.PORT = port
        self.PATH = path

    def startserver(self, FILENAME=None):
        if FILENAME == None:
            FILENAME = str(input("What is the name of your file? "))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            # conn is a socket object and addr is a pair with (hostaddr, port)
            conn, addr = s.accept()
            with conn:
                # print('Connected to: ' + addr)
                type_of_file = str(conn.recv(1024)).replace("'", "").replace("b", "")
                file = open(self.PATH + FILENAME + type_of_file, "a+b")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)


if __name__ == "__main__":
    server = Server(
        host="192.168.1.3", port=5000, path="D:/Destination_For_File-Transfer/"
    )
    while True:
        server.startserver()

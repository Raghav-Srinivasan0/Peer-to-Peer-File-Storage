# from importlib.resources import path
import socket

# from black import main


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

    def startserver(self, filename, conn, addr):
        if filename == None:
            filename = str(input("What is the name of your file? "))
        with conn:
            # print('Connected to: ' + addr)
            type_of_file = str(conn.recv(1024)).replace("'", "").replace("b", "")
            file = open(self.PATH + filename + type_of_file, "a+b")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)

    def return_self(self):
        return self


if __name__ == "__main__":
    server = Server(
        host="localhost",
        # port=5000,
        path="D:/Destination_For_File-Transfer/",
    )
    while True:
        server.startserver(None)

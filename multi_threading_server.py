from socket_basic_server import Server
import threading
import socket

HOST = '127.0.0.1'
PORT = 5000
PATH = "C:/Users/binad/Peer-To-Peer File Storage/Peer-to-Peer-File-Storage/Test Destination/"

serverSocket = socket.socket();
serverSocket.bind((HOST, PORT));
serverSocket.listen();

while(True):
    (clientConnection, clientAddress) = serverSocket.accept();

    # Close the connection to the client
    s = Server()
    thread = threading.Thread(target=s.startserver, args=(str(threading.active_count()),None,None))
    thread.start()
    thread.run()

    clientConnection.close(); 
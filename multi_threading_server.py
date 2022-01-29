# from socket_basic_server import Server

# IMPORTANT: This code works for one run of the client code but the second time the client code runs it doesn't work

import threading
import socket

HOST = "localhost"
PORT = 5000
PATH = "D:/Destination_For_File-Transfer/"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))


def createandrun(filename):
    # server = Server(host=HOST, port=PORT, path=PATH)
    # server.startserver(name, c, a)
    s.listen()
    conn, addr = s.accept()
    if filename == None:
        filename = str(input("What is the name of your file? "))
    with conn:
        # print('Connected to: ' + addr)
        type_of_file = str(conn.recv(1024)).replace("'", "").replace("b", "")
        file = open(PATH + filename + type_of_file, "a+b")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)


while True:
    # Close the connection to the client
    thread = threading.Thread(
        target=createandrun,
        args=(str(threading.active_count()),),
    )
    thread.start()
    # error here
    thread.run()

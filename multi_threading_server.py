# from socket_basic_server import Server

# IMPORTANT: This code works for one run of the client code but the second time the client code runs it doesn't work

import multiprocessing
import socket
import sys
import string
import random

HOST = "localhost"
PORT = 5000
PATH = "D:/Destination_For_File-Transfer/"

all_processes = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))


def createandrun(filename, process_name):
    # server = Server(host=HOST, port=PORT, path=PATH)
    # server.startserver(name, c, a)
    s.listen()
    conn, addr = s.accept()
    if filename == None:
        filename = str(input("What is the name of your file? "))
    with conn:
        # print('Connected to: ' + addr)
        type_of_file = str(conn.recv(1024)).replace("'", "")[1:]
        file = open(PATH + filename + type_of_file, "a+b")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
    for process in all_processes:
        if process.name == process_name:
            process.kill()
    conn.close()


i = 1
while True:
    # Close the connection to the client
    print("Beginning of Loop")
    name = "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(50)
    )
    process = multiprocessing.Process(
        target=createandrun,
        args=(
            str(i),
            name,
        ),
        daemon=True,
        name=name,
    )
    process.start()
    all_processes.append(process)
    for p in all_processes:
        print(p.name)
    process.run()
    print("end of run")
    i += 1

# from socket_basic_server import Server

# IMPORTANT: This code works for one run of the client code but the second time the client code runs it doesn't work

import multiprocessing
from multiprocessing import Process
import socket
import sys
import string
import random

from black import main

HOST = socket.gethostbyname(socket.gethostname())
port_range = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008]
PATH = "D:/Destination_For_File-Transfer/"

all_processes = []


def find_port():
    for port in port_range:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if data == bytes("ready"):
                    return port
        except Exception:
            pass
    return None


def createandrun(filename, process_name, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    conn, addr = s.accept()
    # server = Server(host=HOST, port=PORT, path=PATH)
    # server.startserver(name, c, a)
    # not getting here
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
    # Dont get here
    for process in all_processes:
        print("%s,%s", process.name, process_name)
        if process.name == process_name:
            process.kill()
    conn.close()
    s.close()


def main_function(port):
    # Close the connection to the client
    print("Beginning of Loop")
    name = "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(50)
    )
    process = Process(
        target=createandrun,
        args=(name, name, port),
        daemon=True,
        name=name,
    )
    # process.start()
    all_processes.append(process)
    for p in all_processes:
        print(p.name)
    # program gets here and then errors
    process.start()
    process.join()
    print("end of run")


if __name__ == "__main__":
    while True:
        port = find_port()
        print(port)
        if port == None:
            pass
        else:
            main_function(port)

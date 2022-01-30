# from socket_basic_server import Server

# IMPORTANT: This code works for one run of the client code but the second time the client code runs it doesn't work

import multiprocessing
from multiprocessing import Process
import socket
import sys
import string
import random
import argparse

# from black import main

my_parser = argparse.ArgumentParser(description="Start the server")

my_parser.add_argument("PORT", metavar="port", type=int, help="The port")
my_parser.add_argument(
    "NUMCONN",
    metavar="number_of_connections",
    type=int,
    help="The number of connections",
)
my_parser.add_argument("PATH", metavar="path", type=str, help="The destination path")

args = my_parser.parse_args()

HOST = socket.gethostbyname(socket.gethostname())
PORT = args.PORT
if args.PATH == "None":
    PATH = "D:/Destination_For_File-Transfer/"
else:
    PATH = args.PATH

all_processes = []


def createandrun(filename, process_name, conn, addr):
    # server = Server(host=HOST, port=PORT, path=PATH)
    # server.startserver(name, c, a)
    # not getting here
    if filename == None:
        filename = str(input("What is the name of your file? "))
    with conn:
        print("Connected to: " + addr)
        type_of_file = str(conn.recv(1024)).replace("'", "")[1:]
        file = open(PATH + filename + type_of_file, "a+b")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
    # Dont get here
    print("leaving connection 2")
    conn.close()
    s.close()


def main_function(conn, addr):
    # Close the connection to the client
    print("Beginning of Loop")
    name = "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(50)
    )
    process = Process(
        target=createandrun,
        args=(
            name,
            name,
            conn,
            addr,
        ),
        daemon=False,
        name=name,
    )
    # process.start()
    all_processes.append(process)
    # for p in all_processes:
    #    print(p.name)
    # program gets here and then errors
    print("end of run")


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(args.NUMCONN)
    try:
        conn, addr = s.accept()
    except Exception as e:
        print(e)
        return
    print(s)
    for i in range(args.NUMCONN):
        main_function(conn, addr)
        print(all_processes)
    for process in all_processes:
        process.start()
        process.join()

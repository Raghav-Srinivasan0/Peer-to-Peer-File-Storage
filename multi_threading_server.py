# from socket_basic_server import Server

# IMPORTANT: This code works for one run of the client code but the second time the client code runs it doesn't work

from multiprocessing import Process
import socket
import string
import random
import argparse
from unicodedata import name

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

HOST = 'localhost'
#socket.gethostbyname(socket.gethostname())
PORT = args.PORT
if args.PATH == "None":
    PATH = "D:/Destination_For_File-Transfer/"
else:
    PATH = args.PATH

all_processes = []

sending = False


def createandrun(filename, conn, addr):
    # server = Server(host=HOST, port=PORT, path=PATH)
    # server.startserver(name, c, a)
    # not getting here
    #print(filename)
    if filename == None:
        filename = str(input("What is the name of your file? "))
    with conn:
        file_str = PATH + filename
        try:
            file = open(file_str[: file_str.index("**END**")] + '.data', "a+b")
            overflow = file_str[file_str.index("**END**") + 7 :]
            file.write(overflow.encode())
        except Exception as e:
            file = open(file_str + '.data', "a+b")
        while True:
            if not sending:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
    # Dont get here
    # print("leaving connection 2")


def main_function(conn, addr, name):
    # Close the connection to the client
    # print("Beginning of Loop")
    process = Process(
        target=createandrun,
        args=(
            name,
            conn,
            addr,
        ),
        daemon=False,
        name=name,
    )
    # process.start()
    all_processes.append(process)
    process.start()
    process.join()
    # for p in all_processes:
    #print(process.name)
    # program gets here and then errors
    # print("end of run")


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(args.NUMCONN)
    while True:
        try:
            conn, addr = s.accept()
            # print("Connected to: " + addr)
        except Exception as e:
            #print(e)
            pass
        recieved = str(conn.recv(1024))
        for i in range(args.NUMCONN):
            #print(recieved)
            filename = main_function(conn, addr, recieved[1:].replace("'", ""))
            # print(all_processes)

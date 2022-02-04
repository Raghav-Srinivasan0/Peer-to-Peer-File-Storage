from multiprocessing import Process
import socket
import argparse
from unicodedata import name

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

HOST = "localhost"

PORT = args.PORT
if args.PATH == "None":
    PATH = "D:/Destination_For_File-Transfer/"
else:
    PATH = args.PATH

all_processes = []

sending = False


def createandrun(filename, conn, addr):
    if filename == None:
        filename = str(input("What is the name of your file? "))
    with conn:
        file_str = PATH + filename
        if not file_str.find("**SEND**") == -1:
            sending = True
        else:
            sending = False
        if not sending:
            try:
                file = open(file_str[: file_str.index("**END**")] + ".data", "a+b")
                overflow = file_str[file_str.index("**END**") + 7 :]
                file.write(overflow.encode())
            except Exception as e:
                file = open(file_str + ".data", "a+b")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
        else:
            file = open(
                file_str[: file_str.index("**SEND**")]
                + file_str[file_str.index("**SEND**") + 8 :]
                + ".data",
                "r+",
            )
            for line in file.readlines():
                conn.sendall(line.encode())


def main_function(conn, addr, name):
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
    all_processes.append(process)
    process.start()
    process.join()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(args.NUMCONN)
    while True:
        try:
            conn, addr = s.accept()
        except Exception as e:
            pass
        recieved = str(conn.recv(1024))
        for i in range(args.NUMCONN):
            filename = main_function(conn, addr, recieved[1:].replace("'", ""))

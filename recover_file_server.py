import argparse
from multiprocessing import Process
import socket

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


PATH = args.PATH
HOST = socket.gethostbyname(socket.gethostname())
PORT = args.PORT
NUMCONN = args.NUMCONN

all_processes = []

def main_function(conn):
    print("start of process")
    with conn:
        data = conn.recv(1024)
        if not str(data).find('**SEND**') == -1:
            filename = str(data)[str(data).find('**SEND**')+8:]
    try:
        print(filename)
    except Exception as e:
        pass

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    print("listening ...")
    s.listen(NUMCONN)
    while True:
        try:
            conn, addr = s.accept()
        except Exception as e:
            pass
        for i in range(NUMCONN):
            process = Process(target=main_function, args=(conn,), daemon=False)
            all_processes.append(process)
            process.start()
            process.join()


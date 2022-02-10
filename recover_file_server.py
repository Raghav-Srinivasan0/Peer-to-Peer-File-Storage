from multiprocessing import Process
import multiprocessing
import socket

PATH = "D:/Destination_For_File-Transfer/"
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
NUMCONN = 5


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
print("listening ...")
s.listen(NUMCONN)

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

while True:
    try:
        conn, addr = s.accept()
    except Exception as e:
        pass
    for i in range(NUMCONN):
        process = Process(target=main_function, args=(conn,), daemon=False)
        process.start()
        process.join()


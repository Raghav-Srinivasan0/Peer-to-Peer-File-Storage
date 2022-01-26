import socket

HOST = '127.0.0.1'
PORT = 5000
PATH = f"C:/Users/binad/Peer-To-Peer File Storage/Peer-to-Peer-File-Storage/Test Destination/"
FILENAME = input("What is the name of your file? ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    #conn is a socket object and addr is a pair with (hostaddr, port)
    conn, addr = s.accept()
    with conn:
        #print('Connected to: ' + addr)
        type_of_file = str(conn.recv(1024)).replace("'","").replace("b","")
        file = open(PATH + FILENAME + type_of_file, "a+b")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
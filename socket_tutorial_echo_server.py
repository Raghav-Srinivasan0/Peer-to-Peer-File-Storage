import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    #conn is a socket object and addr is a pair with (hostaddr, port)
    conn, addr = s.accept()
    with conn:
        #print('Connected to: ' + addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
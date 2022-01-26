from dataclasses import Field
import socket
from open_file_dialogue_test import FileDialogue

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    f = FileDialogue()
    file_data = f.get_file_data()
    print(file_data)
    for i in range(len(file_data)):
        s.sendall(file_data[i])
    data = s.recv(1024)

print('Recieved', repr(data.decode()))
from dataclasses import Field
import socket
import os
from open_file_dialogue_test import FileDialogue

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes("ready"))
    f = FileDialogue()
    file_path = f.get_file_path()
    file_data = f.get_file_data()
    file_ext = f.get_file_ext()
    f.close()
    os.chdir("C:")
    os.remove(file_path)
    s.sendall(bytes(file_ext.encode()))
    for i in range(len(file_data)):
        s.sendall(file_data[i])

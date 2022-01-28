# IMPORTANT: Doesn't currently work as it cant connect to the server
# the client that currently does work is the one that is titled socket_original_client.py

from dataclasses import Field
import socket
import os
from open_file_dialogue_test import FileDialogue

class Client:
    def __init__(self, host='127.0.0.1', port=5000):
        self.HOST = host
        self.PORT = port
        f = FileDialogue()
        self.file_path = f.get_file_path()
        self.file_data = f.get_file_data()
        self.file_ext = f.get_file_ext()
        f.close()
        os.chdir('C:')
        os.remove(self.file_path)
    def send(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(bytes(self.file_ext.encode()))
            for i in range(len(self.file_data)):
                s.sendall(self.file_data[i])

if __name__ == "__main__":
    client = Client(
        host="localhost", 
        #port=5000, 
        #path="D:/Destination_For_File-Transfer/"
    )
    while True:
        client.send()
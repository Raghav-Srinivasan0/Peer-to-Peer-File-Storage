from dataclasses import Field
import socket
import os
from open_file_dialogue_test import FileDialogue

class Client:
    def __init__(self, host='127.0.0.1', port=5000):
        self.HOST = host
        self.PORT = port
    def send(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            f = FileDialogue()
            file_path = f.get_file_path()
            file_data = f.get_file_data()
            file_ext = f.get_file_ext()
            f.close()
            os.chdir('C:')
            os.remove(file_path)
            s.sendall(bytes(file_ext.encode()))
            for i in range(len(file_data)):
                s.sendall(file_data[i])

if __name__ == "__main__":
    client = Client(
        # host="192.168.1.3", 
        #port=5000, 
        #path="D:/Destination_For_File-Transfer/"
    )
    while True:
        client.send()
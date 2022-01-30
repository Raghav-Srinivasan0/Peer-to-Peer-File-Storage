from dataclasses import Field
import socket
import os
from open_file_dialogue_test import FileDialogue
import argparse

my_parser = argparse.ArgumentParser(description="Start the client")

my_parser.add_argument("PORT", metavar="port", type=int, help="The port")
my_parser.add_argument("HOST", metavar="host", type=str, help="The host")

args = my_parser.parse_args()

HOST = args.HOST
PORT = args.PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
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

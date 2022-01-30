from dataclasses import Field
import socket
import os
from open_file_dialogue_test import FileDialogue
import argparse

my_parser = argparse.ArgumentParser(description="Start the client")

my_parser.add_argument("PORT", metavar="port", type=int, help="The port")
# my_parser.add_argument("HOST", metavar="host", type=str, help="The host")

args = my_parser.parse_args()

hosts = ["192.168.1.3", "192.168.1.43"]

# HOST = args.HOST
PORT = args.PORT

f = FileDialogue()
file_path = f.get_file_path()
file_data = f.get_file_data()
file_ext = f.get_file_ext()
print(file_ext)
f.close()
os.chdir("C:")
os.remove(file_path)
with open(file_path[: file_path.rindex(".")] + ".ins", "a+") as file:
    file.write("PORT: {port}\nHOSTS: {hosts}".format(port=PORT, hosts=hosts))

for host in range(len(hosts)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((hosts[host], PORT))
        a = file_ext + "**END**"
        s.sendall(bytes(a.encode()))
        for i in range(len(file_data)):
            if i % len(hosts) == host:
                print(file_data[i])
                s.sendall(file_data[i])

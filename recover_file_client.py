import socket
import sys
from open_file_dialogue_test import FileDialogue

# get instruction file
path = ""
while path.find('.ins')==-1:
    try:
        f = FileDialogue()
        data = f.get_file_data()
        ext = f.get_file_ext()
        path = f.get_file_path()
        f.close()
    except FileNotFoundError:
        print('Pick a file!')
        pass

port = -1
hosts = []

with open(path,'r+') as f:
    data = f.readlines()
    for line in range(len(data)):
        if data[line].startswith('PORT: '):
            port = int(data[line][data[line].index(' ')+1:])
        if data[line].startswith('HOSTS: '):
            list_str = data[line][data[line].index(' ')+1:].replace('[','').replace(']','').replace('\'','')
            list_init = list_str.split(',')
            hosts = list_init

print(port)
print(hosts)

for host in range(len(hosts)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((hosts[host],port))
        except Exception as e:
            print("Quitting because: " + e)
            sys.exit(1)
        

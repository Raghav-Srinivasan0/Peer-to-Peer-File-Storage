import socket
from open_file_dialogue_test import FileDialogue

# get instruction file
f = FileDialogue()
data = f.get_file_data()
ext = f.get_file_ext()
path = f.get_file_path()
f.close()

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


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

data_arr = []

for host in range(len(hosts)):
    arr = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            try:
                s.connect((
                    #hosts[host],
                    socket.gethostbyname(socket.gethostname()),
                    port
                    ))
                break
            except Exception as e:
                print("Quitting because: " + str(e))
                pass
        try:
            index_of_slash = path.rindex('/')
        except Exception as e:
            index_of_slash = path.rindex('\\')
        file_name = path[index_of_slash+1:].replace(ext,'')
        s.sendall(('**SEND**' + file_name).encode())
        '''
        s.bind((str(hosts[host]),port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
        '''
        while True:
            data = s.recv(1024)
            if not data:
                break
            arr.append(data)
    data_arr.append(arr)

print(data_arr)
        

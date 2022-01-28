from socket_basic_server import Server
import threading

HOST='localhost'
PORT=5000
PATH="C:/Users/binad/Peer-To-Peer File Storage/Peer-to-Peer-File-Storage/Test Destination/"

def createandrun(filename):
    server = Server(host=HOST,port=PORT,path=PATH)
    server.startserver(filename=filename)

while(True):
    # Close the connection to the client
    thread = threading.Thread(target=createandrun, args=(str(threading.active_count()),))
    thread.start()
    thread.run()
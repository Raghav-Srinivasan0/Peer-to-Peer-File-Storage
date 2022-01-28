from socket_basic_server import Server
import threading

while(True):
    # Close the connection to the client
    thread = threading.Thread(target=Server.startserver, args=(str(threading.active_count())))
    thread.start()
    thread.run()
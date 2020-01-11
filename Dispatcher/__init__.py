import socket
from Dispatcher.library import logg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("192.168.0.102", 9999))
s.listen()

while True:
    nachricht = s.recv(1024)
    s.close()
    print(nachricht.decode("ascii"))

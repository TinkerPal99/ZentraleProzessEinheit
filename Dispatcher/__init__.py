import socket
from Dispatcher.library import logg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9989))
s.listen()
connection = False

while True:
    client, adresse = s.accept()
    logg.logging.info("Verbunden mit " + adresse)
    nachricht = "Hello World".encode("ascii")
    client.send(nachricht)
    client.close()

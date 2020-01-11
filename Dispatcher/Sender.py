import socket
from Dispatcher.library import logg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.102", 9999))

while True:
    client, adresse = s.accept()
    logg.logging.info("Verbunden zu " + str(adresse))
    client.send("Hello World".encode("ascii"))
    client.close()
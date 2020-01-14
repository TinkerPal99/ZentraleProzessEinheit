import socket
from Dispatcher.logs_ import logg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adresse = '192.168.0.104'

try:
    s.connect((adresse, 1200))
except ConnectionRefusedError:
    logg.logging.warning("Connection Refused", exc_info=True)
    SystemExit(2)
except OSError:
    logg.logging.critical("Servererror", exc_info=True)
    SystemExit(2)
logg.logging.info("Verbunden mit " + str(adresse))
message = s.recv(1024)
print(message.decode("ascii"))


nachricht = "Copy.xml".encode("ascii")
s.send(nachricht)
nachricht = "fgzhjbgzujhuikn".encode("ascii")
s.send(nachricht)
s.close()


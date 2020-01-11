import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.102", 9989))

# logg.logging.info("Verbunden zu " + str(adresse))
message = s.recv(1024)
s.close()
print(message.decode("ascii"))

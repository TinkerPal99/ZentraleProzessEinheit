import socket
from library import logg

s = socket.socket()
host = '192.168.0.104'
port = 1200

s.bind((host, port))
s.listen()
connection = False

while True:
    while True:
        client, adresse = s.accept()
        logg.logging.info("Verbunden mit " + str(adresse))
        connection = True

        if connection:
            nachricht = "Connection to EZB-Dispatcher established.".encode("ascii")
            client.send(nachricht)

# first get the file to send to
            message = client.recv(1024)
            message = message.decode("ascii")
            file = str(message)

# then the informations
            message = client.recv(1024)
            logg.logging.info("Write to " + file + " | " +str(message))
            message = str(message.decode("ascii"))

            client.close()
            break

    file = open('/var/www/html/' + str(file),"w")
    file.write(message)
    file.close()

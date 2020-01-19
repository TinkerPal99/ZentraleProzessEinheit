from Dispatcher.library import Priorisator, job
import socket

import logging
import sys

# ---------------------------logger-------------------------------------------------------------------------------------
logging.basicConfig(
    filename="logs\dispatcher_log.log",
    filemode="a",
    format="%(asctime)s|%(process)d||%(levelname)s|-|%(message)s")

# Ausgabe auf terminal
__log_handler = logging.StreamHandler(sys.stdout)

__logger = logging.getLogger()
__logger.addHandler(__log_handler)
__logger.setLevel(logging.DEBUG)
logging.info("________________________________________________________________________________________________________")
logging.info("Logged and loaded.")
# ----------------------------------------------------------------------------------------------------------------------

request_dispatcher = Priorisator.Priorisator()

s = socket.socket()
host = '192.168.0.104'
port = 9900
client = None
adress = None


def is_connected():
    # @is_connected scannt ob gerät ich verbinden will, akzeptiert dieses. Sendet bestätigung an verbinder
    global client, adress

    while True:
        client, adress = s.accept()
        if adress != "":
            nachricht = "Connection to EZB-Priorisator established.".encode("ascii")
            logging.info("Connected to " + str(adress))
            client.send(nachricht)
            return True


def receive_request():
    # empfängt jobpaket und steckt es in die queue
    newJob = job.job()
    newJob.sync(client.recv(1024))
    request_dispatcher.put(newJob)
    request_dispatcher.organize()
    logging.info("Received packet from " + str(adress))


def sendjob():
    # nimmt job mit der höchsten Prio aus der joblist und sendet ihn an den Wagen der in der Destination angegeben ist
    s_dest = socket.socket()
    job_item = request_dispatcher.get()
    destination_host = job_item["Destination"]
    destination_port = 9000
    logging.info("Sending job to " + str(destination_host))
    try:
        s_dest.connect((destination_host, destination_port))
        s.send(job_item.encode("ascii"))
    except ConnectionRefusedError:
        logging.warning("Connection Refused", exc_info=True)
        SystemExit(2)
    except OSError:
        logging.critical("Servererror", exc_info=True)
        SystemExit(2)
    else:
        logging.info("Send!")


while True:
    if is_connected():
        receive_request()
        sendjob()

from library import Priorisator, job
import socket

import logging
import sys

# ---------------------------logger-------------------------------------------------------------------------------------
logging.basicConfig(
    filename="dispatcher_log.log",
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

s.bind((host, port))
s.listen()
adress = None
client = None


def __is_connected():
    # @is_connected scannt ob geraet sich verbinden will, akzeptiert dieses. Sendet bestaetigung an verbinder
    global adress, client

    while True:
        client, adress = s.accept()
        if adress is None:
            nachricht = "Connection to EZB-Priorisator established.".encode("ascii")
            logging.info("Connected to " + str(adress))
            try:
                client.send(nachricht)
            except ConnectionAbortedError:
                logging.error("Connection was aborted", exc_info=True)
            except ConnectionError and ConnectionRefusedError:
                logging.error("ConnectionError", exc_info=True)
            else:
                logging.info("Build connection to " + adress)
                return True
        else:
            return False



def __receive_request():
    # empfängt jobpaket und steckt es in die queue
    newJob = job.job()
    request_dispatcher.put(newJob.sync(client.recv(1024)))
    request_dispatcher.organize()
    logging.info("Received packet from " + str(adress))


def __sendjob():
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
    except ConnectionError and ConnectionAbortedError:
        logging.error("ConnectionError", exc_info=True)
    except OSError:
        logging.critical("Servererror", exc_info=True)
        SystemExit(2)
    else:
        logging.info("Send!")


while True:
    if __is_connected():
        __receive_request()
        __sendjob()

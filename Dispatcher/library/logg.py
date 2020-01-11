import logging
import sys

logging.basicConfig(
    filename="library\logs\Server.log",
    filemode="a",
    format="%(asctime)s|%(process)d||%(levelname)s|-|%(message)s")

# Ausgabe auf terminal
__log_handler = logging.StreamHandler(sys.stdout)

__logger = logging.getLogger()
__logger.addHandler(__log_handler)
__logger.setLevel(logging.DEBUG)
logging.info("________________________________________________________________________________________________________")
logging.info("Logged and loaded.")

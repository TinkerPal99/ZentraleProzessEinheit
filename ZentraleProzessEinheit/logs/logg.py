import logging
import sys

logging.basicConfig(
        filename="ZentraleProzessEinheit/logs/Run.log",
        filemode="a",
        format="%(asctime)s|%(process)d||%(levelname)s|-|%(message)s")

# Ausgabe auf terminal
__log_handler = logging.StreamHandler(sys.stdout)

__logger = logging.getLogger()
__logger.addHandler(__log_handler)
__logger.setLevel(logging.DEBUG)
logging.info(
    "________________________________________________________________________________________________________")
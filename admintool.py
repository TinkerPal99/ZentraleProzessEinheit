from ZentraleProzessEinheit.library import Windows
from ZentraleProzessEinheit.logs import logg

try:
    logg.logging.info("Running Admintool for PyDrone")
    run = Windows.MainWin()
    if run.build():
        run.root.mainloop()
    else:
        raise RuntimeError
except IOError:
    logg.logging.debug("IOError occured in main", exc_info=True)
    Windows.Errorhandling()
except ValueError:
    logg.logging.debug("ValueError occured in main", exc_info=True)
    Windows.Errorhandling()
except TypeError:
    logg.logging.debug("TypeError occured in main", exc_info=True)
    Windows.Errorhandling()
except UnboundLocalError:
    logg.logging.critical("False input error occured", exc_info=True)
    print("Wrong Vehicleaddress.")
except NameError:
    logg.logging.debug("TypeError occured in main", exc_info=True)
    Windows.Errorhandling()
except RuntimeError:
    Windows.Errorhandling()
    logg.logging.critical("Build was not sucessful. Major error.")
else:
    pass
finally:
    SystemExit(0)

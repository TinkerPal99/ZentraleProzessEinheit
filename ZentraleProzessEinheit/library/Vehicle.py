import shutil
from urllib.request import *
import xml.etree.cElementTree as xmlparser
from random import randint
from urllib import request
import requests


class Vehicle:

    def __init__(self, url=str):
        # consructor, zieht daten von weburl wenn angegeben, sonst werden daten von temp gezogen
        self.url = url
        self.temp = "xml/temporary.xml"  # "library/xml/temporary.xml"

        if url == "":
            raise FileNotFoundError

        urlretrieve(url, self.temp)

        self.web = True

        self.tree = xmlparser.parse(self.temp)

        self.attributes = {"Name": None,
                           "Status": None,
                           "URL": None,
                           "Passcode": None,
                           "JOL": None,
                           "FW": None,
                           "BW": None}

        self.root = self.tree.getroot()

        for Name in self.root.iter("Name"):
            self.attributes["Name"] = Name.text  # TODO Get name from webxml (get)
        for Status in self.root.iter("Status"):
            self.attributes["Status"] = Status.text  # TODO Get Status from webxml (get)
        for URL in self.root.iter("JobUrl"):
            self.attributes["URL"] = URL.text
        for Passcode in self.root.iter("Adminpasscode"):
            self.attributes["Passcode"] = Passcode.text
        for License in self.root.iter("JOL"):
            self.attributes["JOL"] = License.text
        for FW in self.root.iter("FW"):
            self.attributes["FW"] = FW.text
        for BW in self.root.iter("BW"):
            self.attributes["BW"] = BW.text

    def save_changes(self):
        for Name in self.root.iter("Name"):
            Name.text = self.attributes["Name"]
        for Status in self.root.iter("Status"):
            Status.text = self.attributes["Status"]
        for URL in self.root.iter("JobUrl"):
            URL.text = self.attributes["URL"]
        for FW in self.root.iter("FW"):
            FW.text = self.attributes["FW"]
        for BW in self.root.iter("BW"):
            BW.text = self.attributes["BW"]
        self.tree.write(self.temp)

        if self.web:
            uploadfile = {"file": open(self.temp, "rb")}
            print(requests.put(self.url, uploadfile).reason + "Upload wasn't possible. Feature is momentarily not "
                                                              "supported.")

    def getattribute(self, attributename):
        try:
            return self.attributes.get(attributename)
        except AssertionError:
            # NOTE Assert wurde enferrnt, !Sicherheitsbedenken!
            print("You are not allowed to ask for this attribute.")
            SystemExit(1)

    def __copy__(self, copypath=str):
        # überladene copymethode, erstellt eine kopie in die übergebene xml (xml nach Vorlage), gibt werte der copy aus

        # "library/xml/Vorlage.xml"
        shutil.copy(str(self.save), str(copypath))

        tree = xmlparser.parse(copypath)
        root = tree.getroot()

        copy = self
        copy.attributes["Name"] = self.attributes["Name"] + "-Copy"
        copy.attributes["Status"] = "Deactivated"
        copy.attributes["URL"] = "TBD"
        copy.attributes["Passcode"] = str(randint(0, 9999)) + " " + str(randint(0, 9999))

        for Name in root.iter("Name"):
            Name.text = copy.attributes["Name"]  # TODO Get name from webxml (get)
        for Status in root.iter("Status"):
            Status.text = copy.attributes["Status"]  # TODO Get Status from webxml (get)
        for URL in root.iter("JobUrl"):
            URL.text = copy.attributes["URL"]
        for passcode in root.iter("Adminpasscode"):
            passcode.text = copy.attributes["Passcode"]
        for License in self.root.iter("JOL"):
            License.text = copy.attributes["JOL"]
        for FW in root.iter("FW"):
            FW.text = copy.attributes["FW"]
        for BW in root.iter("BW"):
            BW.text = copy.attributes["BW"]

        tree.write(copypath)
        print("Copy was made to " + copypath + " Ask a administrator to upload your new car.")
        return copy

    def __str__(self):
        # überladene string methode, definiert welcher wert bei str(self) zurückgegeben wird
        return str(self.attributes)

    def call_for_movement(self, movement):
        print("Vehicle " + str(self.attributes.get("Name")))
        if movement == 100:
            print(" -> Move forward.")
            # TODO Call for forward
        if movement == 101:
            print(" -> Move right.")
            # TODO Call for right
        if movement == 110:
            print(" -> Move left.")
            # TODO Call for left
        if movement == 111:
            print(" -> Move Backward.")
            # TODO Call for backward
        if movement == 000:
            print(" -> Carstop.")
            # TODO Call for stop


def __test_method():
    sim = Vehicle("http://192.168.0.102/Copy.xml")
    sim.attributes["Name"] = "newName"
    print(open(sim.temp, "rb"))
    sim.save_changes()


########################################
print("Vehiclemodule loaded properly")
########################################



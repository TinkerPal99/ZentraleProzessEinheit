import xml.etree.cElementTree as xmlparser


class Vehicle:
    def __init__(self, loadurl=str):
        self.save = loadurl
        self.attributes = {"Name": None,
                           "Status": None,
                           "URL": None,
                           "Passcode": None,
                           "JOL": None,
                           "FW": None,
                           "BW": None}

        self.tree = xmlparser.parse(loadurl)
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
            Name.text = self.attributes["Name"]  # TODO Get name from webxml (get)
        for Status in self.root.iter("Status"):
            Status.text = self.attributes["Status"]  # TODO Get Status from webxml (get)
        for URL in self.root.iter("JobUrl"):
            URL.text = self.attributes["URL"]
        for FW in self.root.iter("FW"):
            FW.text = self.attributes["FW"]
        for BW in self.root.iter("BW"):
            BW.text = self.attributes["BW"]
        self.tree.write(self.save)

    def getattribute(self, attributename):
        try:
            return self.attributes.get(attributename)
        except AssertionError:
            # NOTE Assert wurde enferrnt, !Sicherheitsbedenken!
            print("You are not allowed to ask for this attribute.")
            SystemExit(1)

    def __copy__(self, path):
        # überladene copymethode, erstellt eine kopie in die übergebene xml (xml nach Vorlage), gibt werte der copy aus

        # "library/xml/Vorlage.xml"
        tree = xmlparser.parse(path)
        root = tree.getroot()

        copy = self
        copy.attributes["Name"] = self.attributes["Name"] + "-Copy"
        copy.attributes["Status"] = "Deactivated"
        copy.attributes["URL"] = "TBD"
        copy.attributes["Passcode"] = "1234 5678"

        for Name in root.iter("Name"):
            Name.text = copy.attributes["Name"]  # TODO Get name from webxml (get)
        for Status in root.iter("Status"):
            Status.text = copy.attributes["Status"]  # TODO Get Status from webxml (get)
        for URL in root.iter("JobUrl"):
            URL.text = copy.attributes["URL"]
        for License in self.root.iter("JOL"):
            License.text = copy.attributes["JOL"]
        for FW in root.iter("FW"):
            FW.text = copy.attributes["FW"]
        for BW in root.iter("BW"):
            BW.text = copy.attributes["BW"]

        tree.write(path)
        print("Copy was made to " + path)
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
    sim = Vehicle("xml/PiTank.xml")
    print(str(sim))
    sua = sim.__copy__("xml/Vorlage.xml")
    print(str(sua))


########################################
print("Vehiclemodule loaded properly")
########################################




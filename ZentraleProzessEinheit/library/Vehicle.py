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

    def __get__(self):
        for attribute in self.attributes:
            print(attribute + " : " + self.attributes.get(attribute))

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
    print(sim.attributes["FW"])
    print(sim.attributes["JOL"])


########################################
print("Vehiclemodule loaded properly")
########################################



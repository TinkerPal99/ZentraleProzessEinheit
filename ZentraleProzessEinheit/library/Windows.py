from tkinter import *

from ZentraleProzessEinheit.library import Vehicle, logg


def Errorhandling():
    Error = Tk()
    __Error = Label(Error,
                    text="An Error occured. Please check the log.",
                    font="Times, 30",
                    fg="red")
    __Error.grid()
    __Error.mainloop()


class MainWin:

    def __init__(self):
        self.root = Tk()
        self.root.configure(background='darkred')
        self.__Title = "ZentraleProzessEinheit - Admintool 2.3"

        self.vehicle = Vehicle.Vehicle
        self.Vehicle_name = StringVar()
        self.Vehicle_status = StringVar()
        self.appout = StringVar()

        self.Vehicle_status.set("---")
        self.Vehicle_name.set("---")
        self.appout.set("Application started. Please choose your Vehicle.")

        self.returncode = 0
        # returncode tells, which action was made, 0 -> none

        self.__Headline = Label(self.root,
                                # compound=RIGHT,
                                padx=50,
                                width=46,
                                justify=LEFT,
                                text=self.__Title,
                                font="Times, 25")

        self.__explanator = Label(self.root,
                                  width=40,
                                  # height=20,
                                  borderwidth=5,
                                  relief="groove",
                                  text="Enter Vehicleadress here: ",  # TODO Dropdownlist
                                  font="Times, 15")
        self.__input_Vehicle = Entry(self.root,
                                     width=47,
                                     # height=20,
                                     borderwidth=5,
                                     relief="sunken",
                                     text="Test",
                                     font="Times, 15")

        self.__VehicleIdent = Label(self.root,
                                    width=19,
                                    height=2,
                                    borderwidth=5,
                                    relief="groove",
                                    text="Vehicleident:  ",
                                    font="Times, 15")
        self.__VehicleStatus = Label(self.root,
                                     width=19,
                                     height=2,
                                     borderwidth=5,
                                     relief="groove",
                                     text="Vehicestatus: ",
                                     font="Times, 15")
        self.__VStatus = Label(self.root,
                               width=19,
                               height=2,
                               borderwidth=5,
                               relief="groove",
                               textvariable=self.Vehicle_status,
                               font="Times, 15")
        self.__VIdent = Label(self.root,
                              width=19,
                              height=2,
                              borderwidth=5,
                              relief="groove",
                              textvariable=self.Vehicle_name,
                              font="Times, 15")
        self.__Textoutput = Label(self.root,
                                  width=68,
                                  height=8,
                                  borderwidth=6,
                                  relief="groove",
                                  textvariable=self.appout,
                                  font="Times, 15"
                                  )

        self.__Adminunit_Button = Button(self.root,
                                         text="Button \n Admin",
                                         command=self.__onclick_A,
                                         width=30,
                                         height=4,
                                         )
        self.__Controlunit_Button = Button(self.root,
                                           text="Button \n Control",
                                           command=self.__onclick_C,
                                           width=30,
                                           height=4)

        # TODO Bug-0002 User aendert ueber die Adminkonttrollen den Zustand des Wagens. Danach kehrt er zum rootframe
        #  zurueck. Dort wird der wagen immernoch im urspruenglichen Zustand angezeigt. Erwartet wird,
        #  dass der Zutand aktualisiert angezeigt wird.

    def __onReturn(self, event):
        try:
            output = self.__input_Vehicle.get()
            self.vehicle = Vehicle.Vehicle(output)
            self.Vehicle_status.set(self.vehicle.getattribute("Status"))
            self.Vehicle_name.set(self.vehicle.getattribute("Name"))

            logg.logging.info(
                "Loaded Vehicle " + self.vehicle.getattribute("Name") + " | Status " + self.vehicle.getattribute(
                    "Status")
                + " " + output)
            self.appout.set("Choose " + self.vehicle.getattribute("Name") + " from " + str(self.__input_Vehicle.get()))
        except FileNotFoundError:
            logg.logging.warning("File '" + self.__input_Vehicle.get() + "' user searched for was not found.")
            self.appout.set("File not found.")
        else:
            if self.vehicle.getattribute("Status") == "Ready":
                self.__Controlunit_Button.grid(row=2, column=2, rowspan=2)
            else:
                self.appout.set("Choose " + self.vehicle.getattribute("Name") + " from " + str(
                    self.__input_Vehicle.get()) + "\n" + "This vehicle is deactivated.")
                self.__Controlunit_Button.grid_remove()

            if self.vehicle.getattribute("JOL") == "True":
                self.__Adminunit_Button.grid(row=2, column=3, rowspan=2)
            else:
                self.appout.set("Choose " + self.vehicle.getattribute("Name") + " from " + str(
                    self.__input_Vehicle.get()) + "\n" + "This vehicle isn't jol'able.")
                self.__Adminunit_Button.grid_remove()

    def __onclick_A(self):
        adminwin = AdminWin(self)
        adminwin.build_gate()
        logg.logging.info("Call for Adminwindow")

    def __onclick_C(self):
        ctrlwin = ControlWin(self)
        ctrlwin.build()
        logg.logging.info("Call for Controlwindow")

    def __onDestroy(self):
        logg.logging.info("User killed window.")
        self.root.destroy()

    def build(self):
        self.__Headline.grid(row=0, columnspan=4)
        # Vehiclemenue
        self.__explanator.grid(row=1, column=0, columnspan=2)
        self.__input_Vehicle.grid(row=1, column=2, columnspan=3)
        # VehicleData
        self.__VehicleIdent.grid(row=3, column=0)
        self.__VehicleStatus.grid(row=2, column=0)
        self.__VStatus.grid(row=2, column=1)
        self.__VIdent.grid(row=3, column=1)
        self.__Textoutput.grid(row=4, rowspan=2, column=0, columnspan=3)

        try:
            self.root.protocol("WM_DELETE_WINDOW", self.__onDestroy)
            self.root.bind('<Return>', self.__onReturn)
            self.root.geometry("975x415")
            logg.logging.info("GUI initialized")
        except IOError:
            self.root.destroy()
            logg.logging.debug("IOError occured in main", exc_info=True)
            Errorhandling()
        except ValueError:
            self.root.destroy()
            logg.logging.debug("ValueError occured in main", exc_info=True)
            Errorhandling()
        except TypeError:
            self.root.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()
        except UnboundLocalError:
            logg.logging.critical("False input error occured", exc_info=True)
            print("Wrong Vehicleaddress.")
        except NameError:
            self.root.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()
        else:
            return True


class AdminWin:
    def __init__(self, Toplevelframe):
        self.Toplevelframe = Toplevelframe
        self.admingate = Toplevel(Toplevelframe.root)
        self.vehicle = Toplevelframe.vehicle

        self.status = StringVar
        self.Adminframe = Toplevel(Toplevelframe.root)

        self.vehicleattributes = self.vehicle.attributes.copy()
        # --------------------------Admingate------------------------------------------------------------------------------------
        self.__Infolabel = Label(self.admingate,
                                 text="Enter Passcode here: ",
                                 borderwidth=5,
                                 relief="groove")
        self.__Passentry = Entry(self.admingate,
                                 borderwidth=5,
                                 relief="groove")
        self.__Submit = Button(self.admingate,
                               text="Submit",
                               command=self.__Send)
        self.__Quit = Button(self.admingate,
                             text="Quit",
                             command=self.admingate.destroy)
        # ---------------------Admminframe---------------------------------------------------------------------------------------
        self.__GateLabel = Label(self.Adminframe,
                                 text="Please confirm access.",
                                 width=100,
                                 height=20,
                                 borderwidth=5,
                                 relief="groove")

        self.__NameLabel = Label(self.Adminframe,
                                 text="Name",
                                 width=10,
                                 height=2,
                                 borderwidth=5,
                                 relief="groove")

        self.__NameOutput = Label(self.Adminframe,
                                  text=self.vehicleattributes.get("Name"),
                                  width=10,
                                  height=2,
                                  borderwidth=5,
                                  relief="groove")

        self.__StatusLabel = Label(self.Adminframe,
                                   text="Status",
                                   width=10,
                                   height=2,
                                   borderwidth=5,
                                   relief="groove")

        self.__StatusOutput = Label(self.Adminframe,
                                    text=self.vehicleattributes.get("Status"),
                                    width=10,
                                    height=2,
                                    borderwidth=5,
                                    relief="groove")
        # --------------------------------Pin-----------------------------------------
        self.__WheelFWLabel = Label(self.Adminframe,
                                    text="FW-Pin",
                                    width=10,
                                    height=2,
                                    borderwidth=5,
                                    relief="groove")

        self.__WheelFWOutput = Button(self.Adminframe,
                                      text=self.vehicleattributes.get("FW"),
                                      width=10,
                                      height=2,
                                      borderwidth=5,
                                      relief="raised",
                                      command=self.__changeFW)

        self.__NewWheelFW = Entry(self.Adminframe,
                                  width=10,
                                  borderwidth=5,
                                  relief="sunken")

        self.__WheelBWLabel = Label(self.Adminframe,
                                    text="BW-pin",
                                    width=10,
                                    height=2,
                                    borderwidth=5,
                                    relief="groove")

        self.__WheelBWOutput = Button(self.Adminframe,
                                      text=self.vehicleattributes.get("BW"),
                                      width=10,
                                      height=2,
                                      borderwidth=5,
                                      relief="raised",
                                      command=self.__changeBW)

        self.__NewWheelBW = Entry(self.Adminframe,
                                  width=10,
                                  borderwidth=5,
                                  relief="sunken")
        # -----------------------------------------------------------------------------------
        self.__URLLabel = Label(self.Adminframe,
                                text="URL ",
                                width=15,
                                height=2,
                                borderwidth=5,
                                relief="groove")

        self.__URLOutput = Label(self.Adminframe,
                                 text=self.vehicleattributes.get("URL"),
                                 width=15,
                                 height=2,
                                 borderwidth=5,
                                 relief="groove")

        self.__JOLLabel = Label(self.Adminframe,
                                text="JOL'able ",
                                width=15,
                                height=2,
                                borderwidth=5,
                                relief="groove")

        self.__JOLOutput = Label(self.Adminframe,
                                 text=self.vehicleattributes.get("JOL"),
                                 width=15,
                                 height=2,
                                 borderwidth=5,
                                 relief="groove")

        self.__GreyBar = Label(self.Adminframe,
                               width=60,
                               borderwidth=5,
                               relief="groove")

        self.__StatusChangeLabel = Label(self.Adminframe,
                                         text="Change \n Status ",
                                         width=10,
                                         height=5,
                                         borderwidth=5,
                                         relief="groove")

        self.__Statuschange_Deactivated = Radiobutton(self.Adminframe,
                                                      text="Deactivate",
                                                      width=10,
                                                      height=2,
                                                      indicatoron=0,
                                                      padx=10,
                                                      pady=5,
                                                      command=self.__set_deactivated,
                                                      variable=self.status)

        self.__StatusChange_ready = Radiobutton(self.Adminframe,
                                                text="Ready",
                                                width=10,
                                                height=2,
                                                indicatoron=0,
                                                padx=10,
                                                pady=5,
                                                command=self.__set_ready,
                                                variable=self.status)

        self.__SaveChanges = Button(self.Adminframe,
                                    text="Save",
                                    width=10,
                                    height=2,
                                    command=self.__savechanges)

    def __changeFW(self):
        self.__WheelFWOutput.grid_remove()
        self.__NewWheelFW.grid(row=3, column=3)

    def __changeBW(self):
        self.__WheelBWOutput.grid_remove()
        self.__NewWheelBW.grid(row=4, column=3)

    def __Send(self):
        try:
            if self.__Passentry.get() == self.vehicle.getattribute("Passcode"):
                assert (self.__Passentry.get() == self.vehicle.getattribute("Passcode"))
                self.admingate.destroy()
                self.__GateLabel.grid_remove()
                self.__build_Adminframe()
        except AssertionError:
            logg.logging.warning("User tried to acess adminframe without cars passcode.", exc_info=True)

    def __set_deactivated(self):
        self.vehicleattributes["Status"] = "Deactivated"
        logg.logging.info(self.vehicleattributes["Name"] + " was set on deactivated.")

    def __set_ready(self):
        self.vehicleattributes["Status"] = "Ready"
        logg.logging.info(self.vehicleattributes["Name"] + " was set on deactivated.")

    def __savechanges(self):
        if self.__NewWheelFW.get() != "":
            self.vehicleattributes["FW"] = self.__NewWheelFW.get()
        if self.__NewWheelBW.get() != "":
            self.vehicleattributes["BW"] = self.__NewWheelBW.get()

        self.vehicle.attributes.update(self.vehicleattributes)
        logg.logging.info(self.vehicleattributes["Name"] + " Changes are now saved")
        self.vehicle.save_changes()
        self.Adminframe.destroy()

    def build_gate(self):
        try:
            self.__Infolabel.grid(row=0, column=0)
            self.__Passentry.grid(row=0, column=1)
            self.__Submit.grid(row=1, column=0)
            self.__Quit.grid(row=1, column=1)

            self.__GateLabel.grid()
        except ValueError:
            self.admingate.destroy()
            logg.logging.debug("ValueError occured in main", exc_info=True)
            Errorhandling()
        except TypeError:
            self.admingate.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()
        except NameError:
            self.admingate.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()

    def __build_Adminframe(self):
        try:
            if self.vehicleattributes["Status"] == "Ready":
                self.__Statuschange_Deactivated.grid(row=3, column=1)
            else:
                self.__StatusChange_ready.grid(row=3, column=1)

            self.__NameLabel.grid(row=0, column=0)
            self.__NameOutput.grid(row=0, column=1)
            self.__StatusLabel.grid(row=1, column=0)
            self.__StatusOutput.grid(row=1, column=1)
            self.__URLLabel.grid(row=0, column=2)
            self.__URLOutput.grid(row=0, column=3)
            self.__JOLLabel.grid(row=1, column=2)
            self.__JOLOutput.grid(row=1, column=3)
            self.__GreyBar.grid(row=2, column=0, columnspan=4)
            self.__StatusChangeLabel.grid(row=3, column=0, rowspan=2)
            self.__SaveChanges.grid(row=5, column=3)
            self.__WheelFWLabel.grid(row=3, column=2)
            self.__WheelFWOutput.grid(row=3, column=3)
            self.__WheelBWLabel.grid(row=4, column=2)
            self.__WheelBWOutput.grid(row=4, column=3)

        except ValueError:
            self.Adminframe.destroy()
            logg.logging.debug("ValueError occured in main", exc_info=True)
            Errorhandling()
        except TypeError:
            self.Adminframe.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()
        except NameError:
            self.Adminframe.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()


class ControlWin:
    def __init__(self, Toplevelframe):
        self.ctrlwin = Toplevel(Toplevelframe.root)
        self.speed = IntVar
        self.vehicle = Toplevelframe.vehicle

        self.__RadioExpla = Label(self.ctrlwin,
                                  width=27,
                                  height=10,
                                  borderwidth=5,
                                  relief="groove",
                                  text=" <-- Speed \n Conns --> ",
                                  font="Times, 15")
        self.__RadioButtonSpeed100 = Radiobutton(self.ctrlwin,
                                                 text="100 %",
                                                 width=25,
                                                 height=4,
                                                 indicatoron=0,
                                                 padx=10,
                                                 pady=5,
                                                 variable=self.speed,
                                                 value=1)
        self.__RadioButtonSpeed50 = Radiobutton(self.ctrlwin,
                                                text=" 50 %",
                                                width=25,
                                                height=4,
                                                indicatoron=0,
                                                padx=10,
                                                pady=5,
                                                variable=self.speed,
                                                value=2)
        self.__Buttonforward = Button(self.ctrlwin,
                                      text="Forward",
                                      command=self.__mov_forward,
                                      height=2)
        self.__Buttonbackward = Button(self.ctrlwin,
                                       text="Backward",
                                       command=self.__mov_backward,
                                       height=2)
        self.__Buttonleft = Button(self.ctrlwin,
                                   text="Left",
                                   command=self.__mov_left,
                                   height=2)
        self.__Buttonright = Button(self.ctrlwin,
                                    text="Right",
                                    command=self.__mov_right,
                                    height=2)
        self.__Carstop = Button(self.ctrlwin,
                                text="Fullstop",
                                command=self.__mov_carstop,
                                height=2)

    def __mov_forward(self):
        try:
            self.vehicle.call_for_movement(100)
        except NameError:
            logg.logging.debug("Vehicle undeclared.", exc_info=True)
            pass

    def __mov_backward(self):
        try:
            self.vehicle.call_for_movement(111)
        except NameError:
            logg.logging.debug("Vehicle undeclared.", exc_info=True)
            pass

    def __mov_right(self):
        try:
            self.vehicle.call_for_movement(101)
        except NameError:
            logg.logging.debug("Vehicle undeclared.", exc_info=True)
            pass

    def __mov_left(self):
        try:
            self.vehicle.call_for_movement(110)
        except NameError:
            logg.logging.debug("Vehicle undeclared.", exc_info=True)
            pass

    def __mov_carstop(self):
        try:
            self.vehicle.call_for_movement(000)
        except NameError:
            logg.logging.debug("Vehicle undeclared.", exc_info=True)
            pass

    def build(self):
        try:
            self.__Buttonforward.grid(row=0, column=3, columnspan=3)
            self.__Buttonleft.grid(row=1, column=2)
            self.__Carstop.grid(row=1, column=3)
            self.__Buttonright.grid(row=1, column=4)
            self.__Buttonbackward.grid(row=2, column=3, columnspan=3)
            self.__RadioExpla.grid(row=0, rowspan=3, column=1)
            self.__RadioButtonSpeed50.grid(row=0, column=0)
            self.__RadioButtonSpeed100.grid(row=1, column=0)
        except IOError:
            logg.logging.debug("IOError occured. Wrong path on input.", exc_info=True)
            pass
        except ValueError:
            self.ctrlwin.destroy()
            logg.logging.debug("ValueError occured in main", exc_info=True)
            Errorhandling()
        except TypeError:
            self.ctrlwin.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()
        except NameError:
            self.ctrlwin.destroy()
            logg.logging.debug("TypeError occured in main", exc_info=True)
            Errorhandling()


logg.logging.info("Windows classes properly loaded.")

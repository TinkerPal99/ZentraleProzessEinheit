import PyViz.library.reference
from Library.PyMod import rssProcess


class PiViz:
    def __init__(self, page):
        self.page = page
        self.__Weather = PyViz.library.reference.CSVtoList("library/csv/Weather.csv")  # ["wetter", "Wetter"]
        self.__News = PyViz.library.reference.CSVtoList("library/csv/News.csv")  # ["Nachrichten", "nachrichten", "News", "news"]
        self.__Consent = PyViz.library.reference.CSVtoList(
            "library/csv/Consent.csv")  # ["Yes", "Jo", "Ja", "Yep", "Jep", "yes", "jo", "ja", "yep", "jep"]
        self.__Dissent = PyViz.library.reference.CSVtoList("library/csv/Dissent.csv")  # ["No", "Nope", "Nep", "Noe", "no", "nope", "nep", "noe"]
        self.__Note = PyViz.library.reference.CSVtoList("library/csv/Note.csv")
        self.Notelist = PyViz.library.reference.CSVtoList("library/csv/Notes.csv")
        self.__Get = PyViz.library.reference.CSVtoList("library/csv/Get.csv")
        self.__Set = PyViz.library.reference.CSVtoList("library/csv/Set.csv")
        self.__Delete = PyViz.library.reference.CSVtoList("library/csv/Delete.csv")
        self.__Number = PyViz.library.reference.CSVtoList("library/csv/Integer.csv")

    def onInput(self, input):
        __recent_input = input
        __splitted_list = __recent_input.split(" ")
        return __splitted_list

    def run(self, input_list):
        output = []
        if len(input_list) > 0:
            # ______________________Wetter_______________________________________________________________________________________
            if PyViz.library.reference.searchBy(input_list, self.__Weather):
              output.append("Hier ist das aktuelle Wetter.")
            # ___________________________News_______________________________________________________________________________________
            if PyViz.library.reference.searchBy(input_list, self.__News) \
                    and PyViz.library.reference.searchBy(input_list, self.__Number):
                indexpos = PyViz.library.reference.extractInput(input_list, self.__Number)
                __feed = rssProcess.loadFeed(self.page)
                entry = __feed.entries[indexpos]
                output.append("Post Title : -" + entry.title + "- from " + entry.link + "\n" +
                              "########################################################################################################## \n")

                __splitted_entry = entry.summary.split(" ")
                __splitted_entry.pop()
                for x in range(0, len(__splitted_entry)):
                    output.append(__splitted_entry[x] + "\n")
                    x = x + 1
                output.append(
                    "___________________________________________________________________________________________________________ \n")

            elif PyViz.library.reference.searchBy(input_list, self.__News):
               output.append("Hier sind die aktuellen Top 5 News von " + self.page + "\n")
               output.append(rssProcess.show_all_Entries_of(self.page))
            # _______________________________Notizen________________________________________________________________________________
            # if reference.searchBy(input_list, reference.getList(reference.__Note)):
            #    if reference.searchBy(input_list, reference.getList(reference.__Set)):
            #        __newNote = input("Wie lautet ihre neue Notiz ?")
            #        reference.Notelist.append(__newNote)
            #    elif reference.searchBy(input_list, reference.getList(reference.__Get)):
            #        for x in range(0, len(reference.Notelist)):
            #            print ("[" + str(x) + "] " + reference.Notelist[x])
            #            x = x + 1
            #    elif reference.searchBy(input_list, reference.getList(reference.__Delete)):
            #        __delete = input("Welche Notiz soll entfernt werden ? Geben Sie bitte die Indexposition an. ")
            #        print (reference.Notelist.pop(__delete) + " wurde entfernt.")
            #    __newrow = ",".join(reference.Notelist)
            #    reference.rewrite_csv("library/csv/Notes.csv", __newrow)'''
        else:
            output.append("Entschuldigung, dass habe ich nicht verstanden.")

        return output

from library import reference
from Library.PyMod import rssProcess

page = reference.getList(reference._Guardian)

print ("Booting abgeschlossen ... Guten Tag, Sir.")

while 1:

    input_list = reference.inputToProcess("Was wuenschen Sie? ")

    if len(input_list) > 0:
# ______________________Wetter_______________________________________________________________________________________
        if reference.searchBy(input_list, reference.getList(reference.__Weather)):
            print ("Hier ist das aktuelle Wetter.")
# ___________________________News_______________________________________________________________________________________
        if reference.searchBy(input_list, reference.getList(reference.__News)) \
                and reference.searchBy(input_list, reference.getList(reference.__Number)):
            indexpos = reference.extractInput(input_list, reference.__Number)
            rssProcess.full_feedEntry(page, indexpos)
        elif reference.searchBy(input_list, reference.getList(reference.__News)):
            print ("Hier sind die aktuellen Top 5 News von " + page)
            print ("")
            rssProcess.show_all_Entries_of(page)
            while reference.followUp_handle("Wollen Sie sich einen genauer anschauen ? "):
                indexpos = int(reference.handleIndex())
                rssProcess.full_feedEntry(page, indexpos)

# _______________________________Notizen________________________________________________________________________________
        if reference.searchBy(input_list, reference.getList(reference.__Note)):
            if reference.searchBy(input_list, reference.getList(reference.__Set)):
                __newNote = input("Wie lautet ihre neue Notiz ?")
                reference.Notelist.append(__newNote)
            elif reference.searchBy(input_list, reference.getList(reference.__Get)):
                for x in range(0, len(reference.Notelist)):
                    print ("[" + str(x) + "] " + reference.Notelist[x])
                    x = x + 1
            elif reference.searchBy(input_list, reference.getList(reference.__Delete)):
                __delete = input("Welche Notiz soll entfernt werden ? Geben Sie bitte die Indexposition an. ")
                print (reference.Notelist.pop(__delete) + " wurde entfernt.")
            __newrow = ",".join(reference.Notelist)
            reference.rewrite_csv("library/csv/Notes.csv", __newrow)
    else:
        print ("Entschuldigung, dass habe ich nicht verstanden.")

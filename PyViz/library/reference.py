import csv

# webpages
_Guardian = "https://www.theguardian.com/world/rss"


# --------------------CSVHandlle----------------------------
def CSVtoList(inputCSV=str):
    outputList = list
    with open(inputCSV) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            ()
        outputList = row
        csvfile.close()
        return outputList


def rewrite_csv(fileName, newRow):
    __new_file = open(fileName, "w")
    __new_file.write(newRow)
    __new_file.close()


# ----------------------listhandle-------------------------------
def getList(collection=list):
    return collection


def searchBy(inputcollection=list, compare_collection=list):
    __value = False
    for x in range(0, len(inputcollection)):
        for y in range(0, len(compare_collection)):
            if inputcollection[x] == compare_collection[y]:
                __value = True
            else:
                y = y + 1
        y = 0
    return __value


def inputToProcess(output=str):
    __recent_input = input(output)
    __splitted_list = __recent_input.split(" ")
    return __splitted_list


def extractInput(inputcollection=list, compare_collection=list):
    for x in range(0, len(inputcollection)):
        for y in range(0, len(compare_collection)):
            if inputcollection[x] == compare_collection[y]:
                __value = int(inputcollection[x])
            else:
                y = y + 1
        y = 0
    return __value


def followUp_handle(output=str):
    __status = False
    print ("\n \n \n \n")
    __splitted_list = inputToProcess(output)
    if searchBy(__splitted_list, __Consent):
        __status = True
    return __status

def handleIndex():
    while 1:
        try:
            indexposition = input("Welchen wollen sie sich genauer ansehen? ")
            indexposition = int(indexposition)
            break
        except ValueError:
            print "Please enter only a indexposition that is valued. E.g. 5"
    return indexposition


# -------------------------------------------------------------------
try:
    __Weather = CSVtoList("library/csv/Weather.csv")  # ["wetter", "Wetter"]
    __News = CSVtoList("library/csv/News.csv")  # ["Nachrichten", "nachrichten", "News", "news"]
    __Consent = CSVtoList(
        "library/csv/Consent.csv")  # ["Yes", "Jo", "Ja", "Yep", "Jep", "yes", "jo", "ja", "yep", "jep"]
    __Dissent = CSVtoList("library/csv/Dissent.csv")  # ["No", "Nope", "Nep", "Noe", "no", "nope", "nep", "noe"]
    __Note = CSVtoList("library/csv/Note.csv")
    Notelist = CSVtoList("library/csv/Notes.csv")
    __Get = CSVtoList("library/csv/Get.csv")
    __Set = CSVtoList("library/csv/Set.csv")
    __Delete = CSVtoList("library/csv/Delete.csv")
    __Number = CSVtoList("library/csv/Integer.csv")
    __list1 = ["1", "2", "5", "7"]
    __list2 = ["3", "4", "8", "5", "9"]
except ImportError:
    print ("Please check the imports.")
    print (ImportError.message)
    exit(1)


def SaveLists():
    try:
        rewrite_csv("library/csv/Dissent.csv", ",".join(__Dissent))
        rewrite_csv("library/csv/Weather.csv", ",".join(__Weather))
        rewrite_csv("library/csv/News.csv", ",".join(__News))
        rewrite_csv("library/csv/Consent.csv", ",".join(__Consent))
        rewrite_csv("library/csv/Note.csv", ",".join(__Note))
        rewrite_csv("library/csv/Notes.csv", ",".join(Notelist))
        rewrite_csv("library/csv/Get.csv", ",".join(__Get))
        rewrite_csv("library/csv/Set.csv", ",".join(__Set))
        rewrite_csv("library/csv/Delete.csv", ",".join(__Delete))
        rewrite_csv("library/csv/Integer.csv", ",".join(__Number))
        print ("Properly rewrote the csv's")
    except IOError:
        print ("Please check the imports.")
        print (IOError.message)
        pass
    except OSError:
        print ("Please check the imports.")
        print (OSError.message)
        pass

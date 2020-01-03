# https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm
import feedparser

# __ExampleFeed = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
__ExampleFeed = "http://www.tagesschau.de/xml/rss2"
__ExampleWeather = "https://www.wetterleitstelle.de/rss.php"


def checkNewFeed(feed=str):
    NewsFeed = feedparser.parse(__ExampleFeed)
    entry = NewsFeed.entries[1]
    print entry.keys()


def loadFeed(feed=str):
    __newsFeed = feedparser.parse(feed)
    return __newsFeed


def print_splittedEntry_of(summary, sign=str):
    __splitted_entry = summary.split(sign)
    __splitted_entry.pop()
    for x in range(0, len(__splitted_entry)):
        print __splitted_entry[x]
        x = x + 1


def headline_feedEntry(preload_feed, index):
    entry = preload_feed.entries[index]
    print ("[" + str(index) + "]" + " Post Title : " + entry.title)


def full_feedEntry(feed_url, index):
    __feed = loadFeed(feed_url)
    entry = __feed.entries[index]
    print ("Post Title : -" + entry.title + "- from " + entry.link)
    print ("##########################################################################################################")
    print_splittedEntry_of(entry.summary, "</p>")
    print ("__________________________________________________________________________________________________________")


def show_x_Entries_of(feed=str, x=int):
    __feed = loadFeed(feed)
    if len(__feed) < x:
        for x in range(0, len(__feed)):
            x = x + 1
            headline_feedEntry(__feed, x)
    else:
        for x in range(0, x):
            x = x + 1
            headline_feedEntry(__feed, x)


def show_all_Entries_of(feed=str):
    __feed = loadFeed(feed)
    for x in range(0, len(__feed)):
        x = x + 1
        headline_feedEntry(__feed, x)

from bs4 import BeautifulSoup
import time
import requests
import string

"""basketball refrence's player stats page urls, start with the first letter of
their last name, then  a string that starts with the first 5 letters of their
last name, then first two letters of their first name, and final 01, so here I
use the player lists I got from getPlayerList to create the string I need for
the url.  I then make a dictionary where each key is the url string and the value
is boolean denoting if the stats page has been downloaded.
Once i get the url string i check the download list to see if I have
already downloaded the stats page for the player, if I have I set the
boolean to true"""
def downloadPlayerInfo():
    alphabet = list(string.ascii_uppercase)
    urlStart= "https://www.basketball-reference.com"
    for letter in alphabet:
        with open("../../HTML/Players/{0}/{0}list.HTML".format(letter), encoding="utf-8") as f:
            page = f.read()
        playerIndex = BeautifulSoup(page, "html.parser")
        for row in playerIndex.find_all("tr"):
            nameCol = row.find_all('th')[0]
            linkTag = nameCol.find("a",href=True)
            if(linkTag != None):
                urlEnd = linkTag.get("href")
                url = urlStart + urlEnd
                key = urlEnd.split("/")[3]
                if(key not in open("../../HTML/Players/downloadList.txt").read()):
                    data = requests.get(url)
                    with open("../../HTML/Players/{}/{}".format(key[0],key), "w+", encoding="utf-8") as f:
                        f.write(data.text)
                    with open("../../HTML/Players/downloadList.txt", "a") as f:
                        f.write(key)
                        f.write("\n")
                    print(key)
                    time.sleep(5)
downloadPlayerInfo()

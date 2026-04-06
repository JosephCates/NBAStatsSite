from bs4 import BeautifulSoup
import time
import requests

"""
This function downloads updated player information from basketball-reference.com for players listed in the update list HTML file.
It checks if the player has already been downloaded by consulting updateList.txt, and if not, it fetches their stats page,
saves the HTML locally in the appropriate folder, and appends the player's key to updateList.txt to avoid duplicate downloads.
"""
def downloadUpdatedPlayerInfo():
    urlStart = "https://www.basketball-reference.com"
    with open("../../../HTML/Players/Update/updateList.HTML", encoding="utf-8") as f:
        page = f.read()
    with open("../../../HTML/Players/Update/updateList.txt", "r") as f:
        downloadedPlayers = f.read()
    playerIndex = BeautifulSoup(page, "html.parser")
    for row in playerIndex.find_all("tr"):
        tds = row.find_all('td')
        if len(tds) < 1:
            continue
        nameCol = tds[0]
        linkTag = nameCol.find("a", href=True)
        if(linkTag != None):
            urlEnd = linkTag.get("href")
            url = urlStart + urlEnd
            key = urlEnd.split("/")[3]
            if(key not in downloadedPlayers):
                data = requests.get(url)
                with open("../../../HTML/Players/{}/{}".format(key[0], key), "w+", encoding="utf-8") as f:
                    f.write(data.text)
                with open("../../../HTML/Players/Update/updateList.txt", "a") as f:
                    f.write(key)
                    f.write("\n")
                downloadedPlayers += key + "\n"
                print(key)
                time.sleep(5)
downloadUpdatedPlayerInfo()
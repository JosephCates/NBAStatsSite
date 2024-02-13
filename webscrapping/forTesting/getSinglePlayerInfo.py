from bs4 import BeautifulSoup
import string
import pandas as pd
import time
def getSinglePlayerInfo():
    #"HTML/Players/A/antetgi01.html"
    #abdelal01.html

    with open("../../HTML/Players/w/willish01.html", "r", encoding="utf-8") as playerFile:
        page = playerFile.read()
        soup = BeautifulSoup(page, "html.parser")
        playerInfo = soup.find(id="meta")
        name = playerInfo.h1.span.get_text()
        #birthList = playerInfo.find(id='necro-birth').get_text().replace("\n", " ")
        #birth = " ".join(birthList.split())
        count = 0
        #print(playerInfo.find_all('p'))
        position = "Unknown"
        height = "Unknown"
        weight = "Unknown"
        college = "Did Not Attend College"
        draft = "Undrafted"
        birth = "Unknown"
        for text in playerInfo.find_all('p'):
            if("Born:" in text.get_text()):
                born = text.get_text().replace("Born:","").strip().split()
                if(len(born) == 1):
                    birth = born[0]
                else:
                    birth = born[0] + " " + born[1] + " " + born[2]
            if("Position" in text.get_text()):
                    position = text.get_text().replace("▪", "").replace("Shoots:", "").replace("Right", "").replace("Left","").replace("Position:","").strip()
            if("lb" in text.get_text() and "-" in text.get_text()):
                    heightWeight = text.get_text().split()
                    print(heightWeight)
                    height = heightWeight[0]
                    weight = heightWeight[1]
            if("College:" in text.get_text()):
                college = text.get_text().replace("College:","").strip()
            if("Draft:" in text.get_text()):
                draft = text.get_text().replace("Draft:","").strip()
        PlayerInfoDict = {
        "PlayerID":"hardeja01",
        "Name":name,
        "Position:":position,
        "College":college,
        "Height":height,
        "Weight":weight,
        "BirthDate":birth,
        "Draft":draft,
        }
        PlayerInfoJson = json.dumps(PlayerInfoDict, indent=4)
        with open("../../JSON/PlayerInfo.json", "a") as outfile:
            json.dump(data, f)
        """print(birth)
        print(position)
        print(height,weight)
        print(college)
        print(draft)"""

getSinglePlayerInfo()

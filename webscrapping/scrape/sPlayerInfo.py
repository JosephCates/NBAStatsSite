from bs4 import BeautifulSoup
from unidecode import unidecode
import json

def scrapePlayerInfo():
    diclist = []
    with open("../../HTML/Players/downloadList.txt", "r", encoding="utf-8") as playerList:
        for key in playerList:
            with open("../../HTML/Players/{}/{}".format(key[0].upper(), key.replace("\n","")), "r", encoding="utf-8") as playerFile:
                page = playerFile.read()
                soup = BeautifulSoup(page, "html.parser")
                playerInfo = soup.find(id="meta")
                name = playerInfo.h1.span.get_text()
                print(name)
                nameli = playerInfo.h1.span.get_text().split()
                firstName = nameli[0]
                lastName = nameli[len(nameli)-1]
                swapNames = ["III","IV","II", "Jr.", "Sr."]
                if(len(nameli) > 2):
                    middleNameLi = nameli[1:-1]
                    middleName = ' '.join(middleNameLi)
                    if(middleName != "" and lastName in swapNames):
                        tmp = middleName
                        middleName = lastName
                        lastName = tmp
                else:
                    middleName = ""
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
                    if("Position:" in text.get_text()):
                        position = text.get_text().replace("▪", "").replace("Shoots:", "").replace("Right", "").replace("Left","").replace("Position:","").strip()
                    if("lb" in text.get_text()  and "-" in text.get_text()):
                        heightWeight = text.get_text().split()
                        height = heightWeight[0]
                        weight = heightWeight[1]
                    if("College:" in text.get_text()):
                        college = text.get_text().replace("College:","").strip()
                    if("Draft:" in text.get_text()):
                        draft = text.get_text().replace("Draft:","").strip()
                PlayerInfoDict = {
                "PlayerID":key.replace(".html\n",""),
                "Name":unidecode(name),
                "firstName":unidecode(firstName),
                "lastName": unidecode(lastName),
                "middleName":unidecode(middleName),
                "Position":position,
                "College":college,
                "Height":height,
                "Weight":weight,
                "BirthDate":birth,
                "Draft":draft,
                }
                diclist.append(PlayerInfoDict)

        with open("../../JSON/PlayerInfo.json", "a", encoding="utf-8") as outfile:
            json.dump(diclist, outfile, ensure_ascii=False, indent=4)
scrapePlayerInfo()

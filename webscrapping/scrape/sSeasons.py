from bs4 import BeautifulSoup
import json

def scrapeSeasons():
    diclist = []
    with open("../../HTML/Seasons/SeasonList.txt", encoding="utf-8") as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    seasonTable = soup.find(id="stats")
    years = "Unavailable"
    champion = "Unavailable"
    MVP = "Unavailable"
    ROY = "Unavailable"
    pointsLeader = "Unavailable"
    assistsLeader = "Unavailable"
    reboundLeader = "Unavailable"
    count = 0
    li = []
    for text in seasonTable.find_all(class_="left"):
        if(count % 9 == 0 and count != 0):
            seasonInfoDict = {
            "seasonID":li[0],
            "champion":li[2],
            "MVP":li[3],
            "ROY":li[4],
            "pointsLeader":li[5],
            "reboundLeader":li[6],
            "assistsLeader":li[7],
            }
            if(li[1] == "NBA"):
                diclist.append(seasonInfoDict)
            li = []
        if("-" in text.get_text() and "Abdul" not in text.get_text()):
            li.append(text.get_text())
        elif(text.get_text() == ""):
            li.append("Unavailable")
        else:
            str = text.get_text().replace("\xa0(","")
            result = ''.join([i for i in str if not i.isdigit()])
            li.append(result.replace(")",""))
        print(li[0])
        count+=1
    with open("../../JSON/seasonInfo.json", "a", encoding="utf-8") as outfile:
        json.dump(diclist, outfile, ensure_ascii=False, indent=4)

from bs4 import BeautifulSoup
import json

def getTeamKey(city,name):
    key = ""
    if("Nets" == name):
        key = "BRN"
    elif("Warriors" == name):
        key = "GSW"
    elif("Clippers" == name):
        key = "LAC"
    elif("Lakers" == name):
        key = "LAL"
    elif("Pelicans" == name):
        key = "NOP"
    elif("Knicks" == name):
        key = "NYK"
    elif("Thunder" == name):
        key = "OKC"
    elif("Spurs" == name):
        key = "SAS"
    else:
        key = city[:3].upper()
    return key

def scrapeTeamInfo():
    diclist = []
    with open("../../HTML/Teams/teamList.txt", encoding="utf-8") as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    teamtable = soup.find(id="teams_active")
    teamID = "Unknown"
    name = "Unknown"
    city = "Unknown"
    founding = "Unknown"
    for text in teamtable.find_all(class_="full_table"):
        for teamCtyName in text.find_all("a"):
            li = teamCtyName.get_text().split()
            if(len(li) == 2):
                city = li[0]
                teamName = li[1]
            else:
                city = li[0] + " " + li[1]
                teamName = li[2]
        count = 0
        for startYear in text.find_all(class_ = "right"):
            if(count == 0):
                founding = startYear.get_text()
            count+=1
        teamID = getTeamKey(city,teamName)
        teamInfoDict = {
        "teamID":teamID,
        "Name":teamName,
        "City":city,
        "Founding":founding,
        }
        diclist.append(teamInfoDict)
    with open("../../JSON/teamInfo.json", "a", encoding="utf-8") as outfile:
        json.dump(diclist, outfile, ensure_ascii=False, indent=4)
scrapeTeamInfo()

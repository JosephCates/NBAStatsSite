from bs4 import BeautifulSoup
import requests

def testTeamSeasonInfoHTML():
    seasonInfoUnformated = "https://www.basketball-reference.com/teams/{0}/{1}.html"
    ID = "DEN"
    year = 2025
    with open("../../HTML/Teams/{0}/{0}list.HTML".format(ID), "r", encoding="utf-8") as teamList:
        page = teamList.read()
        soup = BeautifulSoup(page, "html.parser")
        seasonTable = soup.find(id=ID)
        for row in seasonTable.find_all("tr"):
            count = 0
            for info in row.find_all("td"):
                if(count == 1):
                    teamName = info.get_text().strip("*")
                    teamID = genTeamIDfromName(teamName, year)
                    url = seasonInfoUnformated.format(teamID,year)
                    print(url)
                count+=1
            year -= 1

def GetBRN():
    url = "https://www.basketball-reference.com/teams/CHH/1989.html"
    data = requests.get(url)
    with open("../../HTML/Teams/CHA/CHA1989.HTML", "w+", encoding="utf-8") as f:
        f.write(data.text)

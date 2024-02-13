import time
import requests
import genTeamID
def downloadTeamSeasonInfo():
    seasonInfoUnformated = "https://www.basketball-reference.com/teams/{0}/{1}.html"
    with open("../../JSON/teamInfo.json", "r", encoding="utf-8") as f:
            teams = json.load(f)
            for i in teams:
                year = 2025
                ID = i["teamID"]
                if(ID == "BRN"):
                    brRefID = "NJN"
                elif(ID == "NOP"):
                    brRefID = "NOH"
                else:
                    brRefID = ID
                with open("../../HTML/Teams/{0}/{0}list.HTML".format(ID), "r", encoding="utf-8") as teamList:
                    page = teamList.read()
                    soup = BeautifulSoup(page, "html.parser")
                    seasonTable = soup.find(id=brRefID)
                    for row in seasonTable.find_all("tr"):
                        count = 0
                        for info in row.find_all("td"):
                            if(count == 1):
                                teamName = info.get_text().strip("*")
                                teamID = genTeamID(teamName, year)
                                url = seasonInfoUnformated.format(teamID,year)
                                time.sleep(5)
                                data = requests.get(url)
                                with open("../../HTML/Teams/{0}/{0}{1}.HTML".format(ID,year), "w+", encoding="utf-8") as f:
                                    f.write(data.text)
                            count+=1
                        year -= 1
downloadTeamSeasonInfo()

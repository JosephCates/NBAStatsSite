import json
import time
import requests
from genTeamID import genTeamID
from bs4 import BeautifulSoup

def downloadTeamSingleSeasonInfo(year):
    seasonInfoUnformated = "https://www.basketball-reference.com/teams/{0}/{1}.html"
    with open("../../JSON/teamInfo.json", "r", encoding="utf-8") as f:
        teams = json.load(f)
        for i in teams:
            ID = i["teamID"]
            if ID == "BRN":
                brRefID = "NJN"
            elif ID == "NOP":
                brRefID = "NOH"
            else:
                brRefID = ID

            with open("../../../HTML/Teams/{0}/{0}list.HTML".format(ID), "r", encoding="utf-8") as teamList:
                page = teamList.read()
                soup = BeautifulSoup(page, "html.parser")
                seasonTable = soup.find(id=brRefID)

                currentYear = 2026  # start at the most recent season
                for row in seasonTable.find_all("tr"):
                    processed = False
                    for count, info in enumerate(row.find_all("td")):
                        if count == 1:
                            if currentYear == year:
                                teamName = info.get_text().strip("*")
                                teamID = genTeamID(teamName, year)
                                url = seasonInfoUnformated.format(teamID, year)
                                print(url)
                                time.sleep(5)
                                data = requests.get(url)
                                with open("../../../HTML/Teams/{0}/{0}{1}.HTML".format(ID, year), "w+", encoding="utf-8") as out:
                                    out.write(data.text)
                                print("Downloaded {} {}".format(ID, year))
                            processed = True
                    if processed:
                        if currentYear == year:
                            break  # found and handled our target year, stop scanning rows
                        currentYear -= 1

downloadTeamSingleSeasonInfo(2026)
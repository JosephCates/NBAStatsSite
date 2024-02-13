import time
import requests
def downloadTeamSeasonIndex():
    teamPageurl_unformated = "https://www.basketball-reference.com/teams/{}/"
    with open("JSON/teamInfo.json", "r", encoding="utf-8") as f:
        teams = json.load(f)
        for i in teams:
            if(i["teamID"] != "BRN" and i["teamID"] != "NOP" ):
                teamPageurl = teamPageurl_unformated.format(i["teamID"])
                time.sleep(5)
                data = requests.get(teamPageurl)
                with open("../../HTML/Teams/{0}/{0}list.HTML".format(i["teamID"]), "w+", encoding="utf-8") as f:
                    f.write(data.text)
            elif(i["teamID"] == "NOP"):
                data = requests.get("https://www.basketball-reference.com/teams/NOH/")
                with open("../../HTML/Teams/NOP/NOPlist.HTML", "w+", encoding="utf-8") as f:
                    f.write(data.text)
            else:
                data = requests.get("https://www.basketball-reference.com/teams/NJN/")
                with open("../../HTML/Teams/BRN/BRNlist.HTML", "w+", encoding="utf-8") as f:
                    f.write(data.text)
downloadTeamSeason()

from bs4 import BeautifulSoup
import json
from genTeamID import genTeamID
def initilizeTeamSeasonInfoDict():
    dic = {
    "teamID": " ",
    "seasonID": " ",
    "TeamAbbr":" ",
    "TeamName": " ",
    "LG": " ",
    "Record": " ",
    "Seed": " ",
    "PostSeason": "Didn't make the playoffs",
    "OffRtg": "Untracked",
    "DefRtg": "Untracked",
    "NetRtg": "Untracked",
    "expectedRecord": " ",
    "Coach": " ",
    "GM": "None"
    }
    return dic

def scrapeTeamSeason():
    dicLi = []
    with open("../../JSON/teamInfo.json", "r", encoding="utf-8") as f:
        teams = json.load(f)
        for i in teams:
            foundingUnformated = i["founding"]
            ID = i["teamID"]
            founding = int(i["founding"].split("-")[0])
            year = 2023
            while year > founding:
                if (ID == "CHA" and year == 2004) or (ID == "CHA" and year == 2003):
                    year -= 1
                else:
                    with open(f"../../HTML/Teams/{ID}/{ID}{year}.HTML", "r", encoding="utf-8") as seasonInfo:
                        page = seasonInfo.read()
                        soup = BeautifulSoup(page, "html.parser")
                        seasonTable = soup.find(id="meta")
                        count = 0
                        dic = initilizeTeamSeasonInfoDict()
                        dic["teamID"] = ID
                        yearStart = year - 1
                        yearID = f"{yearStart}-{str(year)[2]}{str(year)[3]}"
                        dic["seasonID"] = yearID
                        nameLi = seasonTable.find("h1").get_text().split()[1:]
                        dic["TeamName"] = " ".join(nameLi).replace("Roster and Stats", "").strip()
                        dic["TeamAbbr"] = genTeamID(dic["TeamName"],yearStart)
                        for row in seasonTable.find_all("p"):
                            if "Record:" in row.get_text():
                                dic["Record"] = row.get_text().replace("Record:", "").replace(",", "").strip().split()[0]
                                dic["Seed"] = row.get_text().replace("Record:", "").strip().split()[2]
                                dic["LG"] = row.get_text().replace("Record:", "").strip().split()[4]
                            if "Coach:" in row.get_text():
                                dic["Coach"] = row.get_text().replace("Coach:", "").strip()
                            if "Executive:" in row.get_text():
                                dic["GM"] = row.get_text().replace("Executive:", "").strip()
                            if "Off Rtg:" in row.get_text():
                                li = row.get_text().replace("Off Rtg:", "").replace("Def Rtg:", "").replace("Net Rtg:", "").replace("\n", "").strip().split(") ")
                                if li != [""]:
                                    dic["OffRtg"] = li[0].strip() + ")"
                                    dic["DefRtg"] = li[1].strip() + ")"
                                    dic["NetRtg"] = li[2].strip()
                            if "Expected W-L:" in row.get_text():
                                dic["expectedRecord"] = row.get_text().replace("Expected W-L:", "").replace("\n", "").replace(",", "").strip()
                            if "Playoffs:" in row.get_text():
                                li = row.get_text().replace("(Series Stats)", "").replace(u'\xa0', u'').split("\n")
                                playoffStr = ""
                                for item in li[1:-1]:
                                    playoffStr += item
                                    playoffStr += "\n"
                                dic["PostSeason"] = playoffStr
                        year -= 1
                        print(dic)
                        dicLi.append(dic)
    with open("../../JSON/teamSeasonInfo.json", "a", encoding="utf-8") as outfile:
        json.dump(dicLi, outfile, ensure_ascii=False, indent=4)
scrapeTeamSeason()

from bs4 import BeautifulSoup
import json

def scrapeTeamSingleSeason():
    dic = initilizeTeamSeasonInfoDict()
    year = 1950
    ID = "ATL"
    with open("../../HTML/Teams/{0}/{0}{1}.HTML".format(ID,year), "r", encoding="utf-8") as seasonInfo:
        page = seasonInfo.read()
        soup = BeautifulSoup(page, "html.parser")
        seasonTable = soup.find(id="meta")
        count = 0
        dic["teamID"] = ID
        yearStart = year - 1
        yearID =  str(yearStart) + "-" + list(str(year))[2] + list(str(year))[3]
        dic["seasonID"] = yearID
        for row in seasonTable.find_all("p"):
            if("Record:" in row.get_text()):
                dic["record"] = row.get_text().replace("Record:","").strip().split()[0]
                dic["seed"] = row.get_text().replace("Record:","").strip().split()[2]
                dic["league"] = row.get_text().replace("Record:","").strip().split()[4]
            if("Coach:" in row.get_text()):
                dic["coach"] = row.get_text().replace("Coach:","").strip()
            if("Executive:"in row.get_text()):
                dic["generalManager"] = row.get_text().replace("Executive:","").strip()
            if("Off Rtg:"in row.get_text()):
                li = row.get_text().replace("Off Rtg:","").replace("Def Rtg:","").replace("Net Rtg:","").replace("\n","").strip().split(") ")
                if(li != [""]):
                    dic["offensiveRating"] = li[0].strip() + ")"
                    dic["defensiveRating"] = li[1].strip()+ ")"
                    dic["netRating"] = li[2].strip()
            if("Expected W-L:" in row.get_text()):
                dic["expectedWinLoss"] = row.get_text().replace("Expected W-L:","").replace("\n","")
            if("Playoffs:" in row.get_text()):
                li = row.get_text().replace("(Series Stats)", "").replace(u'\xa0', u'').split("\n")
                playoffStr = ""
                for item in li[1:-1]:
                    playoffStr += item
                    playoffStr += "\n"
                dic["playoffOutcome"] = playoffStr
        print(dic)

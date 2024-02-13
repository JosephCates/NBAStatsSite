from bs4 import BeautifulSoup
import json

def initilizeStatsDictionary():
    dic = {"playerID": " ",
    "seasonID" :" ",
    "teamID" : " ",
    "Age"  :" ",
    "Pos" : " ",
    "GP" : "0",
    "GS" : "Untrackted",
    "MP" : "Untrackted",
    "FG" : "Untrackted",
    "FGA" : "Untrackted",
    "FG%" : "Untrackted",
    "3P":"NA",
    "3PA":"NA",
    "3P%":"NA" ,
    "2P":"NA",
    "2PA":"NA",
    "2P%":"NA",
    "eFG%": "NA",
    "FT":"Untrackted",
    "FTA":"Untrackted",
    "FT%":"Untrackted",
    "ORB": "Untrackted",
    "DRB": "Untrackted",
    "TRB":"Untrackted",
    "AST":"Untrackted",
    "STL": "Untrackted",
    "BLK":"Untrackted",
    "TOV": "Untrackted",
    "PF":"Untrackted",
    "PTS":"Untrackted"}
    return dic

def scrapePlayerStats():
    diclist = []
    with open("../../HTML/Players/downloadList.txt", "r", encoding="utf-8") as playerList:
        for playerKey in playerList:
            with open("../../HTML/Players/{}/{}".format(playerKey[0].upper(), playerKey.replace("\n","")), "r", encoding="utf-8") as playerFile:
                page = playerFile.read()
                soup = BeautifulSoup(page, "html.parser")
                if(soup.find(id="per_game")):
                    SeasonStats = soup.find(id="per_game")
                    for seasonStats in SeasonStats.find_all(class_=["full_table","light_text partial_table"])[::-1]:
                        dic = initilizeStatsDictionary()
                        print(playerKey)
                        dic["playerID"] = playerKey.replace(".html\n","")
                        count = 0
                        for year in seasonStats.find_all("th"):
                            dic["seasonID"] = year.get_text()
                        for stats in seasonStats.find_all("td"):
                            if count == 0 and stats.get_text() != "":
                                dic["Age"] = stats.get_text()
                            if count == 1 and stats.get_text() != "":
                                dic["teamID"] = stats.get_text()
                            if count == 3 and stats.get_text() != "":
                                dic["Pos"] = stats.get_text()
                            if count == 4 and stats.get_text() != "":
                                dic["GP"] = stats.get_text()
                            if count == 5 and stats.get_text() != "":
                                dic["GS"] = stats.get_text()
                            if count == 6 and stats.get_text() != "":
                                dic["MP"] = stats.get_text()
                            if count == 7 and stats.get_text() != "":
                                dic["FG"] = stats.get_text()
                            if count == 8 and stats.get_text() != "":
                                dic["FGA"] = stats.get_text()
                            if count == 9 and stats.get_text() != "":
                                dic["FG%"] = stats.get_text()
                            if(dic["seasonID"].split("-")[0] < "1979"):
                                if count == 10 and stats.get_text() != "":
                                    dic["FT"] = stats.get_text()
                                if count == 11 and stats.get_text() != "":
                                    dic["FTA"] = stats.get_text()
                                if count == 12 and stats.get_text() != "":
                                    dic["FT%"] = stats.get_text()
                                if count == 13 and stats.get_text() != "":
                                    dic["TRB"] = stats.get_text()
                                if count == 14 and stats.get_text() != "":
                                    dic["AST"] = stats.get_text()
                                if count == 15 and stats.get_text() != "":
                                    dic["PF"] = stats.get_text()
                                if count == 16 and stats.get_text() != "":
                                    dic["PTS"] = stats.get_text()
                            else:
                                if count == 10 and stats.get_text() != "":
                                    dic["3P"] = stats.get_text()
                                if count == 11 and stats.get_text() != "":
                                    dic["3PA"] = stats.get_text()
                                if count == 12 and stats.get_text() != "":
                                    dic["3P%"] = stats.get_text()
                                if count == 13 and stats.get_text() != "":
                                    dic["2P"] = stats.get_text()
                                if count == 14 and stats.get_text() != "":
                                    dic["2PA"] = stats.get_text()
                                if count == 15 and stats.get_text() != "":
                                    dic["2P%"] = stats.get_text()
                                if count == 16 and stats.get_text() != "":
                                    dic["eFG%"] = stats.get_text()
                                if count == 17 and stats.get_text() != "":
                                    dic["FT"] = stats.get_text()
                                if count == 18 and stats.get_text() != "":
                                    dic["FTA"] = stats.get_text()
                                if count == 19 and stats.get_text() != "":
                                    dic["FT%"] = stats.get_text()
                                if count == 20 and stats.get_text() != "":
                                    dic["ORB"] = stats.get_text()
                                if count == 21 and stats.get_text() != "":
                                    dic["DRB"] = stats.get_text()
                                if count == 22 and stats.get_text() != "":
                                    dic["TRB"] = stats.get_text()
                                if count == 23 and stats.get_text() != "":
                                    dic["AST"] = stats.get_text()
                                if count == 24 and stats.get_text() != "":
                                    dic["STL"] = stats.get_text()
                                if count == 25 and stats.get_text() != "":
                                    dic["BLK"] = stats.get_text()
                                if count == 26 and stats.get_text() != "":
                                    dic["TOV"] = stats.get_text()
                                if count == 27 and stats.get_text() != "":
                                    dic["PF"] = stats.get_text()
                                if count == 28 and stats.get_text() != "":
                                    dic["PTS"] = stats.get_text()
                            count+=1
                        diclist.append(dic)
    with open("../../JSON/playerSeasonStats.json", "a", encoding="utf-8") as outfile:
        json.dump(diclist, outfile, ensure_ascii=False, indent=4)
scrapePlayerStats()

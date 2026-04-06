from bs4 import BeautifulSoup

def initilizeStatsDictionary():
    dic = {
    "playerID": " ",
    "seasonID": " ",
    "teamID": " ",
    "Age": " ",
    "Pos": " ",
    "GP": "0",
    "GS": "Untrackted",
    "MP": "Untrackted",
    "FG": "Untrackted",
    "FGA": "Untrackted",
    "FG%": "Untrackted",
    "3P": "NA",
    "3PA": "NA",
    "3P%": "NA",
    "2P": "NA",
    "2PA": "NA",
    "2P%": "NA",
    "eFG%": "NA",
    "FT": "Untrackted",
    "FTA": "Untrackted",
    "FT%": "Untrackted",
    "ORB": "Untrackted",
    "DRB": "Untrackted",
    "TRB": "Untrackted",
    "AST": "Untrackted",
    "STL": "Untrackted",
    "BLK": "Untrackted",
    "TOV": "Untrackted",
    "PF": "Untrackted",
    "PTS": "Untrackted"
    }
    return dic

statMap = {
    "age": "Age",
    "team_name_abbr": "teamID",
    "team_id": "teamID",
    "pos": "Pos",
    "games": "GP",
    "g": "GP",
    "games_started": "GS",
    "gs": "GS",
    "mp_per_g": "MP",
    "fg_per_g": "FG",
    "fga_per_g": "FGA",
    "fg_pct": "FG%",
    "fg3_per_g": "3P",
    "fg3a_per_g": "3PA",
    "fg3_pct": "3P%",
    "fg2_per_g": "2P",
    "fg2a_per_g": "2PA",
    "fg2_pct": "2P%",
    "efg_pct": "eFG%",
    "ft_per_g": "FT",
    "fta_per_g": "FTA",
    "ft_pct": "FT%",
    "orb_per_g": "ORB",
    "drb_per_g": "DRB",
    "trb_per_g": "TRB",
    "ast_per_g": "AST",
    "stl_per_g": "STL",
    "blk_per_g": "BLK",
    "tov_per_g": "TOV",
    "pf_per_g": "PF",
    "pts_per_g": "PTS"
}

def scrapePlayerStats():
    key = "abdulma02"
    with open("../../../HTML/Players/A/{}.html".format(key), "r", encoding="utf-8") as playerFile:
        page = playerFile.read()
    soup = BeautifulSoup(page, "html.parser")
    SeasonStats = soup.find(id="per_game") or soup.find(id="per_game_stats")
    if SeasonStats:
        for seasonStats in SeasonStats.find_all("tr"):
            if not seasonStats.find("td"):
                continue
            dic = initilizeStatsDictionary()
            dic["playerID"] = key
            yearTh = seasonStats.find("th", {"data-stat": "year_id"}) or seasonStats.find("th", {"data-stat": "season"})
            if yearTh:
                link = yearTh.find("a")
                if link:
                    dic["seasonID"] = link.get_text()
                else:
                    continue
            for td in seasonStats.find_all("td"):
                dataStat = td.get("data-stat")
                if dataStat in statMap:
                    text = td.find("a").get_text() if td.find("a") else td.get_text()
                    if text != "":
                        dic[statMap[dataStat]] = text
            print("{} - {} - {}".format(dic["playerID"], dic["seasonID"], dic["teamID"]))
            print(dic)
            print("\n")

scrapePlayerStats()
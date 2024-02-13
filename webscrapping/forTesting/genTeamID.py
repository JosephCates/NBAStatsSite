def genTeamID(name, year):
    teamID = ""
    if(name == "Tri-Cities Blackhawks"):
        teamID = "TRI"
    if(name == "Milwaukee Hawks"):
        teamID = "MLH"
    if(name == "St. Louis Hawks"):
        teamID = "STL"
    if(name == "Atlanta Hawks"):
            teamID = "ATL"
    if(name == "Boston Celtics"):
            teamID = "BOS"
    if(name == "New York Nets" and year != 1977):
            teamID = "NYA"
    if(name == "New York Nets" and year == 1977):
                teamID = "NYN"
    if(name == "New Jersey Americans"):
            teamID = "NJA"
    if(name == "New Jersey Nets"):
            teamID = "NJN"
    if(name == "Brooklyn Nets"):
            teamID = "BRK"
    if(name == "Charlotte Hornets" and year > 2014):
            teamID = "CHO"
    if(name == "Charlotte Hornets" and year < 2014):
            teamID = "CHH"
    if(name == "Charlotte Bobcats"):
            teamID = "CHA"
    if(name == "Chicago Bulls"):
            teamID = "CHI"
    if(name == "Cleveland Cavaliers"):
            teamID = "CLE"
    if(name == "Dallas Mavericks"):
            teamID = "DAL"
    if(name == "Denver Rockets"):
            teamID = "DNR"
    if(name == "Denver Nuggets" and year > 1976):
            teamID = "DEN"
    if(name == "Denver Nuggets" and year <= 1976):
                teamID = "DNA"
    if(name == "Fort Wayne Pistons"):
            teamID = "FTW"
    if(name == "Detroit Pistons"):
            teamID = "DET"
    if(name == "Golden State Warriors"):
            teamID = "GSW"
    if(name == "San Francisco Warriors"):
            teamID = "SFW"
    if(name == "Philadelphia Warriors"):
            teamID = "PHW"
    if(name == "San Diego Rockets"):
            teamID = "SDR"
    if(name == "Houston Rockets"):
            teamID = "HOU"
    if(name == "Indiana Pacers" and year <= 1976):
            teamID = "INA"
    if(name == "Indiana Pacers" and year > 1976):
            teamID = "IND"
    if(name == "Buffalo Braves"):
            teamID = "BUF"
    if(name == "San Diego Clippers"):
            teamID = "SDC"
    if(name == "Los Angeles Clippers"):
            teamID = "LAC"
    if(name == "Minneapolis Lakers"):
            teamID = "MNL"
    if(name == "Los Angeles Lakers"):
            teamID = "LAL"
    if(name == "Vancouver Grizzlies"):
            teamID = "VAN"
    if(name == "Memphis Grizzlies"):
            teamID = "MEM"
    if(name == "Miami Heat"):
            teamID = "MIA"
    if(name == "Milwaukee Bucks"):
            teamID = "MIL"
    if(name == "Minnesota Timberwolves"):
            teamID = "MIN"
    if(name == "New Orleans Hornets"):
            teamID = "NOH"
    if(name == "New Orleans/Oklahoma City Hornets"):
            teamID = "NOK"
    if(name == "New Orleans Pelicans"):
            teamID = "NOP"
    if(name == "New York Knicks"):
            teamID = "NYK"
    if(name == "Oklahoma City Thunder"):
            teamID = "OKC"
    if(name == "Seattle SuperSonics"):
            teamID = "SEA"
    if(name == "Portland Trail Blazers"):
            teamID = "POR"
    if(name == "Sacramento Kings"):
            teamID = "SAC"
    if(name == "Rochester Royals"):
            teamID = "ROC"
    if(name == "Cincinnati Royals"):
            teamID = "CIN"
    if(name == "Kansas City-Omaha Kings"):
            teamID = "KCO"
    if(name == "Kansas City Kings"):
            teamID = "KCK"
    if(name == "Orlando Magic"):
            teamID = "ORL"
    if(name == "Philadelphia 76ers"):
            teamID = "PHI"
    if(name == "Syracuse Nationals"):
            teamID = "SYR"
    if(name == "Phoenix Suns"):
            teamID = "PHO"
    if(name == "San Antonio Spurs" and year > 1976):
            teamID = "SAS"
    if(name == "Dallas Chaparrals"):
            teamID = "DLC"
    if(name == "San Antonio Spurs" and year <= 1976):
            teamID = "SAA"
    if(name == "Toronto Raptors"):
            teamID = "TOR"
    if(name == "Utah Jazz"):
            teamID = "UTA"
    if(name == "New Orleans Jazz"):
            teamID = "NOJ"
    if(name == "Washington Wizards"):
            teamID = "WAS"
    if(name == "Chicago Packers"):
            teamID = "CHP"
    if(name == "Chicago Zephyrs"):
            teamID = "CHZ"
    if(name == "Baltimore Bullets"):
            teamID = "BAL"
    if(name == "Capital Bullets"):
            teamID = "CAP"
    if(name == "Washington Bullets"):
            teamID = "WSB"
    if(name == "Texas Chaparrals"):
                teamID = "TEX"

    return teamID

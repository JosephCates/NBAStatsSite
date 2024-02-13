import requests
def getTeamHTML():
    url = "https://www.basketball-reference.com/teams/"
    data = requests.get(url)
    with open("../../HTML/Teams/teamList.txt", "w+", encoding="utf-8") as f:
        f.write(data.text)

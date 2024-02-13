import requests
def downloadSeasons():
        url = "https://www.basketball-reference.com/leagues/"
        data = requests.get(url)
        with open("../../HTML/Seasons/SeasonList.txt", "w+", encoding="utf-8") as f:
            f.write(data.text)

from bs4 import BeautifulSoup
from datetime import date
import time
import requests
"""this function downloads the player list for the given year, if no year is given it defaults to the current year"""
def downloadPlayerListToUpdate(year=None):
    url_unformated = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"
    if(not year):
        year = date.today().year
    url = url_unformated.format(year)
    time.sleep(5)
    data = requests.get(url)
    with open("../../../HTML/Players/Update/updateList.HTML", "w+", encoding="utf-8") as f:
        f.write(data.text)
    open("../../../HTML/Players/Update/updateList.txt", "w").close()

downloadPlayerListToUpdate(2026)





import time
import requests
import string


"""gets the list of all name players sorted in alphabetical order by last name.
Also creates the download list file which will tell us if a player has had their stat
sheet downloaded. only run this function when you want to redownload all the players """
def downloadPlayerList():
    alphabet = list(string.ascii_uppercase)
    url_unformated = "https://www.basketball-reference.com/players/{}/"
    for letter in alphabet:
        url = url_unformated.format(letter)
        time.sleep(5)
        data = requests.get(url)
        with open("../../HTML/Players/{0}/{0}list.HTML".format(letter), "w+", encoding="utf-8") as f:
            f.write(data.text)
        open("../../HTML/Players/downloadList.txt", "w").close()
downloadPlayerList()

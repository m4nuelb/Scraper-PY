# coding=utf-8
import bs4
import requests

# specify the url
quote_page = ["https://www.dragonstore.it/default.asp?cmd=search&cmdFilter=1|CONSIGLIATI&orderBy=webGroupOrder&pg=1",
              "https://www.dragonstore.it/default.asp?cmd=search&cmdFilter=1|CONSIGLIATI&orderBy=webGroupOrder&pg=2"]
sorgente = requests.get(quote_page).text

soup = bs4.BeautifulSoup(sorgente, "lxml")

for page in quote_page:
    for s in soup.find_all('div', class_="resultBox"):

        desc = s.find('h2', class_="title").text
        app = s.find('dd', class_="D1").text
        app = app.encode("utf-8")
        t = app.split()
        disp = s.find('span').text
        print '{:90s} {:17s} {:15s} '.format(desc, t[0], disp)




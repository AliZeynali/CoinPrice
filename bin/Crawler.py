import sys
import certifi
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import time


def getCoinPrices(address):
    coins = ['bitcoin', 'ethereum', 'ripple', 'bitcoin-cash', 'eos', 'litecoin', 'cardano', 'stellar', 'tron']
    site = urlopen(address, cafile=certifi.where()).read()
    soup = BeautifulSoup(site, "html.parser")
    slectors = []
    text = ""
    for coin in coins:
        s = "#id-" + coin + " > td:nth-of-type("
        h1 = soup.select(s + "8)")[0].text
        h24 = soup.select(s + "9)")[0].text
        # print("{0}:\t\t%1h : {1} ,\t %24h : {2}\t\t\t\t{3}".format(coin, h1,h24,datetime.datetime.today()))
        text += "{0}:\t\t%1h : {1} ,\t %24h : {2}\t\t\t\t{3}\n\n\n".format(coin, h1,h24,datetime.datetime.today())
    return text




if __name__ == "__main__":
    text  = getCoinPrices("https://coinmarketcap.com/all/views/all/")
    print(text)


def findElementsLinks(address):
    i = 1
    while True:
        site_url = address + "?page=" + str(i)
        try:
            open_site_url = urlopen(site_url).read()
            soup = BeautifulSoup(open_site_url, "html.parser")
            ctr = 1
            flag = False
            for link in soup.find_all('a', href=True):
                text = link['href']
                if text[5:12] == "details" and flag:
                    ctr += 1
                    file = open("LimitedLinks.txt", "a")
                    file.write("https://bama.ir" + text + "\n")
                    file.close()
                flag = not flag
            if ctr < 12:
                return
            for tt in soup.select("#content > div.leftpanel > div.paging-bottom-div.hidden-xs > h4"):
                text = tt.text
                splited = text.split(" ")
                if splited[5] == splited[7]:
                    return
            i += 1
        except (TimeoutError):
            i = i - 1
            continue

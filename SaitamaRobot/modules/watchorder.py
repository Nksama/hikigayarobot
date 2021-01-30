import requests
import re
from bs4 import BeautifulSoup as soup

def watchsearch(st):
    index = {}
    for i in range(1, 6):
        link = "https://chiaki.site/?/tools/watch_order_groups/type/popular/page/" + str(i)
        req = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        sou = soup(req.content, "html.parser")
        inde = sou.find_all('td', class_='uk-text-truncate')
        for j in range(len(inde)):
            x = inde[j].find("a").getText()
            y = "https://chiaki.site/" + inde[j].find("a").attrs["href"]
            index[x] = y
    ret = {}
    keys = list(index.keys())
    for i in range(len(keys)):
        ch = re.sub("\W+","",keys[i])
        st = re.sub("\W+","",st)
        if st.lower() in ch.lower():
            ret[keys[i]] = index[keys[i]]
    return ret

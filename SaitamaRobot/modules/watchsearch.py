import requests
import os
from bs4 import BeautifulSoup
import re

def filter_data(url):
	data = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	all_data = data.text
	soup = BeautifulSoup(all_data, features="lxml")
	title = []
	movie_data = []
	for line in soup.find_all('td',attrs={"class" : "uk-text-middle"}):
		title.append(str(line.text))
	movie_text = ""
	for movies_data in title:
		movie_text = movie_text + movies_data.replace('MAL', '')
	movie_text = movie_text.replace('\n\n\n', '')
	return movie_text

def watchsearch(st):
	index = {}
	for i in range(1, 6):
		link = "https://chiaki.site/?/tools/watch_order_groups/type/popular/page/" + str(i)
		req = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
		sou = BeautifulSoup(req.content, "html.parser")
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
	all_data_to_send = ""
	for keys_in in ret:
		all_data_to_send = all_data_to_send + filter_data(ret[keys_in])
	return all_data_to_send

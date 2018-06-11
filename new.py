#!/usr/bin/python3

import os
from bs4 import BeautifulSoup
import requests
import numpy as np

url = 'http://www.cricbuzz.com/cricket-match/live-scores'
wiki = requests.get(url)
soup = BeautifulSoup(wiki.text,'html.parser')

#print(soup.prettify())

match_update = soup.select('div > div > div > a ')
title_match = soup.select('div > div > div > h3 > a')




#print(type(title_match[3]))

#_____________________ to clean the title of the matches__________________________________________

title1=[]
title2=[]
for i in range(0,len(title_match)):
	title1.append(title_match[i].getText())
	title2.append(title1[i].replace(',',''))
	#print(title2[i])
	
#__________________operation complete_________________________________________________________


#___________________________ to clean the scores_________________________________________________

update_text=[]
striped_update_text=[]
final_update=[]


for i in range(0,len(title2)):
	update_text.append(match_update[i].getText())
	striped_update_text.append(update_text[i].strip())
	#print(y[i])
	if striped_update_text[i].lower()=='read preview':
		final_update.append('Match to be played')
	else:
		final_update.append(striped_update_text[i])


#____________________operation done__________________________________________________________




#________________________________________  print result_________________________________________

for i in range(0,len(title2)):
	print(title2[i])
	for j in range(0,len(title2)):
		if i==j:
			print(final_update[j])
print('')

#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request

website = "http://php.net"

# data downloading
web_data=urllib.request.urlopen(website)

#printing data
#print(web_data.read())


#reading web data with html tag
clean_data = web_data.read()


#applying library of HTML5 to scrape
get_clean = BeautifulSoup(clean_data,'html5lib')

# getting only text fromat data
final_data = get_clean.get_text()

#removing unnecessary spaces
good_data=final_data.strip().split()

print(good_data)


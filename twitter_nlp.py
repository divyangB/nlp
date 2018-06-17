#!/usr/bin/python3

#importing libraries
import tweepy
from tweepy import OAuthHandler #-------------for authorization--------
from textblob import TextBlob #---------------for analysis-------------
from bs4 import BeautifulSoup
import requests
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import string as sr
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as anim

stop_words = stopwords.words('english')
# credentials of twitter api
consumer_key = "Dppbvsr5N0XjObW21PlgOsAXG"
consumer_secret= "Ib19tsQcL1vijmqHgFCYm7IzeACv3VNJgWwbqLyQ27eLugqKCv"

access_key = "820116704718188544-wmhrXLSxDJ77IoEQXv3KFrVqU2bdf55" 
access_secret = "zkiXlMjzx4alTQHpKJ76VcGnoOrNkjpyCAq7D4shM4ZSS"

# authorising the twitter
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)

# connecting the api
connect = tweepy.API(auth)

# collecting the data
keyword = input('Enter the keyword you want to search: ')
get_data = connect.search(keyword,count=100)  # count can be max 100


# fetching tweets 
result=[]
for i in get_data:
	tweets = i.text
	# getting punctuation clean data
	clean_data = [j for j in tweets if j not in sr.punctuation]
	joined = ''.join(clean_data)
	tokenized_data = word_tokenize(joined)
	#print(tokenized_data)
	# removing stop words
	stop_clean_data = [i for i in tokenized_data if i.lower() not in stop_words]
	#print(stop_clean_data)
	join_stop = ' '.join(stop_clean_data)
	#print(join_stop)
	analysis = TextBlob(join_stop)
	result.append(analysis.sentiment[0])


pos=[]
neg=[]
neutral=[]
for i in result:
	if i<0.0:
		neg.append(i)
	elif i == 0.0:
		neutral.append(i)
	else:
		pos.append(i)
neg = len(neg)
pos = len(pos)
neutral =len(neutral)
	
print(neg,pos,neutral)
#x = ['sad','neutral','happy']
labels = ['sad','neutral','happy']
explode = (0,0,0.1)
colors = ['lightcoral','yellow','lightgreen']
y = [neg,neutral,pos]
plt.xlabel('sentiments')
plt.ylabel('frquency')
#plt.bar(x,y,label='emotions graph')
plt.pie(y, explode=explode, colors = colors, labels=labels, startangle=140, shadow=True , autopct ='%1.1f%%')
plt.axis('equal')
plt.legend()
plt.show()


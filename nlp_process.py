#!/usr/bin/python3

from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords

stopwords.words('english')
#print(a)

data1='hello this is me!! now going to have a tea break. pranav garg divyang'

token = word_tokenize(data1)
#print(token)

for i in token:
	if i in (stopwords.words('english')):
		token.remove(i)

print(token)


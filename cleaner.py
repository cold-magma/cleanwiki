from bs4 import BeautifulSoup as bs
from urllib import request
import time
import re

def clean(url):
	htdoc = request.urlopen(url)
	soup = bs(htdoc, "html.parser")

	out = soup.find("h1",{"class":"firstHeading"}).get_text()+ "\n\n"

	l = soup.find("div",{"class":"mw-parser-output"})

	for i in l.select("table"):
	    i.extract()
	    
	for i in l.select("style"):
	    i.extract()


	tempout = str(l)
	flag = True
	x=0
	while x<len(tempout):
	    if tempout[x]=="<":
	        if tempout[x+1]=="p":
	            out+="\n"
	        flag = True
	    elif flag and tempout[x]==">":
	        flag = False
	    else:
	        if not flag:
	            out+=tempout[x]
	    x+=1

	out = re.sub(r"\[\d+\]","",out)
	out = re.sub(r"\[edit\]","",out)
	out = re.sub(r"\[[A-Z]\]", "", out)
	out = re.sub(r"\[note [1234567890]*\]", "", out)

	return out
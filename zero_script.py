import urllib2
from BeautifulSoup import BeautifulSoup
import re
import win32api
import time

def check():
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	url = ('https://www.adafruit.com/products/2885')

	ourUrl = opener.open(url).read()

	#get html of url
	soup = BeautifulSoup(ourUrl)

	#get text
	checking = soup.find(text=re.compile("OUT OF STOCK"))

	if (checking != "OUT OF STOCK"):
		win32api.MessageBox(0, 'IN STOCK!!!!!', 'IN STOCK')
	else:
		print "Nothing - ",
		print time.ctime()
		time.sleep(120)
		check()

check()
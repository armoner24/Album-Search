'''input
cape
'''
import urllib2, cookielib, requests
from bs4 import BeautifulSoup
linkadd=['0-9','A-B','C-D','E-F','G-H','I-J','K-L','M-N','O-P','Q-R','S-T','U-V','W-X','Y-Z']
linkalpha=["http://www.princevault.com/index.php?title=A-Z_Songs_"]
linkbeta=["http://www.princevault.com/index.php?title=A-Z_Songs_"]
songs=[]
for i in linkadd:
	linkalpha.append(i)
	link=''.join(linkalpha)
	page=urllib2.urlopen(link)
	soup=BeautifulSoup(page,'html.parser')
	songnames=[]
	for content in soup.find_all("a"):
		for titles in content:
			songnames.append(titles)
	for i in range(30,len(songnames)-35,3):
		songs.append(songnames[i])
	linkalpha=linkbeta[::]
file=open("records.txt","w")
for i in songs:
	check='src='
	try:
		i=str(i.lower())
		if check not in i:
			file.write(i+"\n")
	except:
		file.write("null\n")
file.close()




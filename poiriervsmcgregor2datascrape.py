#scrape significant strikes by head, body, and leg and calculate accuracy (sig. str %)
import sys
sys.path.append('C:\\users\\revel\\anaconda3\\lib\\site-packages')

import requests
r = requests.get("http://www.ufcstats.com/fight-details/3d3e7dc7b4bf2bc4")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

#find the tables of the page
tableresults = soup.find_all('table', attrs = {'style': 'width: 745px'})

#work with the sig strikes table only and get the data
allsigstrikes = tableresults[-1].find_all('p', attrs = {'class': 'b-fight-details__table-text'})

strikenumbers = []

#create list of strike numbers
for i in range(6, 12):
	# ~ print (allsigstrikes[i].text)
	for j in allsigstrikes[i].text.split():
		if j.isdigit():
			strikenumbers.append(int(j))

strikepercents = []
count = 0
while count < len(strikenumbers):
	strikepercents.append("{:.0%}".format(strikenumbers[count] / strikenumbers[count + 1]))
	count += 2
	
poiriernum = strikepercents[::2]
mcgregornum = strikepercents[1::2]
targetlist = ["head", "body", "leg"]

for i in range(len(poiriernum)):
	print ("UFC 257: Poirier's significant", targetlist[i], "strike %:", poiriernum[i])

for i in range(len(mcgregornum)):
	print ("UFC 257: McGregor's significant", targetlist[i], "strike %:", mcgregornum[i])

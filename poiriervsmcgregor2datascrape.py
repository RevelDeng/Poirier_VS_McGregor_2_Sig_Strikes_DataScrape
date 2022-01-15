#scrape significant strikes by head, body, and leg and calculate accuracy (sig. str %) by round as well as total
import sys
sys.path.append('C:\\users\\revel\\anaconda3\\lib\\site-packages')

import requests
r = requests.get("http://www.ufcstats.com/fight-details/3d3e7dc7b4bf2bc4")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

#find the tables of the page
tableresults = soup.find_all('table', attrs = {'style': 'width: 745px'})
# ~ print (len(tableresults))

#work with the sig strikes table only and get the data
allsigstrikes = tableresults[-1].find_all('p', attrs = {'class': 'b-fight-details__table-text'})
# ~ print (len(allsigstrikes))

# ~ for i in allsigstrikes:
	# ~ print (i.text)

# ~ print (allsigstrikes[6:12])

strikenumbers = []

#create list of strike numbers
for i in range(6, 12):
	# ~ print (allsigstrikes[i].text)
	for j in allsigstrikes[i].text.split():
		if j.isdigit():
			strikenumbers.append(int(j))
			
# ~ print (strikenumbers)

strikepercents = []
count = 0
while count < len(strikenumbers):
	strikepercents.append("{:.0%}".format(strikenumbers[count] / strikenumbers[count + 1]))
	count += 2
	
# ~ print (strikepercents)

# ~ count2 = 0
# ~ while count2 < len(strikepercents):
	# ~ print ("Dustin Poirier
poiriernum = strikepercents[::2]
mcgregornum = strikepercents[1::2]
targetlist = ["head", "body", "leg"]

# ~ print (poiriernum, mcgregornum)

for i in range(len(poiriernum)):
	print ("UFC 257: Poirier's significant", targetlist[i], "strike %:", poiriernum[i])

for i in range(len(mcgregornum)):
	print ("UFC 257: McGregor's significant", targetlist[i], "strike %:", mcgregornum[i])

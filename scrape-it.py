# coding: utf8 #i'm pretty sure this did nothing
#the purpose of this script is to take a newline-separated list of bussinesses, google search them,
#extracting their city, province, phone number and website into a csv that can be opened in excel.

import requests, bs4, csv

outputFile = open('output.csv', 'w')
outputWriter = csv.writer(outputFile)

somestr = '''list of queries each on a new line, no utf8''' #for easy copy-pasting.
qstr = somestr.replace(' ','+')
qlst = qstr.split('\n') #if you prefer a different separator, specify it here

urlbase = 'https://www.google.ca/search?q='

for i in qlst:

	phone = '' #reset everything to an empty string so that if it can't find the data it will be a blank 'cell'
	num = ''
	webbutt = ''
	webadd = ''
	add = ''
	addsep = ['','','']
	city = ''
	prov = ''

	#print urlbase + i 		#debugging
	res = requests.get(urlbase+i)
	res.raise_for_status()
	currpage = bs4.BeautifulSoup(res.text)
	
	phone = currpage.select('span[class="_tA"]') #to find the selector for your desired fields, save the object as a file
													#and search that html for it cause it will be different from a modern browser
	if phone != []:
		for j in phone:
			if "-" in j.getText(): #if it has a dash its a phone number? seemed to work, surprisingly
				num = j.getText()
				print num
		
	webbutt = currpage.select('div[class="_IGf"] > a[class="fl"]')
	if webbutt != []:
		webadd = webbutt[0].get('href')
		
	add = currpage.select('span[class="_tA"]')
	if add != []:
		for k in add:
			if "," in k.getText():
				addsep = k.getText().split(', ')
				try:
					city = addsep[1] 
					#city = addsep[-2]	#city would prob be more accurate from the right, test this
					
				except IndexError: 
					print('bad city format')
				try:
					prov = addsep[2][:2]	#example target '22 Gore St E, Perth, ON K7H 1H5'
				except IndexError:
					print('bad prov format')
	try:
		outputWriter.writerow([i.replace('+', ' '), str(city), str(prov), str(num), str(webadd)]) #if something pulled from google is
	except UnicodeEncodeError:																	#in a bad format, i don't want an error
		print('encountered bad unichar')														#message, i much prefer it to move on.
																								#hence all the error catching.
	
outputFile.close()

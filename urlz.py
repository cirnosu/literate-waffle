#this file accompanies scrape-it.py
#
#the urls from scrape-it.py come out looking like the example I left in below in z; they need to be cleaned
#this script cleans those urls. it could probably be merged into scrape-it.py



z = '''/url?q=https://burnsjewellershop.com/&sa=U&ved=0ahUKEwiMl9yequnTAhUKxYMKHb65AVAQ_BcIbCgBMA4&usg=AFQjCNFIb93zvi04mRTJ20Kr75JsYsMTHQ
'''
#again newline-separated, copied right out of the csv that we opened in excel, including all blank lines that were blank in the output of scrape-it.py

x = z.split('\n')
y = []

for i in x:
	c = i
	if i != '':					#get the url part out
		a = i.rsplit('/', 1)
		b = a[0].split('=', 1)
		
		try:
			c = b[1]			#we don't need errors due to bad scrape data
		except IndexError:
			c = "bad url"		#maybe you want it to be a blank string instead? idc
		
	y.append(c)
	y.append('\n')
	
w = ''.join(y)					#output to a string that fits right up with the csv we copied from, paste this in its place.
print w
	
	
	
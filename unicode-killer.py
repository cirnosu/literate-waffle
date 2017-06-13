# BETA NOT TESTED YET

#ever felt like you wanted to kill something over encoding errors? a script like this can easily
#take zombie characters from a unicode file of web origin and make it readable and useable.

#replaces bad chars with a readable substitute for csv files

import csv

inputFile = open('infile.csv', 'r')
inputReader = csv.reader(inputFile)

outputFile = open('outfile.csv', 'w')
outputWriter = csv.writer(outputFile)

bad = {"Â®":'',
"&reg;":'',
"â„¢":'',
"Ã©":'e',
"Ã¨":'e',
"Ã§":'c',
"Ã´":'o',
"Ã¯":'i',
"â€“":'-',
"Ã¢":'a',
"É™":'e',
"â€™":"'",
"Ã‰":'E',
"ÃŽ":'I',
"Ã¼":'u',
"Å":'o'}

for row in inputReader:
	for i in bad.items():
		row = row.replace(key, value)
	outputWriter.writerow(row)
	
outputFile.close()
inputFile.close()

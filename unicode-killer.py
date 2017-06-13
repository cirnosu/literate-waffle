#replaces bad chars with a readable substitute

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
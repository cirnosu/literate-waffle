print("Welcome to letter counter! \n")
workingText = input("Enter in text to be processed: ") #get the sample text

chrlst = [0] * 130 #initialize a list to hold the data

for i in range(len(workingText)): #itterate thru text
    lttr = ord(workingText[i])  #index of list corresponds to ascii of character
    chrlst[lttr] += 1           #value at that index increases for each letter
    
for j in range(len(chrlst)):    #itterate through data
    if chrlst[j] != 0:          #only output results for characters that were found
        print( chr(j) + ": " + str(chrlst[j])) #convert the index to its corresponding character and also print its value found
        

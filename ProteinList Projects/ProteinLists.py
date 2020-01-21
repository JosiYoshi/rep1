#ProteinLists.py
#Program making protein sequences easier to retrieve

import os
import csv
import pandas as pd

List = []
col = 0
cat =''


#function to search for something in data

def fileOpen(search):
	print (search)
	count =1
	lists = ['sequence', 'type', 'origin Line', 'name', 'organism', 'more info', 'link']
	
	#if search in lists:
	#	ind = lists.index(search)
	#else:
	#	ind = None
	#	print ('not in list')
	data = pd.read_csv('Protein Sequences.csv')
	print (data.head())
	df = pd.DataFrame(data)
	print(df)

	print (df.loc[ : , search])

	nextStep = input('To see information enter data\'s number (number on left)  ')

	print (df.loc[int(nextStep), :])



def addFunc():
    
    fileName = 'Protein Sequences - Sheet1.csv'
    outFile = open(fileName, 'a')
    again = 'y'
    
    while (again == 'y'):
        partOfSequence = str(input("Enter the part of sequence: "))
        typeOfProtein = str(input("Enter the type of protein: "))
        originLine = str(input("Enter the origin line: "))
        proteinName = str(input("Enter the protein name: "))
        organism = str(input("Enter organism name: "))
        moreInfo = str(input("Enter notes and or more information: "))
        link = str(input("Enter the link to the original data source: "))
        outFile.write(partOfSequence + "," + typeOfProtein + "," + originLine + "," + proteinName + "," + organism + "," + moreInfo + "," + link +"\n")
        
        
        again =input("To continue entering data into the spreadsheet type y  otherwise type n: ")
	
    outFile.close()


'''
In find function add prompt for the search they want
'''

#open file where provided data is
#only use below line for project
def find(search):
	if search == 'Organism':
		fileOpen(search)
		
	else: 
		if search == 'Type':
			fileOpen(search)

			
		else:
			if search== 'Name':
				fileOpen(search)

				

			else:
				if search == 'Other':
					add = input('Would you like to add data(for yes enter y)?\n')
					if add == 'y':
						addFunc()
					else:
						run()
					
#program title and intro

def run():
	print ("********************\n\nProtein List\n\n*********************")
	print ('Our list will ease your basic projects when it comes to looking up protein sequences.')




#make into pop up window?
#program instructions
#may want to use buttons once learned

	print ('Begin your search by entering one of the options\n(*Options are case sensitive*)\n')

#create list or get data from spreadsheet
#acces data with use of data structures TBD
#for now  search by either entering one of the critiria ('organism','part of sequence'),'type of protein','protein name', 'other keywords', 'or other option where user knows which one exactly'
	
	search = input('Options: \nOrganism\nType\nName\nOther\nInput Here:\n')
#after user adds input, list his options for what they have
#use for loop or cases to give the leist for each option
	print (search)



	scriptDir = os.getcwd()
	print (scriptDir)

	find(search)



run()






			




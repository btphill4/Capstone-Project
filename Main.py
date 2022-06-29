# To Do:
# 1) import proper CVS files 
# 2) create arrays that hold values for HomeOwner and Tenants
# 3) add functions for each match
#
# Team notes:
# - We might want to create classes/objects to hold the values
# - numpy might be useful for array matching but using sets (intersection) currently works




# Import Numpy for np.isin array functions
# Install with linux command: pip install numpy
import numpy as np
from Methods import *
# ~~~~~~~~~~~ Import CVS Here (To be updated with better method) ~~~~~~~~~~~ #
# Import template
import csv

# Store imported data in an empty array imported
importedDB = []

# Figure out how to change the path for it to work on all machines
with open("/home/brandon/Desktop/business.csv", 'r') as businessFile:
    rows = csv.reader(businessFile, delimiter=',')
    for r in rows:
        # append(r[0]) get first column, append(r[1]) gets 2nd column etc
        importedDB.append(r[1])
        # print(r)

# ~~~~~~ CSV is now imported and added to array(imported) ~~~~~~ #

# Print entire DB: 
# print(imported)

# Print specific index:
#print(importedDB[100])

#test function to check Methods.py methods:
#testFunction() 

# ~~~~~~~~~~Matching starts here~~~~~~~~~~ #

# Copy omportedDB to a tempDB to not alter the list
tempDB = importedDB

matchedDB = []

#print to Test that the DB was copied
#print(tempDB[1])


# ~~~~~~~~~~~ match rent function ~~~~~~~~~~~ #
# Checks for intersection between HO_rentDB_Set and TEN_rentDB_Set
# If it found an intersection - add to matched
# else do nothing -> print not match for testing
HO_rentDB = [700]
HO_rentDB_set = set(HO_rentDB)
TEN_rentDB = [700]
TEN_rentDB_set = set(TEN_rentDB)

def match_rent():
    # Testing Print Statement
    #print("match_rent function()")

    # Checks if values of testingRentDB are in rentDB (using numpy)
    #np.isin(testingRentDB[0], rentDB[0])
    
    #if match is found
    if HO_rentDB_set.intersection(TEN_rentDB_set):
        #Print if found (testing)
        print("RENT MATCHED")

        # add to matchedDB
        global matchedDB, HO_rentDB 
        matchedDB = matchedDB + HO_rentDB

        #print updated matchedDB (testing)
        #print(matchedDB)

    #if match is not found     
    else:
        # Print if not found (Testing)
        print("RENT NOT MATCHED")

    # print(rentDB)
# end match_rent()



match_rent()
print(matchedDB)


# Create DB for Cities and add them to sets for (testing change with multi-dimensional array)
HO_cityDB = ['Phoenix']
HO_cityDB_Set = set(HO_cityDB)
TEN_tempCityDB = ['Glendale']
TEN_tempCityDB_Set = set(TEN_tempCityDB)


# City Matching Function
def match_City():
    # for cityDB in cityDB:
    # if tempCityDB == 'Glendale':
    # print('MATCH')
    if set(HO_cityDB_Set).intersection(TEN_tempCityDB_Set):
        print("CITY MATCH")

        # add to the matched array
    else:
        print("NO City Match")
#end match_city()

# Run match_City()
match_City()

# To Do:
# 1) import proper CVS files 
# 2) create arrays that hold values for HomeOwner and Tenants
# 3) add functions for each match
#
# Team notes:
# - We might want to create classes/objects to hold the values
# - numpy might be useful for array matching but using sets (intersection) currently works




# Import Numpy for np.isin array functions
from nis import match
import numpy as np
from Match_Methods import *
# os for importing files
import os
import sys
# ~~~~~~~~~~~ Import CVS Here (To be updated with better method) ~~~~~~~~~~~ #
# Import template
import csv

# Store imported data in an empty array imported
importedTenDB = []
importedHODB = []

# Figure out how to change the path for it to work on all machines
with open(os.path.join(sys.path[0], "Tenantdb.csv"), 'r') as TenantDB:
    rows = csv.reader(TenantDB, delimiter=',')
    for r in rows:
        # append(r[0]) get first column, append(r[1]) gets 2nd column etc
        importedTenDB.append(r[1])
        # print(r)


# Figure out how to change the path for it to work on all machines
with open(os.path.join(sys.path[0], "HomeOwnerdb.csv"), 'r') as HomeOwnerDB:
    rows = csv.reader(HomeOwnerDB, delimiter=',')
    for r in rows:
        # append(r[0]) get first column, append(r[1]) gets 2nd column etc
        importedHODB.append(r[1])
        # print(r)

# ~~~~~~ CSV is now imported and added to arrays(importedHODB, importedTenDB) ~~~~~~ #

# Print entire DB: 
print(importedHODB)
print(importedTenDB)

# Print specific index:
#print(importedDB[100])

#test function to check Methods.py methods:
#testFunction() 

# ~~~~~~~~~~Matching starts here~~~~~~~~~~ #

# Copy omportedDB to a tempDB to not alter the list
tempTenantDB = importedTenDB
tempHomeOwnerDB = importedHODB
matchedDB = []

#print to Test that the DB was copied
#print(tempDB[1])


# ~~~~~~~~~~ Most Important Questions ~~~~~~~~~~ #

# Q6: workSchedule
match_workSchedule()

# Q7: city
#Temp Values (WILL BE REMOVED)
# Create DB for Cities and add them to sets for (testing change with multi-dimensional array)
HO_cityDB = ['Phoenix']
TEN_tempCityDB = ['Glendale']
TEN_tempCityDB_1 = ['Phoenix']

# Run match_City() EXAMPLES
match_city(HO_cityDB, TEN_tempCityDB)   #fail
match_city(HO_cityDB, TEN_tempCityDB_1) #pass

# Q10: Rent
#Testing values (WILL BE REMOVED)
HO_rentDB = [700]
TEN_rentDB = [700]

# Run match_rent()
match_rent(HO_rentDB, TEN_rentDB)

# Q14: Open to living with kids
match_livingWithKids()

# Q13: Do you have kids
match_HaveKids()

# Q16: Open to living with pets
#Teasting Values 
boolLivingPets_TEN = True
boolLivingPets_HO = True

match_livingWithPets(boolLivingPets_HO, boolLivingPets_TEN)
# Q15: Do you have pets
# Testing Values
boolHavePets_TEN = True
boolHavePets_HO = True
petTypes_HO = ["dog", "cat", "lizard"]
petTypes_TEN = ["dog", "cat"]
match_HavePets()

# Q17: Move in date
match_MoveDate()

# Q12: Lease Type
match_leaseType()

# ~~~~~~~~~~ Medium Important Questions ~~~~~~~~~~ #

# Q8: Neighborhood Preference
match_neighborhoodPref()

# Q9: Max number of housemates (1 to 5+)
match_MaxRoomates()

# Q11: Age of roomates
match_AgeRange()

# Q19: Type of social enviroment
match_SocialEnviroment()

# Q20: Scale 1-5 amenities
match_amenitiesImportance()

# Q24: Rate yourself cleanliness
match_rateYourself()

# Q26: Rate your roomates
match_RateOthers()

# Q28: Tell us about yourself
match_TellUs()

# ~~~~~~~~~~ Low Important Questions ~~~~~~~~~~ #

# Q18: Personality
match_personality()

# Q21: Ideal friday night
match_FridayNight()

# Q27: Hobbies/free time
match_hobbies()


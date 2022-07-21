# Import Numpy for np.isin array functions
from nis import match
#import numpy as np
from Match_Methods import *
from Tenant import *
from pprint import pprint
# os for importing files
import os
import sys
# ~~~~~~~~~~~ Import CVS Here (To be updated with better method) ~~~~~~~~~~~ #
# Import template
import csv

# Connects to DB and saves to HO_list
HO_list = db_connect()
ex_Ten = Tenant(1, 'Phoenix', 600, 900, 'lease', 6, True, 6, 
                True, True, 'Dog', True, 'cat', 'Jan 2023',
                 'what do you do', 'neighborhood', 3, '18-21', 'peace and quiet', 
                1, 3, 5, 4, 5, 3, 5, 4, 3, 2,
                2, 3, 1, 4, 5, 1, 2, '', 
                1, 1, 1, 0, 1, 0, 0, 0, 1, 0, '', 0)

ex_HO = HomeOwner(2, 'Phoenix', 600, 900, 'lease', 6, True, 6, 
                True, True, 'cat', True, 'dog', 'Feb 2023',
                 '', '', 3, '18-21', 'peace and quiet', 
                1, 3, 5, 4, 5, 3, 5, 4, 3, 2,
                2, 3, 1, 4, 5, 1, 2, '', 
                1, 1, 1, 0, 1, 0, 0, 0, 1, 0, '', 0)

ex_HO_1 = HomeOwner(3, 'Glendale', 1000, 2000, 'rent', 0, False, 0, 
                False, False, '', False, '', 'Jan 2023',
                 'what do you do', 'neighborhood', 3, '18-21', 'peace and quiet', 
                1, 3, 5, 4, 5, 3, 5, 4, 3, 2,
                2, 3, 1, 4, 5, 1, 2, '', 
                1, 1, 1, 0, 1, 0, 0, 0, 1, 0, '', 0)


#Home OWners added to a list
list_of_HO = []
list_of_HO.append(ex_HO)
list_of_HO.append(ex_HO_1)


# Show that db_connect() works
#print_list_index(HO_list, 1)
#print_list_all(HO_list)

#Print specific Values 
#print("ex_Ten.appid: ", ex_Ten.appid, '\n\n')

#pprint(vars(ex_Ten))
#pprint(vars(ex_HO))

# Matching Methods Start Here

#~~~~~~~~~~ Most important Questions ~~~~~~~~~~#
#work schedule
#match_workSchedule(ex_Ten, ex_HO)

# City Matching
match_city(ex_Ten, ex_HO)   #Pass
match_city(ex_Ten, ex_HO_1) #Fail

#Match Rent
match_rent(ex_Ten,ex_HO)    #Pass
match_rent(ex_Ten, ex_HO_1) #Fail

match_livingWithKids(ex_Ten, ex_HO) #Fail
match_livingWithKids(ex_Ten, ex_HO_1) #Pass

match_HaveKids(ex_Ten, ex_HO)
match_HaveKids(ex_Ten, ex_HO_1)

match_livingWithPets(ex_Ten, ex_HO)
match_livingWithPets(ex_Ten, ex_HO_1)

match_HavePets(ex_Ten, ex_HO)
match_HavePets(ex_Ten, ex_HO_1)

match_MoveDate(ex_Ten, ex_HO)
match_MoveDate(ex_Ten, ex_HO_1)

#~~~~~~~~~~ Medium Importance Questions ~~~~~~~~~~#



#~~~~~~~~~~ Low Importance Questions ~~~~~~~~~~#

match_personality()
match_FridayNight(ex_Ten, ex_HO)


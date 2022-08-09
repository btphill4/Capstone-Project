# Import Numpy for np.isin array functions
from nis import match

from psycopg2 import connect
#import numpy as np
from Match_Methods import *
from Tenant import *
from pprint import pprint

# ~~~~~~~~~~~ Import CVS Here (To be updated with better method) ~~~~~~~~~~~ #
# Import template
import csv

# Connects to DB and saves to HO_list
db_con = connect_to_db()
cursor = db_con.cursor()

# getting column names
columns_db(cursor)
col = [desc[0] for desc in cursor.description]


#### Controls which tenant is used for matching ####
tenant_id = 1
#### 

# gets tenant information
tenant_db(tenant_id, cursor)
item = cursor.fetchone()
curr = dict(zip(col, item))

# get tenant : last parameter is matchpercent
ex_Ten = Tenant(curr[col[0]], curr[col[1]],curr[col[2]], curr[col[3]], curr[col[4]],
    curr[col[5]], curr[col[6]], curr[col[7]],curr[col[8]], curr[col[9]], curr[col[10]],
    curr[col[11]], curr[col[12]], curr[col[13]], curr[col[14]], curr[col[15]], curr[col[16]],
    curr[col[17]], curr[col[18]], curr[col[19]], curr[col[20]], curr[col[21]], curr[col[22]],
    curr[col[23]], curr[col[24]], curr[col[25]], curr[col[26]], curr[col[27]], curr[col[28]], 
    curr[col[29]], curr[col[30]], curr[col[31]], curr[col[32]], curr[col[33]], curr[col[34]], 
    curr[col[35]], curr[col[36]], curr[col[37]], curr[col[38]], curr[col[39]], curr[col[40]], 
    curr[col[41]], curr[col[42]], curr[col[43]], curr[col[44]], curr[col[45]], curr[col[46]], 
    curr[col[47]], curr[col[48]], curr[col[49]], curr[col[50]], curr[col[51]], curr[col[52]], 
    curr[col[53]], curr[col[54]], curr[col[55]], curr[col[56]], curr[col[57]], curr[col[58]], 
    curr[col[59]], curr[col[60]], 0)

# gets list of homeowner ids that match city and rent range
initial_filter_db(tenant_id, cursor) 
howner_list = cursor.fetchall()

# loop for matching with homeowner list
for uid in howner_list:
    homeowner_db(uid[0], cursor)
    item = cursor.fetchone()
    
    curr = dict(zip(col, item))

    # last parameter is match percent
    ex_HO = HomeOwner(curr[col[0]], curr[col[1]],curr[col[2]], curr[col[3]], curr[col[4]],
    curr[col[5]], curr[col[6]], curr[col[7]],curr[col[8]], curr[col[9]], curr[col[10]],
    curr[col[11]], curr[col[12]], curr[col[13]], curr[col[14]], curr[col[15]], curr[col[16]],
    curr[col[17]], curr[col[18]], curr[col[19]], curr[col[20]], curr[col[21]], curr[col[22]],
    curr[col[23]], curr[col[24]], curr[col[25]], curr[col[26]], curr[col[27]], curr[col[28]], 
    curr[col[29]], curr[col[30]], curr[col[31]], curr[col[32]], curr[col[33]], curr[col[34]], 
    curr[col[35]], curr[col[36]], curr[col[37]], curr[col[38]], curr[col[39]], curr[col[40]], 
    curr[col[41]], curr[col[42]], curr[col[43]], curr[col[44]], curr[col[45]], curr[col[46]], 
    curr[col[47]], curr[col[48]], curr[col[49]], curr[col[50]], curr[col[51]], curr[col[52]], 
    curr[col[53]], curr[col[54]], curr[col[55]], curr[col[56]], curr[col[57]], curr[col[58]], 
    curr[col[59]], curr[col[60]], 0)

    print("""\n##########       START OF RESULTS       ##########\n""")

    #~~~~~~~~~~ Most important Questions ~~~~~~~~~~#
    print("Tenant ID:", ex_Ten.appid)
    print("HomeOwner ID: ", ex_HO.appid, '\n')
    match_city(ex_Ten, ex_HO)   #Pass
    #match_rent(ex_Ten,ex_HO)    #Pass
    match_livingWithKids(ex_Ten, ex_HO)
    match_HaveKids(ex_Ten, ex_HO)
    match_livingWithPets(ex_Ten, ex_HO)
    match_HavePets(ex_Ten, ex_HO)
    match_MoveDate(ex_Ten, ex_HO)
    match_leaseType(ex_Ten, ex_HO)

    #~~~~~~~~~~ Medium Importance Questions ~~~~~~~~~~#

    match_neighborhoodPref(ex_Ten, ex_HO)
    match_MaxRoomates(ex_Ten, ex_HO)
    match_AgeRange(ex_Ten, ex_HO)
    match_SocialEnvironment(ex_Ten, ex_HO)
    match_amenitiesImportance(ex_Ten, ex_HO)
    match_rateYourself(ex_Ten, ex_HO)
    match_RateOthers(ex_Ten, ex_HO)
    match_TellUs(ex_Ten, ex_HO)

    #~~~~~~~~~~ Low Importance Questions ~~~~~~~~~~#

    match_personality(ex_Ten, ex_HO)
    match_FridayNight(ex_Ten, ex_HO)
    match_hobbies(ex_Ten, ex_HO)
    
    print("\n TOTAL MATCH PERCENT for Homeowner", ex_HO.appid, ":", ex_HO.matchPercent)
    print("""\n##########       END OF RESULTS       ##########\n""")

    
#HO_list = db_connect()
#ex_Ten = Tenant(1, 'Phoenix', 600, 900, 'lease', 6, True, 8, 
#                True, True, 'Dog', True, 'cat', 'Jan 2023',
#                 'what do you do', 'neighborhood', 3, '18-20', 'peace and quiet', 
#                1, 3, 5, 4, 5, 3, 5, 4, 3, 2,
#                2, 3, 1, 4, 5, 1, 2, 'additional info for ex_Ten', 
#                1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 'Camping', 0)

#ex_HO = HomeOwner(2, 'Phoenix', 600, 900, 'lease', 6, True, 6, 
#                True, True, 'cat', True, 'dog', 'Feb 2023',
#                 'what do you do2', 'neighborhood2', 3, '21-30', 'peace and quiet', 
#                1, 2, 3, 4, 5, 3, 5, 2, 1, 3,
#                1, 5, 5, 1, 5, 1, 2, 'additional info for ex_HO', 
#                1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 'Camping', 0)

#ex_HO_1 = HomeOwner(3, 'Glendale', 1000, 2000, 'rent', 0, False, 0, 
#                False, False, '', False, '', 'Jan 2023',
#                 'what do you do', 'neighborhood', 3, '18-20', 'someone I can talk to and hang out with', 
#                1, 3, 3, 4, 5, 3, 5, 4, 1, 2,
#                2, 3, 1, 4, 5, 1, 2, 'additional info for ex_HO_1', 
#                1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 'Fishing', 0)



#Home OWners added to a list
#list_of_HO = []
#list_of_HO.append(ex_HO)
#list_of_HO.append(ex_HO_1)


# Show that db_connect() works
#print_list_index(HO_list, 1)
#print_list_all(HO_list)

#Print specific Values 
#print("ex_Ten.appid: ", ex_Ten.appid, '\n\n')

#pprint(vars(ex_Ten))
#pprint(vars(ex_HO))

# Matching Methods Start Here
#print()
#~~~~~~~~~~ Most important Questions ~~~~~~~~~~#
#work schedule
#match_workSchedule(ex_Ten, ex_HO)

# City Matching
#match_city(ex_Ten, ex_HO)   #Pass
#match_city(ex_Ten, ex_HO_1) #Fail

#Match Rent
#match_rent(ex_Ten,ex_HO)    #Pass
#match_rent(ex_Ten, ex_HO_1) #Fail

#match_livingWithKids(ex_Ten, ex_HO)
#match_livingWithKids(ex_Ten, ex_HO_1)

#match_HaveKids(ex_Ten, ex_HO)
#match_HaveKids(ex_Ten, ex_HO_1)

#match_livingWithPets(ex_Ten, ex_HO)
#match_livingWithPets(ex_Ten, ex_HO_1)

#match_HavePets(ex_Ten, ex_HO)
#match_HavePets(ex_Ten, ex_HO_1)

#match_MoveDate(ex_Ten, ex_HO)
#match_MoveDate(ex_Ten, ex_HO_1)

#match_leaseType(ex_Ten, ex_HO)
#match_leaseType(ex_Ten, ex_HO_1)

#~~~~~~~~~~ Medium Importance Questions ~~~~~~~~~~#
#match_neighborhoodPref(ex_Ten, ex_HO)
#match_neighborhoodPref(ex_Ten, ex_HO_1)

#match_MaxRoomates(ex_Ten, ex_HO)
#match_MaxRoomates(ex_Ten, ex_HO_1)

#match_AgeRange(ex_Ten, ex_HO)
#match_AgeRange(ex_Ten, ex_HO_1)

#match_SocialEnviroment(ex_Ten, ex_HO)
#match_SocialEnviroment(ex_Ten, ex_HO_1)

#match_amenitiesImportance(ex_Ten, ex_HO)
#match_amenitiesImportance(ex_Ten, ex_HO_1)

#match_rateYourself(ex_Ten, ex_HO)
#match_rateYourself(ex_Ten, ex_HO_1)

#match_RateOthers(ex_Ten, ex_HO)
#match_RateOthers(ex_Ten, ex_HO_1)

#match_TellUs(ex_Ten, ex_HO)
#match_TellUs(ex_Ten, ex_HO_1)

#~~~~~~~~~~ Low Importance Questions ~~~~~~~~~~#

#match_personality(ex_Ten, ex_HO)
#match_personality(ex_Ten, ex_HO_1)

#match_FridayNight(ex_Ten, ex_HO)
#match_FridayNight(ex_Ten, ex_HO_1)

#match_hobbies(ex_Ten, ex_HO)
#match_hobbies(ex_Ten, ex_HO_1)

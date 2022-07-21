# File to hold our methods

# Import Database Connection Library 
import psycopg2 

# Import natural language toolkit library
import nltk

#Imports db_connect() from 
from prototype.dbconnect import *
from Tenant import *
from HomeOwners import *

#From dbconnect.py
list1 = db_connect()
#print(list1[2])

#Global matchedDB array
global matchedDB
matchedDB = []


#Test function to ensure the file working
def testFunction():
    print("Printing Test function")

#~~~~~~~~~ Database Methods ~~~~~~~~~#

# must be called first to connect to database, returns a connection object
def connect_to_db():
    # Database host is database address
    # Database name is name of database
    db_host = "ec2-54-165-90-230.compute-1.amazonaws.com"
    db_name = "d6hp3i25m6gslc"

    # Data base username/pass
    db_user = "uqqcowyaruajrk"
    db_pass = "e8828f90c6df41a82eac46bcb552a9cdf32a5b109db1d72ec7cb9ad988030475"
    db_port = 5432

    connect = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_pass, port=db_port)
    return connect

# parameter: an integer representing the ID of the tenant who needs to match with homeowners
# returns a list of ids that match the city and rent range
def initial_filter_db(id):
    print("hi")

def print_list_index(list, x):
    print(list[x], '/n')

def print_list_all(lists):
    print("Entire list: ")
    print(*lists, sep = '\n\n')
    print("\n\n")
#~~~~~~~~~ Matching METHODS ~~~~~~~~~#

#~~~~~~~~~~ Most important Questions ~~~~~~~~~~#

# 6. What are your typical workday hours and days of the week? Please fill out in the boxes below as such (for example: 9-5, 9am-5pm)
# Input: Range of numbers(hours) and string days

def match_workSchedule():
    print("Match Work Schedule")

#end match_workSchedule():

# 7. In which city are you looking to rent? HANDLED WITH SQL
# Input: string

def match_city(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match city function: ")

    if ex_Ten.city == ex_HO.city:
        #match is good
        print("City MATCHED for Tenant ID #: ",
                ex_Ten.appid, " and HomeOwner ID #: ", 
                ex_HO.appid)

        # Add to matched DB
        #global matchedDB 
        #matchedDB = matchedDB + ex_HO
    else:
        print("City NOT MATCHED for Tenant ID #: ",
                ex_Ten.appid, " and HomeOwner ID #: ", 
                ex_HO.appid)

# 10. What is the monthly rent range you are looking to pay? HANDLED WITH SQL
# Input: Range of Numbers 

# ~~~~~~~~~~~ match rent function ~~~~~~~~~~~ #
# Checks for intersection between HO_rentDB_Set and TEN_rentDB_Set
# If it found an intersection - add to matched
# else do nothing -> print not match for testing
def match_rent(ex_Ten: Tenant, ex_HO: HomeOwner):
    # Testing Print Statement
    print("match_rent function(): ")

    
    # Print Temp sets (Testing)
#    print("HO_rent_set: ", HO_rent_set)
#    print("TEN_rent_set: ", TEN_rent_set)

    #if match is found
    if HO_rent_set.intersection(TEN_rent_set):
        #Print if found (testing)
        print("RENT MATCHED")

        # add to matchedDB
#        global matchedDB, HO_rentDB 
#        matchedDB = matchedDB + HO_rentDB

        # print updated matchedDB (testing)
#        print(matchedDB)

    #if match is not found     
    else:
        # Print if not found (Testing)
        print("RENT NOT MATCHED")

#     print(matchedDB)
# end match_rent()

# 14. Are you open to living with someone who may have children?
# Input: Bool (Yes/No)

def match_livingWithKids():
    print("Match living with kids")

#end match_livingWithKids()

# 13. Do you have any children? 
# Input: Bool (Yes/No), if yes number input age numbers
def match_HaveKids():
    print("Match Have Kids")
#end match_HaveKids()

# 16. Are you open to living with someone who has pets? 
# Input: Bool

def match_livingWithPets(boolLivingPets_HO, boolLivingPets_TEN):
    # Testing function print
#    print("living with pets")

    #if they are equal, they match
    if boolLivingPets_HO == boolLivingPets_TEN:
        print("Living with pets MATCHED")
    #add to matched array

    else: 
        print("Living with pets NOT MATCHED")

#end match_livingWithPets()

# 15. Do you have any pets?
# Input: Bool (Yes/No) if yes number input of # of pets and string of types
def match_HavePets(boolHavePets_HO, boolHavePets_TEN, petTypes_HO, petTypes_TEN):
    # Testing Function print   
#    print("match have pets")

    #if they are equal, they match
    if boolHavePets_HO == True:
        #for i in petTypes_HO:
            #print(petTypes_HO[i])
        print("HomeOwner pets: ", petTypes_HO)
    if boolHavePets_TEN == True:
        #for i in petTypes_TEN:
            #print(petTypes_HO[i])
        print("Tenant pets: ", petTypes_TEN)
    #add to matched array

    else: 
        print("Living with pets NOT MATCHED/HAVE NO PETS")

#end match_HavePets()

# 17. When would you like to move in?
# Input: string(month) and number(year) -> Jan 2023
# Notes: we might be able to use a python library to return number values or something
def match_MoveDate():
    print("Match move date")
#end match_MoveDate()

# 12. Would you like to rent month to month or on a lease basis?
# Input: either month-to-month or Lease basis, if lease basis number input for how long
def match_leaseType(leaseType1, leaseType2):
    #Initial testing print
#    print("Match lease type")
    if leaseType1 == leaseType2:
        print("Lease type MATCHED")
    else:
        print("Lease type NOT MATCHED")
#end match_leaseType():


#~~~~~~~~~~ Medium Importance Questions ~~~~~~~~~~#

# 8. Is there a preferred neighborhood you would like to rent within your specified area?
# Input: String
def match_neighborhoodPref():
    print("Match Neighborhood")
#end match_neighborhoodPref()

# 9. What is the maximum number of housemates you are willing to live with?
# Input: 1, 2, 3, 4, 5, 5+
def match_MaxRoomates():
    print("Match max roomates")
#end match_MaxRoomates():

# 11. Please give us a range for the age of the women you would like to co-live with or type “does not matter”
# Input: Range of numbers(might be check box), or string "does not matter"
# Current Ranges: 18-20, 21-30, 31-40, 41-50, 50+
def match_AgeRange():
    print("Match age range")
#end match ageRange()

# 19. What environment would be ideal for you?
# Input: string: peace and quiet, or someone I can talk to and hang out with, or other
# Note: Natural Language toolkit for other?
def match_SocialEnviroment():
    print("Match social enviroment")
#end match_SocialEnviroment()

# 20. On a scale of 1-5 how would you rate the importance of the following?
    # Furnished room
    # Parking
    # Gym
# Input: Range of numbers 1 to 5
# Note: subtract tenant number from home owner number and smaller number better match 
# 0 = 100% 
# 1 = 80%
# 2 = 60% ...
def match_amenitiesImportance():
    print("match amenities importance")
#end match_amenitiesImporance()

# 24. On a scale of 1-5 how would you rate YOURSELF for each of the following:
    #Kitchen use
    #Neatness
    #Kitchen cleanliness
    #Guests often visit
    #Household Cleanliness
    #Recreational Cannabis
    #Smoking
# Input: Range of numbers 1 to 5
# Note: subtract tenant number from home owner number, add all together and divide by 6 and smaller number better match 
# 0 = 100% 
# 1 = 80%
# 2 = 60% ...
def match_rateYourself():
    print("match_RateYourself")
#end match_rateYourself():

# 26. On a scale of 1-5 how would you like your HOUSEMATE to rate for each of the following:
#    Kitchen use
#    Neatness
#    Kitchen cleanliness
#    Guests often visit
#    Household Cleanliness
#    Recreational Cannabis
#    Smoking
# Input: Range of numbers 1 to 5
# Note: subtract tenant number from home owner number, add all together and divide by 6 and smaller number better match 
# 0 = 100% 
# 1 = 80%
# 2 = 60% ...
def match_RateOthers():
    print("Match Rate others")
#end match_rateOthers()

# 28. What else would you like us to know about you or about your future housemate(s)?
# Input: String
# Note: Natural Language Toolkit?
def match_TellUs():
    print("Match Tell us")
#end match_TellUs()


#~~~~~~~~~~ Low Importance Questions ~~~~~~~~~~#
# 18. Which term best describes your personality? Check all that apply.
    #Carefree
    #Outgoing
    #Laid back
    #Other (please specify)
# Input: check box or string other
def match_personality():
    print("match personality")
#end match_personality()

# 21. What does your ideal Friday night look like? Please check all boxes that apply.
#    Movie night with friends/housemates
#    Night out
#    Bar hopping
#    Self-care night to wind down
#    Netflix
#    Other (please specify)
# Input: Checkbox, string other
# Note: can make 0 or 1 values for checked/not checked and test equality
def match_FridayNight(ex_Tenant: Tenant, ex_HO: HomeOwner):
    print("match friday night: ")

    if ex_Tenant.q21_1 == ex_HO.q21_1:
        #match is good
        print("FRIDAY NIGHT Q21_1 MATCHED")

    else:
        print("FRIDAY NIGHT NOT MATCHED")
#end match_FridayNight()

# 27. Please let us know your favorite hobbies, and what you do on your days off for enjoyment.
# Input: String
# Note: Natural Language Toolkit, not sure how to approach this one
def match_hobbies():
    print("match hobbies")
#end match_hobbies()

#~~~~~~~~~ END Matching METHODS ~~~~~~~~~#


def print_matchedDB():
    print('\n\n', matchedDB)







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

# Input 1: an integer representing the ID of the tenant who needs to match with homeowners
# Input 2: a cursor object from the connection object
# Returns: nothing but it edits the cursor object
def initial_filter_db(id, cursor):
    cursor.execute(get_sql_query(id))

# Input 1: an integer representing the ID of the tenant who needs to match with homeowners
# Input 2: a cursor object from the connection object
# Returns: nothing but it edits the cursor object
def homeowner_db(id, cursor):
    cursor.execute(get_sql_homeowner(id))

# Input 1: an integer representing the ID of the tenant who needs to match with homeowners
# Input 2: a cursor object from the connection object
# Returns: nothing but it edits the cursor object
def tenant_db(id, cursor):
    cursor.execute(get_sql_tenant(id))

# Input 1: a cursor object from the connection object
# Returns: nothing but it edits the cursor object
def columns_db(cursor):
    cursor.execute(get_sql_col_names())

# Input: an intteger representing the ID of the tenant
# Returns: sql command in string form to get tenant ID
def get_sql_tenant(id):
    sql_query = """
    SELECT *
    FROM tenantapp
    WHERE appid="""
    return sql_query + str(id)

# Input 1: an integer representing the ID of the homeowner
# Input 2: a cursor object from the connection object
# Returns: the sql command to get the homeowner information
def get_sql_homeowner(id):
    sql_query = """
    SELECT *
    FROM homeownerapp
    WHERE appid="""
    return sql_query + str(id)

# Input: an integer representing the ID of the tenant
# Returns: the sql command in string form for matching city and rent range 
def get_sql_query(id):
    sql_query_p1 = """
    SELECT appid
    FROM homeownerapp
    WHERE rent_range_start <= (
        SELECT rent_range_end
        FROM tenantapp
        WHERE appid="""
    sql_query_p2 = """
    )AND rent_range_end>(
        SELECT rent_range_start
        FROM tenantapp
        WHERE appid="""
    sql_query_p3 = """
    )AND city=(
        SELECT city
        FROM tenantapp
        WHERE appid="""
    sql_query_p4 = """
    )"""
    return sql_query_p1 + str(id) + sql_query_p2 + str(id) + sql_query_p3 + str(id) + sql_query_p4

# Input: no input
# Returns: string for sql command used to get column names
def get_sql_col_names():
    return """
    SELECT *
    FROM homeownerapp
    """

def print_list_index(list, x):
    print(list[x], '\n')

def print_list_all(lists):
    print("Entire list: ")
    print(*lists, sep = '\n\n')
    print("\n\n")
#~~~~~~~~~ Matching METHODS ~~~~~~~~~#

#~~~~~~~~~~ Most important Questions ~~~~~~~~~~#

# 6. What are your typical workday hours and days of the week? Please fill out in the boxes below as such (for example: 9-5, 9am-5pm)
# Input: Range of numbers(hours) and string days

def match_workSchedule(ex_Ten: Tenant, ex_HO: HomeOwner):
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
                ex_HO.appid, '\n')

        # Add to matched DB
        #global matchedDB 
        #matchedDB = matchedDB + ex_HO
    else:
        print("City NOT MATCHED for Tenant ID #: ",
                ex_Ten.appid, " and HomeOwner ID #: ", 
                ex_HO.appid, '\n')

# 10. What is the monthly rent range you are looking to pay? HANDLED WITH SQL
# Input: Range of Numbers 

# ~~~~~~~~~~~ match rent function ~~~~~~~~~~~ #
# Checks for intersection between HO_rentDB_Set and TEN_rentDB_Set
# If it found an intersection - add to matched
# else do nothing -> print not match for testing
def match_rent(ex_Ten: Tenant, ex_HO: HomeOwner):
    # Testing Print Statement
    print("Match Rent: ")

    #get ranges
    TenRange = range(ex_Ten.rent_range_start, ex_Ten.rent_range_end)
    HORange = range(ex_HO.rent_range_start, ex_HO.rent_range_end)

    #put range variables in sets check for intersection
    TenRange_set = set(TenRange)
    HORange_set = set(HORange)
    #if match is found
    if TenRange_set.intersection(HORange_set):
        #Print if found (testing)
        print("RENT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

        # add to matchedDB
#        global matchedDB, HO_rentDB 
#        matchedDB = matchedDB + HO_rentDB

        # print updated matchedDB (testing)
#        print(matchedDB)

    #if match is not found     
    else:
        # Print if not found (Testing)
        print("RENT NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

#     print(matchedDB)
# end match_rent()

# 14. Are you open to living with someone who may have children?
# Input: Bool (Yes/No)

def match_livingWithKids(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match open to living with kids: ")

    if ex_Ten.live_with_children == ex_HO.live_with_children:
        print("Open to living with kids MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    else:
        print("Open to living with kids NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

#end match_livingWithKids()

# 13. Do you have any children? 
# Input: Bool (Yes/No), if yes number input age numbers
def match_HaveKids(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match Have Kids: ")

    if ex_Ten.has_children == ex_HO.has_children:
        print("Has kids MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid)
        if(ex_Ten.has_children == True):
            print("Tenant #", ex_Ten.appid, "Childeren ages: ", ex_Ten.children_ages)
        if(ex_HO.has_children == True):
            print("HomeOwner # ", ex_HO.appid, "Childeren ages: ", ex_HO.children_ages)
        print('\n')
    else: 
        print("Has kids NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid)
        if(ex_Ten.has_children == True):
            print("Tenant #", ex_Ten.appid, "Childeren ages: ", ex_Ten.children_ages)
        if(ex_HO.has_children == True):
            print("HomeOwner # ", ex_HO.appid, "Childeren ages: ", ex_HO.children_ages)
        print('\n')

#end match_HaveKids()

# 16. Are you open to living with someone who has pets? 
# Input: Bool

def match_livingWithPets(ex_Ten: Tenant, ex_HO: HomeOwner):
    # Testing function print
    print("Match living with pets: ")

    #if they are equal, they match
    if ex_Ten.personal_pets_bool == ex_HO.personal_pets_bool:
        print("Living with pets MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    #add to matched array

    else: 
        print("Living with pets NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

#end match_livingWithPets()

# 15. Do you have any pets?
# Input: Bool (Yes/No) if yes number input of # of pets and string of types
def match_HavePets(ex_Ten: Tenant, ex_HO: HomeOwner):
    # Testing Function print   
    print("Match have pets: ")

    if ex_Ten.personal_pets_bool == ex_HO.personal_pets_bool:
        print("Have pets MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid)
        if(ex_Ten.personal_pets_text == True):
            print("Tenant #", ex_Ten.appid, "Pet type: ", ex_Ten.children_ages)
        if(ex_HO.personal_pets_text == True):
            print("HomeOwner # ", ex_HO.appid, "Pet type: ", ex_HO.children_ages, '\n')
        print('\n')
    #add to matched array

    else: 
        print("Have pets NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid)
        if(ex_Ten.personal_pets_bool == True):
            print("Tenant #", ex_Ten.appid, "Pet type: ", ex_Ten.personal_pets_text)
        if(ex_HO.personal_pets_bool == True):
            print("HomeOwner # ", ex_HO.appid, "Pet type: ", ex_HO.personal_pets_text , '\n')
        print('\n')

#end match_HavePets()

# 17. When would you like to move in?
# Input: string(month) and number(year) -> Jan 2023
# Notes: we might be able to use a python library to return number values or something
def match_MoveDate(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match move date UNFINISHED LOGIC: ")

    if ex_Ten.move_in_date == ex_HO.move_in_date:
        print("Move date MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, "for move in date: ", ex_Ten.move_in_date, '\n')
    
    else:
        print("Move date NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

#end match_MoveDate()

# 12. Would you like to rent month to month or on a lease basis?
# Input: either month-to-month or Lease basis, if lease basis number input for how long
def match_leaseType(ex_Ten: Tenant, ex_HO: HomeOwner):
    #Initial testing print
    print("Match lease type: ")
    if ex_Ten.lease_or_rent == ex_HO.lease_or_rent:
        print("Lease Type MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid)
        print("Lease Type wanted:" , ex_Ten.lease_or_rent)
        if ex_Ten.lease_or_rent == 'lease':
            print("Lease Length: ", ex_Ten.lease_length, 'Months \n')
        else:
            print()
    else:
        print("Lease type NOT MATCHED", '\n')
#end match_leaseType():


#~~~~~~~~~~ Medium Importance Questions ~~~~~~~~~~#

# 8. Is there a preferred neighborhood you would like to rent within your specified area?
# Input: String
def match_neighborhoodPref(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match neighborhood preference: ")
    if ex_Ten.preferred_neighborhood == ex_HO.preferred_neighborhood:
        print("neighborhood MATCHED with Tenant ID #: ",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, '\n')
    else:
        print("neighborhood NOT MATCHED",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, '\n')
#end match_neighborhoodPref()

# 9. What is the maximum number of housemates you are willing to live with?
# Input: 1, 2, 3, 4, 5, 5+
def match_MaxRoomates(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Matching max roomates: ")
    if (ex_Ten.max_house_mates <= ex_HO.max_house_mates):
        print("max roommates MATCHED",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, '\n')
    else:
        print("max roommates NOT MATCHED",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, '\n')
#end match_MaxRoomates():

# 11. Please give us a range for the age of the women you would like to co-live with or type “does not matter”
# Input: Range of numbers(might be check box), or string "does not matter"
# Current Ranges: 18-20, 21-30, 31-40, 41-50, 50+
def match_AgeRange(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match age range: ")

    if ex_Ten.age_range == ex_HO.age_range:
        print("Age Range type MATCHED with Tenant ID #: ",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, "for age range: ", ex_Ten.age_range, '\n')

    else:
        print("Age Range type NOT MATCHED with Tenant ID #: ",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, ", Tenant preferred age range: ",
         ex_Ten.age_range, " and Home Owner preferred age range: ",
         ex_HO.age_range, '\n')

#end match ageRange()

# 19. What environment would be ideal for you?
# Input: string: peace and quiet, or someone I can talk to and hang out with, or other
# Note: Natural Language toolkit for other?
def match_SocialEnvironment(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match social enviroment: ")

    if ex_Ten.environment_type == ex_HO.environment_type:
        print("Environment type MATCHED with Tenant ID #: ",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, '\n')
    else:
        print("Environment type NOT MATCHED with Tenant ID #: ",
        ex_Ten.appid, "and HomeOwner ID #: ",
        ex_HO.appid, '\n')
#end match_SocialEnvironment()

# 20. On a scale of 1-5 how would you rate the importance of the following?
    # Furnished room
    # Parking
    # Gym
# Input: Range of numbers 1 to 5
# Note: subtract tenant number from home owner number and smaller number better match 
# 0 = 100% 
# 1 = 80%
# 2 = 60% ...
def match_amenitiesImportance(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("match amenities importance: ")

    # Furnished room
    if ex_Ten.q20_1 == ex_HO.q20_1:
        print("Rating Amenenities Q20_1 (Furnished room) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Amenenities Q20_1 (Furnished room) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    # Parking
    if ex_Ten.q20_2 == ex_HO.q20_2:
        print("Rating Amenenities Q20_2 (Parking) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Amenenities Q20_2 (Parking) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    # Furnished room
    if ex_Ten.q20_3 == ex_HO.q20_3:
        print("Rating Amenenities Q20_3 (Furnished room) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Amenenities Q20_3 (Furnished room) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

#end match_amenitiesImporance()

# 24. On a scale of 1-5 how would you rate YOURSELF for each of the following:
    #Kitchen use
    #Neatness
    #Kitchen cleanliness
    #Guests often visit
    #Household Cleanliness
    #Recreational Cannabis
    #Smoking <- ASK ABOUT SEPERATE QUESTION
# Input: Range of numbers 1 to 5
# Note: subtract tenant number from home owner number, add all together and divide by 6 and smaller number better match 
# 0 = 100% 
# 1 = 80%
# 2 = 60% ...
def match_rateYourself(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match Rate Yourself: ")

    # Kitchen Use
    if ex_Ten.q24_1 == ex_HO.q24_1:
        print("Rating Yourself Q24_1 (Kitchen Use) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Yourself Q24_1 (Kitchen Use) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    #Neatness
    if ex_Ten.q24_2 == ex_HO.q24_2:
        print("Rating Yourself Q24_2 (Neatness) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Yourself Q24_2 (Neatness) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    #Kitchen cleanliness
    if ex_Ten.q24_3 == ex_HO.q24_3:
        print("Rating Yourself Q24_3 (Kitchen cleanliness) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Yourself Q24_3 (Kitchen cleanliness) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    #Guests often visit
    if ex_Ten.q24_4 == ex_HO.q24_4:
        print("Rating Yourself Q24_4 (Guests often visit) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Yourself Q24_4 (Guests often visit) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    #Household Cleanliness
    if ex_Ten.q24_5 == ex_HO.q24_5:
        print("Rating Yourself Q24_5 (Household Cleanliness) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Yourself Q24_5 (Household Cleanliness) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    #Recreational Cannabis
    if ex_Ten.q24_6 == ex_HO.q24_6:
        print("Rating Yourself Q24_6 (Recreational Cannabis) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Yourself Q24_6 (Recreational Cannabis) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    #Smoking
    if ex_Ten.q24_7 == ex_HO.q24_7:
        print("Rating Yourself Q24_7 (Smoking) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Yourself Q24_7 (Smoking) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    print(ex_Ten.q24_1)
    #calculate differences
    tempSum = abs((ex_Ten.q24_1) - ex_HO.q24_1) + abs((ex_Ten.q24_2 - ex_HO.q24_2)) 
    + abs((ex_Ten.q24_3 - ex_HO.q24_3)) + abs((ex_Ten.q24_4 - ex_HO.q24_4)) + abs((ex_Ten.q24_5 - ex_HO.q24_5))
    + abs((ex_Ten.q24_6 - ex_HO.q24_6)) + abs((ex_Ten.q24_7 - ex_HO.q24_7))
    print ('tempSum:', tempSum, '\n')
#end match_rateYourself():

# 26. On a scale of 1-5 how would you like your HOUSEMATE to rate for each of the following:
#    Kitchen use
#    Neatness
#    Kitchen cleanliness
#    Guests oftenmatch_hobbies(ex_Ten, ex_HO)

# Input: Range of numbers 1 to 5
# Note: subtract tenant number from home owner number, add all together and divide by 6 and smaller number better match 
# 0 = 100% 
# 1 = 80%
# 2 = 60% ...
def match_RateOthers(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match Rate others: ")

    #Kitchen use
    if ex_Ten.q26_1 == ex_HO.q26_1:
        print("Rating Others Q26_1 (Kitchen Use) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Others Q26_1 (Kitchen Use) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    #Neatness
    if ex_Ten.q26_2 == ex_HO.q26_2:
        print("Rating Others Q26_2 (Neatness) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Others Q26_2 (Neatness) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    #Kitchen cleanliness
    if ex_Ten.q26_3 == ex_HO.q26_3:
        print("Rating Others Q26_3 (Kitchen cleanliness) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Others Q26_3 (Kitchen cleanliness) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    #Guests often visit
    if ex_Ten.q26_4 == ex_HO.q26_4:
        print("Rating Others Q26_4 (Guests often visit) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Others Q26_4 (Guests often visit) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    #Household Cleanliness
    if ex_Ten.q26_5 == ex_HO.q26_5:
        print("Rating Others Q26_5 (Household Cleanliness) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Others Q26_5 (Household Cleanliness) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    #Recreational Cannabis
    if ex_Ten.q26_6 == ex_HO.q26_6:
        print("Rating Others Q26_6 (Recreational Cannabis) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Others Q26_6 (Recreational Cannabis) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    #Smoking
    if ex_Ten.q26_7 == ex_HO.q26_7:
        print("Rating Others Q26_7 (Smoking) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else: 
        print("Rating Others Q26_7 (Smoking) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    

    #calculate differences
    tempSum = abs((ex_Ten.q26_1 - ex_HO.q26_1)) + abs((ex_Ten.q26_2 - ex_HO.q26_2)) 
    + abs((ex_Ten.q26_3 - ex_HO.q26_3)) + abs((ex_Ten.q26_4 - ex_HO.q26_4)) + abs((ex_Ten.q26_5 - ex_HO.q26_5))
    + abs((ex_Ten.q26_6 - ex_HO.q26_6)) + abs((ex_Ten.q26_7 - ex_HO.q26_7))
    print ('tempSum:', tempSum, '\n')
    
#end match_rateOthers()

# 28. What else would you like us to know about you or about your future housemate(s)?
# Input: String
# Note: Natural Language Toolkit?
def match_TellUs(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match Tell us: UNFINISHED LOGIC")

    print("Tenant tell us about yourself Tenant # ", ex_Ten.appid,": ", ex_Ten.additional_info)
    print("Home Owner tell us about yourself Home Owner # ", ex_HO.appid,": ", ex_HO.additional_info, '\n')
#end match_TellUs()


#~~~~~~~~~~ Low Importance Questions ~~~~~~~~~~#
# 18. Which term best describes your personality? Check all that apply.
    #Carefree
    #Outgoing
    #Laid back
    #Other (please specify)
# Input: check box or string other
def match_personality(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match Personality: ")
    
    # Carefree
    if ex_Ten.q18_1 == ex_HO.q18_1:
        print("Personality Q18_1 (Carefree) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
        
        #add logic to adjust the weight according to 
    else:
        print("Personality Q18_1 (Carefree) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    # Outgoing
    if ex_Ten.q18_2 == ex_HO.q18_2:
        print("Personality Q18_2 (Outgoing) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else:
        print("Personality Q18_2 (Outgoing) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    # Laid Back
    if ex_Ten.q18_3 == ex_HO.q18_3:
        print("Personality Q18_3 (Laid Back) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    else:
        print("Personality Q18_3 (Laid Back) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    # Other
    if ex_Ten.q18_4 == ex_HO.q18_4:
        #print("Personality Q18_4 (Other) MATCHED with Tenant ID #: ", 
        #ex_Ten.appid, "and HomeOwner ID #: ", 
        #ex_HO.appid)
        print("Personality Q18_4 (Other) -> Will add later using Natural Language Toolkit", '\n')
    else:
        #print("Personality Q18_3 (Laid Back) NOT MATCHED with Tenant ID #: ", 
        #ex_Ten.appid, "and HomeOwner ID #: ", 
        #ex_HO.appid)
        print("Personality Q18_4 (Other) -> Will add later using Natural Language Toolkit", '\n')

#end match_personality()

# 21. What does your ideal Friday night look like? Please check all boxes that apply.
#    Movie night with friends/housemates
#    Night out
#    Bar hopping
#    Self-care night to wind down
#    Netflix
#    Other (please specify)
# Input: Checkbox, string other
# Note: can make 0 or 1 values for checked\not checked and test equality
def match_FridayNight(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("Match Friday Night Preference: UNFINISHED LOGIC")

    if ex_Ten.q21_1 == ex_HO.q21_1:
        #match is good
        print("Friday Night Q21_1(Movie night with friends/housemates) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    else:
        print("Friday Night Q21_1(Movie night with friends/housemates) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    if ex_Ten.q21_2 == ex_HO.q21_2:
        #match is good
        print("Friday Night Q21_2(Night out) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    else:
        print("Friday Night Q21_2(Night out) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    if ex_Ten.q21_3 == ex_HO.q21_3:
        #match is good
        print("Friday Night Q21_3(Bar hopping) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    else:
        print("Friday Night Q21_3(Bar hopping) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    if ex_Ten.q21_4 == ex_HO.q21_4:
        #match is good
        print("Friday Night Q21_4(Self-care night to wind down) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    else:
        print("Friday Night Q21_4(Self-care night to wind down) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    if ex_Ten.q21_5 == ex_HO.q21_5:
        #match is good
        print("Friday Night Q21_5(Netflix) MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    else:
        print("Friday Night Q21_5(Netflix) NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
#end match_FridayNight()

# 27. Please let us know your favorite hobbies, and what you do on your days off for enjoyment.
# Input: String
# Note: Natural Language Toolkit, not sure how to approach this one
# Note2: We might be able to add the strings to a set and check for intersection,
#        i.e. 'I watch TV' vs 'watching TV' will find 'TV' intersection
def match_hobbies(ex_Ten: Tenant, ex_HO: HomeOwner):
    print("match hobbies")

    if ex_Ten.hobbies_text == ex_HO.hobbies_text:
        print("Hobbies MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')
    
    else:
        print("Hobbies NOT MATCHED with Tenant ID #: ", 
        ex_Ten.appid, "and HomeOwner ID #: ", 
        ex_HO.appid, '\n')

    
#end match_hobbies()

#~~~~~~~~~ END Matching METHODS ~~~~~~~~~#


def print_matchedDB():
    print('\n\n', matchedDB)







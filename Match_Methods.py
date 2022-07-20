# File to hold our methods



#Test function to ensure the file working
def testFunction():
    print("Printing Test function")


#~~~~~~~~~ Matching METHODS ~~~~~~~~~#

#~~~~~~~~~~ Most important Questions ~~~~~~~~~~#

# 6. What are your typical workday hours and days of the week? Please fill out in the boxes below as such (for example: 9-5, 9am-5pm)
# Input: Range of numbers
def match_workSchedule():
    print("Match Work Schedule")

#end match_workSchedule():

# 7. In which city are you looking to rent?
# Input: string
# In Main.py: Create DB for Cities and add them to sets for (testing change with multi-dimensional array)

def match_city(HO_city, TEN_city):
    # for cityDB in cityDB:
    # if tempCityDB == 'Glendale':
    # print('MATCH')

    #make arrays sets for .intersection()
    HO_city_set = set(HO_city)
    TEN_city_set = set(TEN_city)

    #Test import
    #print("HO_city_set: ", HO_city_set)
    #print("TEN_city_set: ", TEN_city_set)

    if set(HO_city_set).intersection(TEN_city_set):
        print("CITY MATCH")

        # add to matchedDB
       # global matchedDB, HO_rentDB 
       # matchedDB = matchedDB + HO_rentDB

        #print updated matchedDB (testing)
        #print(matchedDB)
    #Else do nothing    
    else:
        print("NO City Match")

#end match_city()

# 10. What is the monthly rent range you are looking to pay? 
# Input: Range of Numbers 

def match_rent(HO_rent, Ten_Rent):
    # Testing Print Statement
    #print("match_rent function()")
    HO_rent_set = set(HO_rent)
    TEN_rent_set = set(Ten_Rent)
    
    #Test sets
    #print("HO_rent_set: ", HO_rent_set)
    #print("TEN_rent_set: ", TEN_rent_set)

    #if match is found
    if HO_rent_set.intersection(TEN_rent_set):
        #Print if found (testing)
        print("RENT MATCHED")

        # add to matchedDB
       # global matchedDB, HO_rentDB 
       # matchedDB = matchedDB + HO_rentDB

        #print updated matchedDB (testing)
        #print(matchedDB)

    #if match is not found     
    else:
        # Print if not found (Testing)
        print("RENT NOT MATCHED")

    # print(rentDB)
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
def match_livingWithPets():
    print("living with pets")
#end match_livingWithPets()

# 15. Do you have any pets?
# Input: Bool (Yes/No) if yes number input of # of pets and string of types
def match_HavePets():
    print("match have pets")
#end match_HavePets()

# 17. When would you like to move in?
# Input: string(month) and number(year) -> Jan 2023
# Notes: we might be able to use a python library to return number values or something
def match_MoveDate():
    print("Match move date")
#end match_MoveDate()

# 12. Would you like to rent month to month or on a lease basis?
# Input: either month-to-month or Lease basis, if lease basis number input for how long
def match_leaseType():
    print("Match lease type")
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
def match_FridayNight():
    print("match friday night")
#end match_FridayNight()

# 27. Please let us know your favorite hobbies, and what you do on your days off for enjoyment.
# Input: String
# Note: Natural Language Toolkit, not sure how to approach this one
def match_hobbies():
    print("match hobbies")
#end match_hobbies()

#~~~~~~~~~ END Matching METHODS ~~~~~~~~~#








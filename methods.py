# File to hold our methods to be called in main

# Install for geopy -> pip install geopy
# Install for pandas -> pip install pandas

# Library imports
# from asyncio.windows_events import NULL
# from asyncio.windows_events import NULL
from multiprocessing.dummy import Array
from Employer import Employer
from Worker import Worker
import psycopg2
import pandas
from geopy import *
from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD
from geopy import distance
import requests
import folium
import polyline
import numpy as np

# Uses https://nominatim.openstreetmap.org/ui/search.html
geolocater = Nominatim(user_agent="http")
global output
output = []

# connect to database method (From previous project)
# def connect_to_db():
#     # Database host is database address
#     # Database name is name of database
#     db_host = "ec2-54-165-90-230.compute-1.amazonaws.com"
#     db_name = "d6hp3i25m6gslc"

#     # Data base username/pass
#     db_user = "uqqcowyaruajrk"
#     db_pass = "e8828f90c6df41a82eac46bcb552a9cdf32a5b109db1d72ec7cb9ad988030475"
#     db_port = 5432

#     connect = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_pass, port=db_port)
#     return connect

# ==============================================================================================

# filter job type i.e. Gardening, etc method
# sets job skills as a set and checks for intersection
# returns -> none
def filter_jobType(ex_Worker: Worker, ex_Employer: Employer):
    # print("Filter_jobType() function for Worker " + ex_Worker.worker_name +
    #             " and Employer " + ex_Employer.employer_name + ":\n")

    jobs_Worker_set = set(ex_Worker.job_skills)
    jobs_Employer_set = set(ex_Employer.job_skills)

    if jobs_Worker_set.intersection(jobs_Employer_set):
        print("SETS MATCHED for: " + ex_Employer.employer_name +
              " and " + ex_Worker.worker_name)
        print("For jobs: " + str(jobs_Employer_set.intersection(jobs_Worker_set)))
        print()

    else:  # ex_Worker.job_skills != ex_Employer.job_skills:
        print("Jobs NOT Matched for: " + ex_Worker.worker_name +
              " and " + ex_Employer.employer_name + "\n")
        print("Available jobs for Worker " + ex_Worker.worker_name +
              ": " + str(ex_Worker.job_skills) + "\n")
        print("Available jobs for Employer " + ex_Employer.employer_name + ": "
              + str(ex_Employer.job_skills) + "\n")

# ==============================================================================================
# Methods for calc_distance
# getMetersToMiles() used for get_Route
# returns miles or kilometers

def getMetersToMiles(meters):
    return meters*0.000621371192

def getMetersToKilometers(meters):
    return meters/1000

# ==============================================================================================
# get_route calculates the distance from one point to another

def test_route(address):
    loc = geolocater.geocode(address)
    return loc

# sets address to geocode values, calculates driving distance using longitude and latidude
# returns distance in miles to worker address and employer address
def get_route(ex_Worker: Worker, ex_Employer: Employer):
    # print("get_route() function: for Worker " + ex_Worker.worker_name +
    #             " and Employer " + ex_Employer.employer_name + ":\n")

    # Set Worker/Employer Addresses to extract latidude/longitude
    worker_Location = geolocater.geocode(ex_Worker.address)
    employer_Location = geolocater.geocode(ex_Employer.address)

    # Address testing
    # print("Worker Address: ")
    # print(worker_Location )
    # print("\nEmployer Address: " )
    # print(employer_Location)

    # Worker Longitude and latidute -> pickup/starting
    pickup_long = worker_Location.longitude
    pickup_lat = worker_Location.latitude

    # Employer Longitude and latitude
    dropoff_lon = employer_Location.longitude
    dropoff_lat = employer_Location.latitude

    # sets location in proper format and calls OSRM
    loc = "{},{};{},{}".format(
        pickup_long, pickup_lat, dropoff_lon, dropoff_lat)
    url = "https://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc)
    if r.status_code != 200:
        return {}

    # calculates the route based on OSRM 
    # sets start_point, end_point and distance and sets it to out
    res = r.json()
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location']
                   [1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location']
                 [1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']

    # can be used to output the route, starting/ending point and distance (meters)
    out = {'route': routes,
           'start_point': start_point,
           'end_point': end_point,
           'distance': distance
           }

    # set distance(meters) to miles and kilometers
    distance_Miles = getMetersToMiles(distance)
    distance_Kilometers = getMetersToKilometers(distance)

    # print output -> remove for final product?
    print("Distance in miles: " +
          str("{:.2f}".format(distance_Miles)) + " Miles")
    print("Distance in kilometers: " +
          str("{:.2f}".format(distance_Kilometers)) + " Kilometers")

    # return
    return distance_Miles

# ==============================================================================================
# original distance calculations 
# -> only returns straight line distance not driving distance
# used for testing address validity 
# returns -> none
def calc_distance(ex_Worker: Worker, ex_Employer: Employer):
    print("calc_distance() function for Worker " + ex_Worker.worker_name +
          " and Employer " + ex_Employer.employer_name + ":\n")

    # Testing
    # print("Worker Address test:")
    # print(ex_Worker.address)

    # print("\nEmployer Address Test: ")
    # print(ex_Employer.address)

    # set address to temp location variables
    worker_Location = geolocater.geocode(ex_Worker.address)
    employer_Location = geolocater.geocode(ex_Employer.address)

    # Used for testing
    # print("Worker Address: ")
    # print(worker_Location )
    # print("\nEmployer Address: " )
    # print(employer_Location)

    # Distance is less than 20 miles check
    # Check if greater than 20 miles
    if GD((worker_Location.latitude, worker_Location.longitude),
          (employer_Location.latitude, employer_Location.longitude)).miles >= 20:
        print("\nDistance in miles is greater than 20\n")

    # else return the distance
    else:
        print("\nDistance in miles: " + str("{:.2f}".format(GD((worker_Location.latitude, worker_Location.longitude),
                                                               (employer_Location.latitude, employer_Location.longitude)).miles)) + " miles\n")
        print("Distance in Kilometers: " + str("{:.2f}".format(GD((worker_Location.latitude, worker_Location.longitude),
                                                                  (employer_Location.latitude, employer_Location.longitude)).kilometers)) + " KM\n")

# ==============================================================================================

# checks for the matched days by adding them to a list of matched_days
# returns matched_days for out_filter()
def filter_days(ex_Worker: Worker, ex_Employer: Employer):
    # print("calc_days() function for Worker " + ex_Worker.worker_name +
    #             " and Employer " + ex_Employer.employer_name + ":\n")
    matched_days = []
    # Check each day set to 1 if matched, 0 if not matched
    # Sunday check
    if ex_Worker.sunday == ex_Employer.sunday:
        # print("Sunday Matched")
        matched_days.append("Sunday")

    # Monday Check
    if ex_Worker.monday == ex_Employer.monday:
        # print("Monday Matched")
        matched_days.append("Monday")

    # Tuesday Check
    if ex_Worker.tuesday == ex_Employer.tuesday:
        # print("Tuesday Matched")
        matched_days.append("Tuesday")

    # Wednesday Check
    if ex_Worker.wednesday == ex_Employer.wednesday:
        # print("Wednesday Matched")
        matched_days.append("Wednesday")

    # Thursday check
    if ex_Worker.thursday == ex_Employer.thursday:
        # print("Thursday Matched")
        matched_days.append("Thursday")

    # Friday check
    if ex_Worker.friday == ex_Employer.friday:
        # print("Friday Matched")
        matched_days.append("Friday")

    # Saturday Check
    if ex_Worker.saturday == ex_Employer.saturday:
        # print("Saturday Matched")
        matched_days.append("Saturday")

    print()
    return matched_days

# ==============================================================================================
# time filtering
# prints intersection
# returns -> none
def filter_time(ex_Worker: Worker, ex_Employer: Employer):
    # print("filter_time() function for Worker " + ex_Worker.worker_name +
    #             " and Employer " + ex_Employer.employer_name + ":\n")

    # set time range to variable -> worker
    worker_range = range(ex_Worker.start_time, ex_Worker.end_time+1)
    employer_range = range(ex_Employer.start_time, ex_Employer.end_time+1)

    # testing
    # for i in worker_range:
    #     print(i)
    # for i in employer_range:
    #     print(i)

    # convert worker_range to set
    worker_rangeSet = set(worker_range)
    intersect = worker_rangeSet.intersection(employer_range)

    if len(intersect) == 0:
        print("Time does not intersect")
    else:
        print(intersect)

    print()


# ==============================================================================================
# Filters gender by checking first if they are matched
# then returns if they are female matched or male matched
def filter_gender(ex_Worker: Worker, ex_Employer: Employer):
    # print("filter_gender() function for Worker ")

    # 0 = female
    # 1 = male

    if ex_Worker.gender == ex_Employer.gender:
        if ex_Worker.gender == 0:
            print("Gender is matched for female")
        else:
            print("Gender is matched for males")

    else:
        print("Gender is not matched")

    print()


# ==============================================================================================
# Check doesn't filter out the objects list 
# returns information based on the filter methods called 
def checker(ex_Worker: Worker, ex_Employer: Employer):
    print("checker() function:\n")
    print("Begin filter for " + ex_Worker.worker_name +
          " and " + ex_Employer.employer_name + ":\n")

    # gender check
    filter_gender(ex_Worker, ex_Employer)
    # job check
    filter_jobType(ex_Worker, ex_Employer)
    # filter days
    filter_days(ex_Worker, ex_Employer)
    # filter time
    filter_time(ex_Worker, ex_Employer)
    # filter distance
    get_route(ex_Worker, ex_Employer)

    # end checker
    print("End of check")

# ==============================================================================================
# checks if genders are matched for what the employer wants
# returns true or false based on 
def checkGender(ex_Worker: Worker, ex_Employer: Employer):
    # Gender check
    if ex_Worker.gender == ex_Worker.gender:
        print("Gender Matched\n")
        return True
    else:
        print("FAILED GENDER CHECK\n")
        return False

# ==============================================================================================
# checks that skills are matched and prints the matched skills
# returns true or false based on interesetion
def checkSkills(ex_Worker: Worker, ex_Employer: Employer):
    # skills check
    jobs_Worker_set = set(ex_Worker.job_skills)
    jobs_Employer_set = set(ex_Employer.job_skills)

    if jobs_Worker_set.intersection(jobs_Employer_set):
        print("For jobs: " + str(jobs_Employer_set.intersection(jobs_Worker_set)))
        return True
    else:
        print("FAILED JOB SKILLS CHECK")
        return False

# ==============================================================================================
# checks that days are matched 
# returns true or false based on days_list
def checkDays(ex_Worker: Worker, ex_Employer: Employer):
    # days check -> figure out days
    days_list = filter_days(ex_Worker, ex_Employer)

    if (len(days_list)) == 0:
        print("Days were NOT matched")
        return False
    else:
        print("Days Matched: ")
        print(days_list)
        print()
        return True

# ==============================================================================================
# checks time based on start and end times using intersections 
# returns intersection list based on matched times
def checkTime(ex_Worker: Worker, ex_Employer: Employer):
    # time filter
    worker_range = range(ex_Worker.start_time, ex_Worker.end_time+1)
    employer_range = range(ex_Employer.start_time, ex_Employer.end_time+1)

    # testing
    # for i in worker_range:
    #     print(i)
    # for i in employer_range:
    #     print(i)

    # convert worker_range to set
    worker_rangeSet = set(worker_range)
    intersect = worker_rangeSet.intersection(employer_range)

    # time does not intersect
    if len(intersect) == 0:
        print("FAILED TIME CHECK\n")
        return False
    else:
        print("Passed time check for times: ")
        print(intersect)
        print()
        return True

# ==============================================================================================
# Checks time array for availability using numpy
# returns -> true or false
def checkTimeArray(ex_Worker: Worker, ex_Employer: Employer):
    
    # get time availability for both in the form of 24 boolean numpy array
    work_array = np.array(ex_Worker.time_array)
    employ_array = np.array(ex_Employer.time_array)

    # subtract the employer array from the worker array to see if there are any negative numbers
    result_array = np.subtract(work_array, employ_array)

    # if there are any negative numbers, return false, otherwise return True
    if (-1 in result_array.tolist()):
        return False
    return True

# ==============================================================================================
# checkDistance -> not used in out_filter 
# returns miles 
def checkDistance(ex_Worker: Worker, ex_Employer: Employer):
    # Distance check
    print("Distance Check: ")
    temp_miles = get_route(ex_Worker, ex_Employer)
    if temp_miles >= 30:
        print("DRIVING DISTANCE FURTHER THAN 30 MILES\n")
    else:
        print()
    return temp_miles

# ==============================================================================================
# prints the list of matched workers per employer
# return -> none
def printMatchedWorkers(ex_Employer: Employer):
    for x in ex_Employer.matched_workers:
        print(x[0].worker_name)

# ==============================================================================================
# Filters out the list of workers and employers and returns the matched list
# return -> list of matched objects
def out_list(ex_Worker: Worker, ex_Employer: Employer):
    # filters based on order of importance and leaves nested if's when false
    if (checkGender(ex_Worker, ex_Employer)):
        if (checkSkills(ex_Worker, ex_Employer)):
            if (checkDays(ex_Worker, ex_Employer)):
                if (checkTimeArray(ex_Worker, ex_Employer)):
                #if (checkTime(ex_Worker, ex_Employer)):
                    print("End of list filtering: \n" +
                        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    miles = checkDistance(ex_Worker, ex_Employer)
                    if (miles <= 30):
                        ex_Employer.matched_workers.append((ex_Worker, miles))
                        ex_Worker.matched_employers.append((ex_Employer, miles))
                        print("Added Worker: " + ex_Worker.worker_name + " to list\n")
                        print("Updated list: ")
                        printMatchedWorkers(ex_Employer)
                    else:
                        print("Worker " + ex_Worker.worker_name +
                            " NOT added for Employer " + ex_Employer.employer_name)
                        if (len(ex_Employer.matched_workers) > 0):
                            print("Current list for employer:")
                            printMatchedWorkers(ex_Employer)
                        else:
                            print(ex_Employer.employer_name + ": employer no matched workers")
                        
    print()

# ==============================================================================================
# Sorts the matched_workers list for each employer 
def sortMatchedWorkers(Employer_List):
    for employer in Employer_List:
        for i in range(len(employer.matched_workers)):
            min_idx = i
            for j in range(i+1, len(employer.matched_workers)):
                if (employer.matched_workers[j][1] < employer.matched_workers[min_idx][1]):
                    min_idx = j
            (employer.matched_workers[i], employer.matched_workers[min_idx]) = (employer.matched_workers[min_idx], employer.matched_workers[i])

# ==============================================================================================
# Sorts the matched_workers list for each employer 
def sortMatchedEmployers(Worker_List):
    for worker in Worker_List:
        for i in range(len(worker.matched_employers)):
            min_idx = i
            for j in range(i+1, len(worker.matched_employers)):
                if (worker.matched_employers[j][1] < worker.matched_employers[min_idx][1]):
                    min_idx = j
            (worker.matched_employers[i], worker.matched_employers[min_idx]) = (worker.matched_employers[min_idx], worker.matched_employers[i])

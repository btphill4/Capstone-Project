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
import time

# Uses https://nominatim.openstreetmap.org/ui/search.html
geolocater = Nominatim(user_agent="http")

# connect to database method 
#   -> From previous project using postgres
#   -> can be used as a reference 
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

    # print output used for testing
    #print("Distance in miles: " +
    #      str("{:.2f}".format(distance_Miles)) + " Miles")
    #print("Distance in kilometers: " +
    #      str("{:.2f}".format(distance_Kilometers)) + " Kilometers")

    # return
    return distance_Miles

# gets route between two addresses
# uses geolocater to assigned the geocode for addresses
# uses OSRM and nomatim.openstreetmap to get distance
def get_route2(address1, address2):
    # print("get_route() function: for Worker " + ex_Worker.worker_name +
    #             " and Employer " + ex_Employer.employer_name + ":\n")

    if (address1 is address2):
        return 0
    # Set Worker/Employer Addresses to extract latidude/longitude
    worker_Location = geolocater.geocode(address1)
    employer_Location = geolocater.geocode(address2)

    # Address testing
    # print("Worker Address: ")
    # print(worker_Location )
    # print("\nEmployer Address: ")
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

    # print output used for testing
    #print("Distance in miles: " +
    #      str("{:.2f}".format(distance_Miles)) + " Miles")
    #print("Distance in kilometers: " +
    #      str("{:.2f}".format(distance_Kilometers)) + " Kilometers")

    # return
    return distance_Miles

# ==============================================================================================
# checks for the matched days by adding them to a list of matched_days
# returns matched_days for match() method
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

    #print()
    return matched_days

# ==============================================================================================
# checks if gender matters to customer and then matches based on their input
# returns true or false based on 
def checkGender(ex_Worker: Worker, ex_Employer: Employer):
    # gender_matters == 1 | doesn't matter == 0

    # Check if gender doesn't matter for both
    if ex_Employer.gender_matters == 0 and ex_Worker.gender_matters == 0:
        # print("Passed gender doesn't matter check")
        return True
    # if gender does matter for both check
    elif ex_Employer.gender_matters == 1 and ex_Worker.gender_matters == 1:
        # check E.preferred == W.gender and W.preferred == E.gender
        if ex_Employer.gender_preferred == ex_Worker.gender and ex_Worker.gender_preferred == ex_Employer.gender:
            return True
        else:
            return False
    # Either both or 1 employer/worker cares
    # Employer cares about gender -> check if E.preferred == W.gender
    elif ex_Employer.gender_matters == 1:
        # employer preferred == worker gender
        if ex_Employer.gender_preferred == ex_Worker.gender:
            return True
        # employer preferred != worker gender
        else:
            return False
    # Worker cares about gender -> check if W.preferred == E.gender
    elif ex_Worker.gender_matters == 1:
        # Worker preferred == employer gender
        if ex_Worker.gender_preferred == ex_Employer.gender:
            return True
        else: 
            return False
    # should never reach here but is a final catch 
    else:
        # print("checkGender failed check input")
        return False

# ==============================================================================================
# checks that skills are matched and prints the matched skills
# returns true or false based on interesetion
def checkSkills(ex_Worker: Worker, ex_Employer: Employer):
    # skills check
    jobs_Worker_set = set(ex_Worker.job_skills)
    jobs_Employer_set = set(ex_Employer.job_skills)

    # verify all these are in jobs_worker_set
    if jobs_Worker_set.intersection(jobs_Employer_set):
        #print("For jobs: " + str(jobs_Employer_set.intersection(jobs_Worker_set)))
        return True
    else:
        #print("FAILED JOB SKILLS CHECK")
        return False

# ==============================================================================================
# checks that days are matched 
# returns true or false based on days_list
def checkDays(ex_Worker: Worker, ex_Employer: Employer):
    # days check -> figure out days
    days_list = filter_days(ex_Worker, ex_Employer)

    if (len(days_list)) == 0:
        #print("Days were NOT matched")
        return False
    else:
        #print("Days Matched: ")
        #print(days_list)
        #print()
        return True

# ==============================================================================================
# REMOVE?
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
        #print("FAILED TIME CHECK\n")
        return False
    else:
        #print("Passed time check for times: ")
        #print(intersect)
        #print()
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
def checkDistance(address1, address2, dist_dict):
    return dist_dict[(address1, address2)]

# ==============================================================================================
# returns true or false based on whether the employer meets the workers minimum salary 
def checkPay(ex_Worker: Worker, ex_Employer: Employer):
    # if the employer rate is equal to or more than ex_Worker rate return true -> good
    if (ex_Employer.payrate >= ex_Worker.min_payrate):
        return True
    # else return false because payrate is below worker rate
    else:
        # print("Payrate too low for " + ex_Worker.worker_name + " and " + ex_Employer.employer_name)    
        return False

# ==============================================================================================
# prints the list of matched workers per employer
# return -> none
def printMatchedWorkers(ex_Employer: Employer):
    for x in ex_Employer.matched_workers:
        print(x[0].worker_name)

# ==============================================================================================
# Filters out the list of workers and employers and returns the matched list
# uses nested if's to find perfect matches. If any return false, it is not a match and exits the nested if's
# return -> None, assigns possible matches to object list variables

# REMOVE?
# def match(ex_Worker: Worker, ex_Employer: Employer, dist_dict):
#     # filters based on order of importance and leaves nested if's when false
#     if (checkGender(ex_Worker, ex_Employer)):
#         if (checkSkills(ex_Worker, ex_Employer)):
#             if (checkDays(ex_Worker, ex_Employer)):
#                 if (checkTimeArray(ex_Worker, ex_Employer)):
#                     miles = checkDistance(ex_Worker.address, ex_Employer.address, dist_dict)
#                     if (miles <= 30):
#                         if ((ex_Employer, miles) not in ex_Worker.matched_employers):
#                             ex_Employer.matched_workers.append((ex_Worker, miles))
#                             ex_Worker.matched_employers.append((ex_Employer, miles))

def match(ex_Worker: Worker, ex_Employer: Employer):
    # filters based on order of importance and leaves nested if's when false
    if (checkGender(ex_Worker, ex_Employer)):
        if (checkSkills(ex_Worker, ex_Employer)):
            if (checkDays(ex_Worker, ex_Employer)):
                 if(checkPay(ex_Worker, ex_Employer)):   # pay check added 
                    if (checkTimeArray(ex_Worker, ex_Employer)):
                        if (ex_Employer not in ex_Worker.matched_employers):
                            ex_Worker.matched_employers.append(ex_Employer)
                            
def addDistanceToMatches(Worker_List, dist_dict):
    for worker in Worker_List:
        new_list = []
        for employer in worker.matched_employers:
            miles = checkDistance(worker.address, employer.address, dist_dict)
            new_list.append((employer, miles))
        worker.matched_employers = new_list;

# REMOVE?
# def match_update(worker, employerList, has_job_list, dist_dict):
#     worker.matched_employers = [];
#     for ex_Employer in employerList:
#         if (ex_Employer not in has_job_list):
#             if (checkGender(worker, ex_Employer)):
#                 if (checkSkills(worker, ex_Employer)):
#                     if (checkDays(worker, ex_Employer)):
#                         if (checkTimeArray(worker, ex_Employer)):
#                             miles = checkDistance(worker.address, ex_Employer.address, dist_dict)
#                             if (miles <= 30):
#                                 worker.matched_employers.append((ex_Employer, miles))
        
    

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

def sortSingleWorker(worker):
    for i in range(len(worker.matched_employers)):
        min_idx = i
        for j in range(i+1, len(worker.matched_employers)):
            if (worker.matched_employers[j][1] < worker.matched_employers[min_idx][1]):
                min_idx = j
        (worker.matched_employers[i], worker.matched_employers[min_idx]) = (worker.matched_employers[min_idx], worker.matched_employers[i])

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

            
def CalcDistanceDict(Employer_List, Worker_List, dist_dict):
    # get distance between each employer/employer combination
    for employer in Employer_List:
        for employer2 in Employer_List:
            if ((employer, employer2) not in dist_dict): # little bit of optimization to lessen API calls
                dist = get_route2(employer.address, employer2.address)
                dist_dict[employer.address, employer2.address] = dist
                dist_dict[employer2.address, employer.address] = dist
                if (dist != 0):
                    time.sleep(1)
                    print("[" + employer.address + ", " + employer2.address + "] = " + str(dist)) 
    
    # get distance between each employer/worker combination
    for worker in Worker_List:
        for employer in Employer_List:
            dist = get_route2(worker.address, employer.address)
            dist_dict[worker.address, employer.address] = dist
            dist_dict[employer.address, worker.address] = dist
            if (dist != 0):
                time.sleep(1)
                print("[" + worker.address + ", " + employer.address + "] = " + str(dist))
                
def CalcDistanceDict2(Employer_List, Worker_List, dist_dict):
    for worker in Worker_List:
        for employer in worker.matched_employers:
            if ((worker.address, employer.address) not in dist_dict):
                dist = get_route2(worker.address, employer.address)
                dist_dict[worker.address, employer.address] = dist;
                dist_dict[employer.address, worker.address] = dist;
                if (dist != 0):
                    time.sleep(1)
                    print("[" + worker.address + ", " + employer.address + "] = " + str(dist)) 
            for employer2 in worker.matched_employers:
                if ((employer.address, employer2.address) not in dist_dict):
                    dist = get_route2(employer.address, employer2.address)
                    dist_dict[employer.address, employer2.address] = dist;
                    dist_dict[employer2.address, employer.address] = dist;
                    if (dist != 0):
                        time.sleep(1)
                        print("[" + employer.address + ", " + employer2.address + "] = " + str(dist)) 
    
#     # get distance between each employer/employer combination
#     for employer in Employer_List:
#         for employer2 in Employer_List:
#             if ((employer, employer2) not in dist_dict): # little bit of optimization to lessen API calls
#                 dist = get_route2(employer.address, employer2.address)
#                 dist_dict[employer.address, employer2.address] = dist
#                 dist_dict[employer2.address, employer.address] = dist
#                 if (dist != 0):
#                     time.sleep(1)
#                     print("[" + employer.address + ", " + employer2.address + "] = " + str(dist)) 
    
#     # get distance between each employer/worker combination
#     for worker in Worker_List:
#         for employer in Employer_List:
#             dist = get_route2(worker.address, employer.address)
#             dist_dict[worker.address, employer.address] = dist
#             dist_dict[employer.address, worker.address] = dist
#             if (dist != 0):
#                 time.sleep(1)
#                 print("[" + worker.address + ", " + employer.address + "] = " + str(dist))
    
# used to calculate distances in multi-job matching
def RecalcDistances(worker, dist_dict):
    for x in range(0, len(worker.matched_employers)):
        current_employer_tuple = worker.matched_employers[x]
        new_employer_tuple = (worker.matched_employers[x][0], checkDistance(worker.address, current_employer_tuple[0].address, dist_dict))
        worker.matched_employers[x] = new_employer_tuple
        sortSingleWorker(worker)
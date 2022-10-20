# File to hold our methods to be called in main

# Install for geopy -> pip install geopy
# Install for pandas -> pip install pandas

# Library imports
# from asyncio.windows_events import NULL
# from asyncio.windows_events import NULL
from Employer import Employer
from Worker import Worker
import psycopg2 
import pandas 
import numpy
from geopy import *
from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD
from geopy import distance
import requests
import folium
import polyline

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
def filter_jobType(ex_Worker: Worker, ex_Employer: Employer):
    print("Filter_jobType() function for Worker " + ex_Worker.worker_name + 
                " and Employer " + ex_Employer.employer_name + ":\n")

    jobs_Worker_set = set(ex_Worker.job_skills)
    jobs_Employer_set = set(ex_Employer.job_skills)

    if jobs_Worker_set.intersection(jobs_Employer_set):
        print("SETS MATCHED for: " + ex_Employer.employer_name + " and " + ex_Worker.worker_name)
        print("For jobs: " + str(jobs_Employer_set.intersection(jobs_Worker_set)))
        print()

    else: #ex_Worker.job_skills != ex_Employer.job_skills:
        print("Jobs NOT Matched for: " + ex_Worker.worker_name + " and " + ex_Employer.employer_name + "\n")
        print("Available jobs for Worker " + ex_Worker.worker_name + ": " + str(ex_Worker.job_skills) + "\n")
        print("Available jobs for Employer " + ex_Employer.employer_name + ": " 
                        + str(ex_Employer.job_skills) + "\n")

# ==============================================================================================


# Methods for calc_distance
# getMetersToMiles() used for get_Route
def getMetersToMiles(meters):
    return meters*0.000621371192

def getMetersToKilometers(meters):
    return meters/1000

# get_route calculates the distance from one point to another
def get_route(ex_Worker: Worker, ex_Employer: Employer):
    print("get_route() function: for Worker " + ex_Worker.worker_name + 
                " and Employer " + ex_Employer.employer_name + ":\n")

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

    loc = "{},{};{},{}".format(pickup_long, pickup_lat, dropoff_lon, dropoff_lat)
    url = "https://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc) 
    if r.status_code!= 200:
        return {}
  
    res = r.json()   
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']
    
    out = {'route':routes,
           'start_point':start_point,
           'end_point':end_point,
           'distance':distance
          }

    # set distance to miles and kilometers
    distance_Miles = getMetersToMiles(distance)
    distance_Kilometers = getMetersToKilometers(distance)

    # print output -> remove for final product?
    print("Distance in miles: " + str("{:.2f}".format(distance_Miles)) + " Miles")
    print("Distance in kilometers: " + str("{:.2f}".format(distance_Kilometers)) + " Kilometers")

    # return everything -> maybe change to just return distance
    # return 
    return distance_Miles

# ==============================================================================================

# method for printing to a map
# def get_map(route):
    
#     m = folium.Map(location=[(route['start_point'][0] + route['end_point'][0])/2, 
#                              (route['start_point'][1] + route['end_point'][1])/2], 
#                    zoom_start=13)

#     folium.PolyLine(
#         route['route'],
#         weight=8,
#         color='blue',
#         opacity=0.6
#     ).add_to(m)

#     folium.Marker(
#         location=route['start_point'],
#         icon=folium.Icon(icon='play', color='green')
#     ).add_to(m)

#     folium.Marker(
#         location=route['end_point'],
#         icon=folium.Icon(icon='stop', color='red')
#     ).add_to(m)

#     return m

# calculate and filter distance method
# Uses https://nominatim.openstreetmap.org/ui/search.html
# limit distance to 20 miles or less -> if more than 20, remove from list
# Run for entire list? or individual?
# For checking next distance, add class value NewDistance and check if newDistance == NULL at start and then run with newDistance
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

def filter_days(ex_Worker: Worker, ex_Employer: Employer):
    print("calc_days() function for Worker " + ex_Worker.worker_name + 
                " and Employer " + ex_Employer.employer_name + ":\n")

    # Check each day set to 1 if matched, 0 if not matched
    # Sunday check
    if ex_Worker.sunday == ex_Employer.sunday:
        print("Sunday Matched")
        ex_Worker.sunday_matched = 1
        ex_Employer.sunday_matched = 1
    else:
        print("Sunday Not Matched")
        ex_Worker.sunday_matched = 0
        ex_Employer.sunday_matched = 0

    # Monday Check
    if ex_Worker.monday == ex_Employer.monday:
        print("Monday Matched")
        ex_Worker.monday_matched = 1
        ex_Employer.monday_matched = 1
    else:
        print("Monday NOT Matched")
        ex_Worker.monday_matched = 0
        ex_Employer.monday_matched = 0

    # Tuesday Check
    if ex_Worker.tuesday == ex_Employer.tuesday:
        print("Tuesday Matched")
        ex_Worker.tuesday_matched = 1
        ex_Employer.tuesday_matched = 1
    else:
        print("Tuesday NOT Matched")
        ex_Worker.tuesday_matched = 0
        ex_Employer.tuesday_matched = 0
    # Wednesday Check
    if ex_Worker.wednesday == ex_Employer.wednesday:
        print("Wednesday Matched")
        ex_Worker.wednesday_matched = 1
        ex_Employer.wednesday_matched = 1
    else:
        print("Wednesday Not Matched")
        ex_Worker.wednesday_matched = 1
        ex_Employer.wednesday_matched = 1

    # Thursday check
    if ex_Worker.thursday == ex_Employer.thursday:
        print("Thursday Matched")
        ex_Worker.thursday_matched = 1
        ex_Employer.thursday_matched = 1
    else:
        print("Thursday Not Matched")
        ex_Worker.thursday_matched = 0
        ex_Employer.thursday_matched = 0

    # Friday check
    if ex_Worker.friday == ex_Employer.friday:
        print("Friday Matched")
        ex_Worker.friday_matched = 1
        ex_Employer.friday_matched = 1
    else:
        print("Friday Not Matched")
        ex_Worker.friday_matched = 0
        ex_Employer.friday_matched = 0

    # Saturday Check
    if ex_Worker.saturday == ex_Employer.saturday:
        print("Saturday Matched")
        ex_Worker.saturday_matched = 1
        ex_Employer.saturday_matched = 1
    else:
        print("Saturday Not Matched")
        ex_Worker.saturday_matched = 0
        ex_Employer.saturday_matched = 0

    print()

# ==============================================================================================
# time filtering
def filter_time(ex_Worker: Worker, ex_Employer: Employer):
    print("filter_time() function for Worker " + ex_Worker.worker_name + 
                " and Employer " + ex_Employer.employer_name + ":\n")

    # set time range to variable -> worker
    worker_range = range(ex_Worker.start_time,ex_Worker.end_time+1)
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
def filter_gender(ex_Worker: Worker, ex_Employer: Employer):
    print("filter_gender() function for Worker ")

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
# output?
def checker(ex_Worker: Worker, ex_Employer: Employer):
    print("checker() function:\n")
    print("Begin filter for " + ex_Worker.worker_name + " and " + ex_Employer.employer_name + ":\n")

    
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

# def print_list(output):
    
def out_list(ex_Worker: Worker, ex_Employer: Employer):
    print("List: ")

    # add worker to list
    output_size = len(output)
    output.append(ex_Worker)

    # Gender check
    if ex_Worker.gender == ex_Worker.gender:
        pass
        # if ex_Worker not in output:
        #     output.append(ex_Worker)
    else:
        if ex_Worker in output:
            output.remove(ex_Worker)
            print("FAILED GENDER CHECK")

        else: 
            pass
        
    
    # skills check
    jobs_Worker_set = set(ex_Worker.job_skills)
    jobs_Employer_set = set(ex_Employer.job_skills)

    if jobs_Worker_set.intersection(jobs_Employer_set):
        # if ex_Worker not in output:
        #     output.append(ex_Worker)
        print("For jobs: " + str(jobs_Employer_set.intersection(jobs_Worker_set)))
    else:
        if ex_Worker in output:
            output.remove(ex_Worker)
            print("FAILED JOB SKILLS CHECK")
        else: 
            pass
    
    # days check -> figure out days
    filter_days(ex_Worker, ex_Employer)
    if ex_Worker.sunday_matched == 1:
        pass
        # output.append(ex_Worker)
    else:
        pass
    if ex_Worker.monday_matched == 1:
        pass
        # output.append(ex_Worker)
    else:
        pass
    if ex_Worker.tuesday_matched == 1:
        pass
        # output.append(ex_Worker)
    else:
        pass
    if ex_Worker.wednesday_matched == 1:
        pass
        # output.append(ex_Worker)
    else:
        pass
    if ex_Worker.thursday_matched == 1:
        pass
        # output.append(ex_Worker)
    else:
        pass
    if ex_Worker.friday_matched == 1:
        pass
        # output.append(ex_Worker)
    else:
        pass
    if ex_Worker.saturday_matched == 1:
        pass
        # output.append(ex_Worker)
    else:
        pass

    # time filter
    worker_range = range(ex_Worker.start_time,ex_Worker.end_time+1)
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
        if ex_Worker in output:
            output.remove(ex_Worker)
            print("FAILED TIME CHECK\n")
        else: 
            pass
    # time does intersect
    else:
        print("Passed time check for times: ")
        print(intersect)  
        print()      
        pass

    temp_miles =get_route(ex_Worker, ex_Employer)
    if temp_miles >= 20:
        print("DRIVING DISTANCE FURTHER THAN 20 MILES\n")
    else: 
        print()
        pass

    print("End of list filtering: \n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )

    if len(output) <= output_size :
        print("Worker " + ex_Worker.worker_name + " NOT added")
        print("Current list")
    else:
        print("Added Worker: " + ex_Worker.worker_name + " to list\n" )
        print("Updated list: ")
        print(*output)
        # for i in len(output):
        #     print(output[i])

    print()
    



# Example from last project
#def match_city(ex_Ten: Tenant, ex_HO: HomeOwner):
#    print("Match city function: ")
#
#    if ex_Ten.city == ex_HO.city:
        #match is good

        #add percent to match percent 
#        ex_HO.matchPercent = ex_HO.matchPercent + 9
        
        #printing test statement
#        print("City MATCHED for Tenant ID #: ",
#                ex_Ten.appid, " and HomeOwner ID #: ", 
#                ex_HO.appid, '\n')

        # Add to matched DB
        #global matchedDB 
        #matchedDB = matchedDB + ex_HO
#    else:
#        print("City NOT MATCHED for Tenant ID #: ",
#                ex_Ten.appid, " and HomeOwner ID #: ", 
#                ex_HO.appid, '\n')
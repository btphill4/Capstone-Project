# File to hold our methods to be called in main

# Install for geopy -> pip install geopy
# Install for pandas -> pip install pandas

# Library imports
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

# filter Day and Time method
def filter_time(ex_Worker: Worker, ex_Employer: Employer):
    print("Filter_time() function for Worker " + ex_Worker.worker_name + 
                " and Employer " + ex_Employer.employer_name + ":\n")

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
    distance_Miles = getMetersToMiles(distance)
    distance_Kilometers = getMetersToKilometers(distance)
    # str("{:.2f}".format(
    print("Distance in miles: " + str("{:.2f}".format(distance_Miles)) + " Miles")
    print("Distance in kilometers: " + str("{:.2f}".format(distance_Kilometers)) + " Kilometers\n")
    return out

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

# output?
def output():
    print("Output() function: STILL IN PROGRESS\n")



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
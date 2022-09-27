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


# filter job type i.e. Gardening, etc method
def filter_jobType(ex_Worker: Worker, ex_Employer: Employer):
    print("filter_jobType() function: \n")

    jobs_Worker_set = set(ex_Worker.job_skills)
    jobs_Employer_set = set(ex_Employer.job_skills)

    if set(jobs_Worker_set).intersection(jobs_Employer_set):
        print("SETS MATCHED for: " + ex_Employer.employer_name + " and " + ex_Worker.worker_name + "\n")

        # print("Job Matched for: " + ex_Worker.worker_name + " and " + ex_Employer.employer_name +
        #         " for job(s): " + ex_Worker.job_skills)

    # if ex_Worker.job_skills == ex_Employer.job_skills:

    #     # job is matched
    #     print("Job Matched for: " + ex_Worker.worker_name + " and " + ex_Employer.employer_name +
    #             " for job(s): " + ex_Worker.job_skills)

    else: #ex_Worker.job_skills != ex_Employer.job_skills:
        print("Jobs NOT Matched for: " + ex_Worker.worker_name + " and " + ex_Employer.employer_name + "\n")



# filter Day and Time method
def filter_time(ex_Worker: Worker, ex_Employer: Employer):
    print("filter_time() function: \n")


# calculate and filter distance method
# limit distance to 20 miles or less -> if more than 20, remove from list
# Run for entire list? or individual?
# For checking next distance, add class value NewDistance and check if newDistance == NULL at start and then run with newDistance
def calc_distance(ex_Worker: Worker, ex_Employer: Employer):
    print("calc_distance() function: \n")

    # Testing 
    print("Worker Address test:")
    print(ex_Worker.address)

    print("\nEmployer Address Test: ")
    print(ex_Employer.address)

    # set address to temp location variables
    Worker_Location = geolocater.geocode(ex_Worker.address)
    employer_Location = geolocater.geocode(ex_Employer.address)

    print("Worker Address: ")
    print(Worker_Location )
    print("\nEmployer Address: " )
    print(employer_Location)

    # print("Distance in miles: " + str("{:.2f}".format(GD((Worker_Location.latitude, Worker_Location.longitude), 
    # (employer_Location.latitude, employer_Location.longitude)).miles)) + " miles")



# output?
def output():
    print("Output() function: \n")



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
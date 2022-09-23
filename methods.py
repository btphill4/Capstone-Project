# File to hold our methods to be called in main

# Install for geopy -> pip install geopy
# Install for pandas -> pip install pandas
from asyncio.windows_events import NULL
import psycopg2 
import pandas 
import numpy
from geopy import *

# connect to database method (From previous project)
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


# filter job type i.e. Gardening, etc method
def filter_jobType():
    print("filter_jobType() function: \n")


# filter Day and Time method
def filter_time():
    print("filter_time() function: \n")


# calculate and filter distance method
# Run for entire list? or individual?
# For checking next distance, add class value NewDistance and check if newDistance == NULL at start and then run with newDistance
def calc_distance():
    print("calc_distance() function: \n")


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
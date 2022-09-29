# File to hold our main function that will be ran 
from Employer import Employer
from Worker import Worker
# from pprint import pprint
from methods import *
import time

# from pyscog2 import connect

# # Connects to DB and saves to HO_list
# db_con = connect_to_db()
# cursor = db_con.cursor()

# # getting column names
# columns_db(cursor)
# col = [desc[0] for desc in cursor.description]


# #### Controls which tenant is used for matching ####
# tenant_id = 1
# #### 

# # gets tenant information
# tenant_db(tenant_id, cursor)
# item = cursor.fetchone()
# curr = dict(zip(col, item))



# ==============================================================================

# Test objects
ex_Employer = Employer("Employer_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Gardening", "Driving", "Babysitting"], 
                    "2083 Palmer Avenue", 0, 1, 1, 1, 1, 1, 0)

ex_Worker = Worker("Worker_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Babysitting", "Gardening", "Cooking"] , 
                    "2064 Maywood St", 0, 1, 1, 1, 1, 1, 0)

# alternate worker -> different jobs -> distance > 20 miles
ex_Worker1 = Worker("Worker_2", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Cooking"] , 
                    "145 Roe Ave", 0, 1, 1, 1, 1, 1, 0)

# print(ex_Worker)



# ==============================================================================

# Method Calls
print("==============================================================================================\n")
print("Begin Filtering for " + ex_Worker.worker_name + " and " + ex_Employer.employer_name + ":\n")

filter_jobType(ex_Worker, ex_Employer)

filter_time(ex_Worker, ex_Employer)

get_route(ex_Worker, ex_Employer)

# for time checking get_route
# tic = time.perf_counter()

# calc_distance(ex_Worker, ex_Employer)
print("End Filtering Iteration # \n")


print("==============================================================================================\n")
print("Filter Iteration # for " + ex_Worker.worker_name + " and " + ex_Employer.employer_name + ":\n")

# sleep for API call restriction 1 second restriction
time.sleep(1)

filter_jobType(ex_Worker1, ex_Employer)

# # Check time for API calls
# toc = time.perf_counter()
# print(f"Time between computations: {toc-tic:0.5f} seconds\n")

filter_time(ex_Worker1, ex_Employer)

get_route(ex_Worker1, ex_Employer)

# calc_distance(ex_Worker1, ex_Employer)

output()
print("End Filtering Iteration # \n")
print("==============================================================================================")

# ==============================================================================

# testing geopy -> need to fix "None" in method
print()
# print(ex_Worker.address)
# ex_Worker_add = ex_Worker.address
# print(ex_Worker_add)

# Worker_Location = geolocater.geocode(ex_Worker_add)
# print(Worker_Location)

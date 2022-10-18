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
# ex_Employer = Employer("Employer_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
#                     1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Gardening", "Driving", "Babysitting"], 
#                     "2083 Palmer Avenue", 0, 1, 1, 1, 1, 1, 0)

# ex_Worker = Worker("Worker_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
#                     1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Babysitting", "Gardening", "Cooking"] , 
#                     "2064 Maywood St", 0, 1, 1, 1, 1, 1, 0)

# # alternate worker -> different jobs -> distance > 20 miles
# ex_Worker1 = Worker("Worker_2", 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
#                     1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Cooking"] , 
#                     "145 Roe Ave", 0, 1, 1, 1, 1, 1, 0)

ex_Employer1 = Employer("Employer_2", 2, 0, 1, 0, 8, 13, ["Gardening", "Driving", "Babysitting"],
                    "3041 RIDGETOP ROAD Ottawa, Ontario K0A1T0", 0, 1, 1, 1, 1, 1, 0 )

ex_Worker2 = Worker("Worker2", 2, 1, 0, 1, 10, 13, ["Babysitting", "Gardening", "Cooking"], 
                    "70 RALLIDALE STREET Ottawa", 0, 0, 1, 1, 0, 1, 0 )

ex_Worker3 = Worker("Worker3", 3, 0, 0, 0, 15, 18, ["Cooking"], 
                    "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0 )

# print(ex_Worker)["Babysitting", "Gardening", "Cooking"], 


# add worker into list
Worker_list = []
Worker_list.append(ex_Worker2)
Worker_list.append(ex_Worker3)

# for obj in Worker_list:
#     print(obj.worker_name)

# ==============================================================================

# Order of filtering
# 0) filter gender
# 1) filter job skills (remove from list of workers/helpers)
# 2) filter days
# 3) filter time
# 4) filter distance (over 20 miles?)
# 5) sort by distance 
# 6) add top closest match to worker# list 
# 7) Redo loop until all helpers have 1 left in list

# ==============================================================================

i = 1
# Method Calls
print("==============================================================================================\n")
print("Begin Filtering for " + ex_Worker2.worker_name + " and " + ex_Employer1.employer_name + ":\n")

filter_gender(ex_Worker2, ex_Employer1)

filter_jobType(ex_Worker2, ex_Employer1)

filter_days(ex_Worker2, ex_Employer1)

filter_time(ex_Worker2, ex_Employer1)

get_route(ex_Worker2, ex_Employer1)

# for time checking get_route
# tic = time.perf_counter()

# calc_distance(ex_Worker, ex_Employer)
print("End Filtering Iteration #"+ str(i) + "\n")
i = i+1

print("==============================================================================================\n")
print("Filter Iteration # for " + ex_Worker3.worker_name + " and " + ex_Employer1.employer_name + ":\n")

# sleep for API call restriction 1 second restriction
time.sleep(1)

filter_gender(ex_Worker2, ex_Employer1)

filter_jobType(ex_Worker3, ex_Employer1)

# # Check time for API calls
# toc = time.perf_counter()
# print(f"Time between computations: {toc-tic:0.5f} seconds\n")

filter_days(ex_Worker3, ex_Employer1)

filter_time(ex_Worker3, ex_Employer1)

get_route(ex_Worker3, ex_Employer1)

# calc_distance(ex_Worker1, ex_Employer)

output()
print("End Filtering Iteration #" + str(i) + "\n")
print("==============================================================================================")
i = i+1
# ==============================================================================

# testing geopy -> need to fix "None" in method
print()
# print(ex_Worker.address)
# ex_Worker_add = ex_Worker.address
# print(ex_Worker_add)

# Worker_Location = geolocater.geocode(ex_Worker_add)
# print(Worker_Location)

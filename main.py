# File to hold our main function that will be ran 
from Employer import Employer
from Worker import Worker
# from pprint import pprint
from methods import *


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
ex_employer = Employer("Employer_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Gardening", "Driving", "Babysitting"], 
                    "348 Wheat Boom Dr #11, Oakville, ON L6H 0V1", 0, 1, 1, 1, 1, 1, 0)

ex_Worker = Worker("Worker_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Babysitting", "Gardening"] , 
                    "498 Markland St Unit 4, Markham, ON L6C 1Z6, Canada", 0, 1, 1, 1, 1, 1, 0)


# print(ex_Worker)



# ==============================================================================

# Method Calls

filter_jobType(ex_Worker, ex_employer)

filter_time(ex_Worker, ex_employer)

calc_distance(ex_Worker, ex_employer)

output()
# ==============================================================================

# testing geopy -> need to fix "None" in method
print()
print(ex_Worker.address)
ex_Worker_add = ex_Worker.address
print(ex_Worker_add)

Worker_Location = geolocater.geocode(ex_Worker_add)
print(Worker_Location)

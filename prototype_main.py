# File to hold our main function that will be ran 
from Employer import Employer
from Worker import Worker
# from pprint import pprint
from methods import *
import time


# ==============================================================================
# connect to database -> OLD PROJECT UPDATE FOR NEW PROJECT

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

# Create example class objects 
# Employer2 and worker3 are exactly the same to ensure matching works

ex_Employer1 = Employer("Employer1", 2, 0, 1, 0, 8, 13, ["Gardening", "Driving", "Babysitting"],
                    "3041 RIDGETOP ROAD Ottawa, Ontario K0A1T0", 0, 1, 1, 1, 1, 1, 0,
                    0, 0, 0, 0, 0, 0, 0 )

ex_Employer2 = Employer("Employer2", 3, 0, 0, 0, 15, 18, ["Cooking"], 
                    "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0,
                    0, 0, 0, 0, 0, 0, 0 )

ex_Worker2 = Worker("Worker2", 2, 1, 0, 1, 10, 13, ["Babysitting", "Gardening", "Cooking"], 
                    "70 RALLIDALE STREET Ottawa", 0, 0, 1, 1, 0, 1, 0,
                    0, 0, 0, 0, 0, 0, 0 )

ex_Worker3 = Worker("Worker3", 3, 0, 0, 0, 15, 18, ["Cooking"], 
                    "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0,
                        0, 0, 0, 0, 0, 0, 0 )


# ==============================================================================

# Add objects to a list to iterate through filtering -> IN PROGRESS

# add worker into list
Worker_list = []
Worker_list.append(ex_Worker2)
Worker_list.append(ex_Worker3)

# Print list of workers -> figure out how to properly print names
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
# 6) add top closest match to worker# lists
# 7) Redo loop until all helpers have 1 left in lists

# ==============================================================================

# Method calls -> filtering
# checker() -> used to print out extra information for each method -> DOES NOT FILTER
# out_list() -> calls the individual methods and filters the objects and adds to list -> DOES FILTER

# i = iteration number -> starts at 1
i = 1
# to calculate run time
tic = time.perf_counter() 

print("==============================================================================================")
print("=================================== Iteration " + str(i)+ " ==============================================")
print("==============================================================================================\n")

print("Begin Filtering for " + ex_Worker2.worker_name + " and " + ex_Employer1.employer_name + ":\n")
# checker(ex_Worker2, ex_Employer1)
out_list(ex_Worker2, ex_Employer1)

i = i + 1
print("==============================================================================================")
print("=================================== Iteration " + str(i)+ " ==============================================")
print("==============================================================================================\n")

print("Begin Filtering for " + ex_Worker2.worker_name + " and " + ex_Employer2.employer_name + ":\n")
# checker(ex_Worker2, ex_Employer2)
out_list(ex_Worker2, ex_Employer2)

i = i + 1
print("==============================================================================================")
print("=================================== Iteration " + str(i)+ " ==============================================")
print("==============================================================================================\n")

print("Begin Filtering for " + ex_Worker3.worker_name + " and " + ex_Employer1.employer_name + ":\n")
# checker(ex_Worker3, ex_Employer1)
out_list(ex_Worker3, ex_Employer1)

i = i + 1
print("==============================================================================================")
print("=================================== Iteration " + str(i)+ " ==============================================")
print("==============================================================================================\n")

print("Begin Filtering for " + ex_Worker3.worker_name + " and " + ex_Employer2.employer_name + ":\n")
# checker(ex_Worker3, ex_Employer1)
out_list(ex_Worker3, ex_Employer2)

# to calculate run time
toc = time.perf_counter() #

print(f"Total runtime: {toc-tic:0.5f} seconds\n") #


# ==============================================================================

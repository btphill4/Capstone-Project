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

ex_Employer1 = Employer("Employer1", 2, 0, 1, 0, 8, 13, ["Gardening"],
                    "3041 RIDGETOP ROAD Ottawa, Ontario K0A1T0", 0, 1, 1, 1, 1, 1, 0 )

ex_Employer2 = Employer("Employer2", 3, 0, 0, 0, 15, 18, ["Cooking"], 
                    "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0 )

ex_Employer3 = Employer("Employer3", 3, 0, 0, 0, 10, 18, ["Cooking"], 
                    "331 Ch. Vanier, Quebec", 0, 1, 1, 1, 1, 1, 0 )

ex_Employer4 = Employer("Employer4", 3, 0, 0, 0, 10, 13, ["Driving"], 
                    "27 BLACKSMITH ROAD|Lombardy, Ontario K0G1L0", 1, 1, 1, 1, 1, 1, 1 )

ex_Employer5 = Employer("Employer5", 3, 0, 0, 0, 15, 17, ["Gardening"], 
                    "510 VICTORIA STREET|Winchester, Ontario K0C2K0", 1, 1, 1, 1, 1, 1, 1 )

ex_Employer6 = Employer("Employer6", 0, 0, 0, 0, 13, 15, ["Cooking", "Driving", "Babysitting", "Gardening"],
                    "1468 DAVID ROAD|Rockland, Ontario K4K1K7", 0, 1, 1, 1, 1, 1, 0)

ex_Employer7 = Employer("Employer7", 0, 0, 0, 0, 10, 18, ["Driving"],
                    "00 GAGNE ROAD|Hammond, Ontario K0A2A0", 0, 1, 1, 1, 1, 1, 0)

ex_Employer8 = Employer("Employer8", 0, 0, 0, 0, 19, 24, ["Babysitting"],
                    "1025 GRENON AVENUE|Ottawa, Ontario K2B8S5", 0, 1, 1, 1, 1, 1, 0)

ex_Employer9 = Employer("Employer9", 0, 0, 0, 0, 10, 12, ["Cooking"],
                    "14 HILLTOP CRESCENT|Kemptville, Ontario K0G1J0", 0, 1, 1, 1, 1, 1, 0)

ex_Employer10 = Employer("Employer10", 0, 0, 0, 0, 20, 22, ["Babysitting"],
                    "119 MANOR WAY|Rideau Ferry, Ontario K0G1W0", 0, 1, 1, 1, 1, 1, 0)

ex_Employer11 = Employer("Employer11", 0, 0, 0, 0, 11, 12, ["Driving"],
                    "2 ALBERT STREET|Johnstown, Ontario K0E1T1", 0, 1, 1, 1, 1, 1, 0)

ex_Employer12 = Employer("Employer12", 0, 0, 0, 0, 8, 24, ["Babysitting"],
                    "607 ROBERT HILL STREET|Almonte, Ontario K0A1A0", 0, 1, 1, 1, 1, 1, 0)
            
ex_Worker1 = Worker("Worker1", 2, 1, 0, 1, 10, 13, ["Babysitting", "Cooking", "Gardening"], 
                    "2014 BOISFRANC CIRCLE", 0, 1, 0, 0, 0, 1, 0 )

ex_Worker2 = Worker("Worker2", 2, 1, 0, 1, 7, 22, ["Babysitting", "Gardening", "Cooking"], 
                    "70 RALLIDALE STREET Ottawa", 0, 0, 1, 1, 0, 1, 0 )

ex_Worker3 = Worker("Worker3", 3, 0, 0, 0, 2, 24, ["Cooking", "Babysitting", "Driving"], 
                    "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0 )

ex_Worker4 = Worker("Worker4", 3, 0, 0, 0, 9, 18, ["Tutoring", "Gardening"], 
                    "32 ALYSSA CRESCENT, Ontario", 0, 1, 1, 1, 1, 1, 0 )

ex_Worker5 = Worker("Worker5", 3, 0, 0, 0, 9, 18, ["Tutoring"], 
                    "35 Rue de la Futaie, Quebec", 0, 1, 1, 1, 1, 1, 0 )

ex_Worker6 = Worker("Worker6", 0, 0, 0, 0, 5, 12, ["Cooking", "Driving", "Babysitting", "Gardening"],
                    "7 BRIDGE STREET N|Kemptville, Ontario K0G1J0", 0, 1, 1, 1, 1, 1, 0)

ex_Worker7 = Worker("Worker7", 0, 0, 0, 0, 8, 24, ["Cooking", "Driving", "Babysitting"],
                    "172 CARSS AVENUE|Smiths Falls, Ontario K7A4B1", 0, 1, 1, 1, 1, 1, 0)

ex_Worker8 = Worker("Worker8", 0, 0, 0, 0, 0, 24, ["Driving", "Babysitting", "Gardening", "Cooking"],
                    "15 DIAMOND LANE|White Lake, Ontario K0A3L0", 0, 1, 1, 1, 1, 1, 0)


# ==============================================================================

# Add objects to a list to iterate through filtering -> IN PROGRESS

# add worker into list
Worker_list = []
Worker_list.append(ex_Worker1)
Worker_list.append(ex_Worker2)
Worker_list.append(ex_Worker3)
Worker_list.append(ex_Worker4)
Worker_list.append(ex_Worker5)
Worker_list.append(ex_Worker6)
Worker_list.append(ex_Worker7)
Worker_list.append(ex_Worker8)

Employer_List = []
Employer_List.append(ex_Employer1)
Employer_List.append(ex_Employer2)
Employer_List.append(ex_Employer3)
Employer_List.append(ex_Employer4)
Employer_List.append(ex_Employer5)
Employer_List.append(ex_Employer6)
Employer_List.append(ex_Employer7)
Employer_List.append(ex_Employer8)
Employer_List.append(ex_Employer9)
Employer_List.append(ex_Employer10)
Employer_List.append(ex_Employer11)
Employer_List.append(ex_Employer12)



# print("==============================================================================================")
# print("==============================================================================================")
# print("==============================================================================================")
# print("==============================================================================================")
# print("==============================================================================================")
# x = 0
# while x < len(Employer_List):
#     print(x)
#     out_list(Worker_list[x], Employer_List[x])
#     x = x + 1

# print("==============================================================================================")
# print("==============================================================================================")
# print("==============================================================================================")
# print("==============================================================================================")
# print("==============================================================================================")


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

count = 1
for employer in Employer_List:
    for worker in Worker_list:
        print("==============================================================================================")
        print("=================================== Iteration " + str(count)+ " ==============================================")
        print("==============================================================================================\n")
        print("Begin Filtering for " + worker.worker_name + " and " + employer.employer_name + ":\n")
        out_list(worker, employer)
        count = count + 1
        time.sleep(2)



# sort
for employer in Employer_List:
    for i in range(len(employer.matched_workers)):
        min_idx = i
        for j in range(i+1, len(employer.matched_workers)):
            if (employer.matched_workers[j][1] < employer.matched_workers[min_idx][1]):
                min_idx = j
        (employer.matched_workers[i], employer.matched_workers[min_idx]) = (employer.matched_workers[min_idx], employer.matched_workers[i])


for employer in Employer_List:
    print(employer.employer_name)
    for item in employer.matched_workers:
        print("\t" + item[0].worker_name + ": " + str(item[1]))
    print()

hasJob = []
for employer in Employer_List:
    for worker in employer.matched_workers:
        if (worker[0].worker_name not in hasJob):
           print(employer.employer_name + ": assigned to " + worker[0].worker_name)
           hasJob.append(worker[0].worker_name)
           break

# to calculate run time
toc = time.perf_counter() 
print(f"Total runtime: {toc-tic:0.5f} seconds\n") 


# ==============================================================================

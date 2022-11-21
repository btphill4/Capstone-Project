# File to hold our main function that will be ran 
# import class objects
from Employer import Employer
from Worker import Worker

# python libraries used in main and methods.py
# from pprint import pprint
from methods import *
import time
import copy


# ==============================================================================
# Create example class objects for testing -> will be filled in my database when implemented
# Employer2 and worker3 are exactly the same to ensure matching works

# Employer Variables 
# employer_name, employer_id, gender, gender_preferred, gender_matters, timeslot_id, 
# time_array, job_skills, address,
# sunday, monday, tuesday, wednesday, thursday, friday, saturday, payrate

ex_Employer1 = Employer(
"Employer1", # employer name
1,           # employer id
"Male",      # employer gender
"Female",    # employer preferred gender for the job
0,           # 0 = gender does not matter, 1 = gender matters
1,           # time slot id
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # time job should be at
["Gardening"], # skill required for job
"3041 RIDGETOP ROAD Ottawa, Ontario K0A1T0", # employer address 
0, 1, 1, 1, 1, 1, 0,  # day of the week the job should be on 
15   # pay for the job
)

# Same as worker3
ex_Employer2 = Employer("Employer2", 2,  "Male", "Male", 0, 2,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Cooking"], "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0, 15)

ex_Employer3 = Employer("Employer3", 3, "Female", "Female", 0, 3,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Cooking"], "331 Ch. Vanier, Quebec", 0, 1, 1, 1, 1, 1, 0, 15 )

ex_Employer4 = Employer("Employer4", 4, "Female", "Male", 0, 4,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Driving"], "27 BLACKSMITH ROAD|Lombardy, Ontario K0G1L0", 1, 1, 1, 1, 1, 1, 1, 16 )

ex_Employer5 = Employer("Employer5", 5, "Male", "Male", 0, 5,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  0,  0], 
["Gardening"], "510 VICTORIA STREET|Winchester, Ontario K0C2K0", 1, 1, 1, 1, 1, 1, 1, 15)

ex_Employer6 = Employer("Employer6", 6, "Female", "Male", 0, 6,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Cooking"], "1468 DAVID ROAD|Rockland, Ontario K4K1K7", 0, 1, 1, 1, 1, 1, 0, 16)

ex_Employer7 = Employer("Employer7", 7, "Non-binary", "Female", 0, 7,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Driving"], "00 GAGNE ROAD|Hammond, Ontario K0A2A0", 0, 1, 1, 1, 1, 1, 0, 14)

ex_Employer8 = Employer("Employer8", 8, "Non-binary", "Non-binary", 0, 8,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1], 
["Babysitting"], "1025 GRENON AVENUE|Ottawa, Ontario K2B8S5", 0, 1, 1, 1, 1, 1, 0, 15)

ex_Employer9 = Employer("Employer9", 9, "Male", "Male", 0, 9,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Cooking"], "14 HILLTOP CRESCENT|Kemptville, Ontario K0G1J0", 0, 1, 1, 1, 1, 1, 0, 15)

ex_Employer10 = Employer("Employer10", 10, "Female", "Female", 0, 10,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0], 
["Babysitting"], "119 MANOR WAY|Rideau Ferry, Ontario K0G1W0", 0, 1, 1, 1, 1, 1, 0, 14)

ex_Employer11 = Employer("Employer11", 11, "Male", "Female", 0, 11,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Driving"], "2 ALBERT STREET|Johnstown, Ontario K0E1T1", 0, 1, 1, 1, 1, 1, 0, 15)

ex_Employer12 = Employer("Employer12", 12, "Male", "Female", 0, 12,
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1], 
["Babysitting"], "607 ROBERT HILL STREET|Almonte, Ontario K0A1A0", 0, 1, 1, 1, 1, 1, 0, 16)

# add comment about what an employer is and how there can be multiple of the same for 
# multiple job requests per employer

# multiple jobs for the same employer in a row has to be checked

# ex_Employer12 = Employer("Employer12", 0, 0, 0, 0, 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
# ["Babysitting"], "607 ROBERT HILL STREET|Almonte, Ontario K0A1A0", 0, 1, 1, 1, 1, 1, 0)

# ex_Employer12 = Employer("Employer12", 0, 0, 0, 0, 
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
# ["Cooking"], "607 ROBERT HILL STREET|Almonte, Ontario K0A1A0", 0, 1, 1, 1, 1, 1, 0)

# Worker class variables 
# def __init__(self, worker_name, worker_id, gender, gender_preferred, gender_matters, timeslot_id,
#     time_array, job_skills, address, 
#     sunday, monday, tuesday, wednesday, thursday, friday, saturday ) 
#            
ex_Worker1 = Worker("Worker1", 1, "Non-binary", "Non-binary", 0, 1,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1], 
["Babysitting", "Cooking", "Gardening"], "2014 BOISFRANC CIRCLE", 0, 1, 0, 0, 0, 1, 0, 13 )

ex_Worker2 = Worker("Worker2", 2, "Male", "Female", 0, 2,
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0], 
["Babysitting", "Gardening", "Cooking"], "70 RALLIDALE STREET Ottawa", 0, 0, 1, 1, 0, 1, 0, 13 )

# Same as employer2 
ex_Worker3 = Worker("Worker3", 3, "Male", "Male", 0, 3,
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1], 
["Cooking", "Babysitting", "Driving"], "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0, 13)

ex_Worker4 = Worker("Worker4", 4, "Male", "Female", 0, 4,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Tutoring", "Gardening"], "32 ALYSSA CRESCENT, Ontario", 0, 1, 1, 1, 1, 1, 0, 14)

ex_Worker5 = Worker("Worker5", 5, "Female", "Female", 0, 5,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Tutoring"], "35 Rue de la Futaie, Quebec", 0, 1, 1, 1, 1, 1, 0, 13)

ex_Worker6 = Worker("Worker6", 6, "Non-binary", "Female", 0, 6,
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Cooking", "Driving", "Babysitting", "Gardening"], "7 BRIDGE STREET N|Kemptville, Ontario K0G1J0", 0, 1, 1, 1, 1, 1, 0, 13)

ex_Worker7 = Worker("Worker7", 7, "Female", "Female", 0, 7,
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1], 
["Cooking", "Driving", "Babysitting"], "172 CARSS AVENUE|Smiths Falls, Ontario K7A4B1", 0, 1, 1, 1, 1, 1, 0, 13)

ex_Worker8 = Worker("Worker8", 8, "Male", "Female", 0, 8,
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1], 
["Driving", "Babysitting", "Gardening", "Cooking"], "15 DIAMOND LANE|White Lake, Ontario K0A3L0", 0, 1, 1, 1, 1, 1, 0, 13)


# Check for multi job matching for same employer and worker
ex_Worker9 = Worker("Worker9", 9, "Female", "Male", 0, 1,
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0], 
["Gardening", "Babysitting"], "51 NORICE STREET Ottawa, Ontario", 0, 1, 1, 1, 1, 1, 0, 13)

ex_Employer13 = Employer("Employer13", 13, "Male", "Male", 0, 13,
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Gardening"], "607 ROBERT HILL STREET|Almonte, Ontario K0A1A0", 0, 1, 1, 1, 1, 1, 0, 13)

ex_Employer13_1 = Employer("Employer13_1", 13_1, "Male", "Male", 0, 13_1,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0], 
["Babysitting"], "607 ROBERT HILL STREET|Almonte, Ontario K0A1A0", 0, 1, 1, 1, 1, 1, 0, 13)

# ex_Worker10 = Worker("Worker10", 10, "Male", "Male", 1, 10,
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0], 
# ["Gardening"], "51 NORICE STREET Ottawa, Ontario", 0, 1, 1, 1, 1, 1, 0 )


# ==============================================================================
# Add objects to a list to iterate through filtering
# For testing objects above -> will be automatically filled by database when implemented

# add employer objects to a list 
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
Employer_List.append(ex_Employer13)
Employer_List.append(ex_Employer13_1)


Worker_List = []
Worker_List.append(ex_Worker1)
Worker_List.append(ex_Worker2)
Worker_List.append(ex_Worker3)
Worker_List.append(ex_Worker4)
Worker_List.append(ex_Worker5)
Worker_List.append(ex_Worker6)
Worker_List.append(ex_Worker7)
Worker_List.append(ex_Worker8)
Worker_List.append(ex_Worker9)

# ==============================================================================
# Matching starts here

#perform initial matching -> single job matching
for employer in Employer_List:
    for worker in Worker_List:
         match(worker, employer)

# # print workers and their matched employers -> for testing
# for worker in Worker_List:
#     print(worker.worker_name + " length is " + str(len(worker.matched_employers)))
#     for item in worker.matched_employers:
#         print("\t" + item.employer_name)
#     print()

# ==============================================================================
# Create distance dictionary for every possible address combination
dist_dict = {}
CalcDistanceDict2(Employer_List, Worker_List, dist_dict)

# add distances to all the objects using dictionary dist_dict
addDistanceToMatches(Worker_List, dist_dict)

# sorts worker and employer lists by distance
sortMatchedWorkers(Employer_List)
sortMatchedEmployers(Worker_List)

# multiple job matching
Copy_Worker_List = copy.deepcopy(Worker_List)
Copy_Employer_List = copy.deepcopy(Employer_List)

# Finished list holds the finalized list of workers and each employer
# jobs_taken_list holds the jobs already assigned to workers/employers
# max_distance to filter out jobs that are too far for the workers 
#   -> can be changed according to sponsor preference
finished_list = {}
job_taken_list = []
max_distance = 30

# initial multiple job matching
# adds matches in finished_list to return to database 
for worker in Copy_Worker_List:
    repeat = True
    print(worker.worker_name)
    for x in worker.matched_employers:
        print("\t" + x[0].employer_name + ": " + str(x[1]))
    while(repeat is True):
        if (worker not in finished_list):
            finished_list[worker] = []
        if (len(worker.matched_employers) > 0):
            if (worker.matched_employers[0][1] <= max_distance):
                if (worker.matched_employers[0][0] not in job_taken_list):
                    if (checkTimeArray(worker, worker.matched_employers[0][0])):
                        # remove the used time slots from the worker's time array
                        work_array = np.array(worker.time_array)
                        employ_array = np.array(worker.matched_employers[0][0].time_array)
                        worker.time_array = np.subtract(work_array, employ_array).tolist()
                        
                        # adds the job to the worker's list of jobs
                        finished_list[worker].append(worker.matched_employers[0][0])
                        
                        # sets the worker's address to the location of the job
                        worker.address = worker.matched_employers[0][0].address
                        
                        # marks the job as taken
                        job_taken_list.append(worker.matched_employers[0][0])
                    else:
                        print("\ntime did not match for " + worker.matched_employers[0][0].employer_name + " trying next closest place\n")
                # consumes the job for the current worker
                del worker.matched_employers[0]
                
                # calculates new distances
                #match_update(worker, Copy_Employer_List, job_taken_list, dist_dict);
                RecalcDistances(worker, dist_dict)
                print(worker.worker_name)
                for x in worker.matched_employers:
                    print("\t" + x[0].employer_name + ": " + str(x[1]))
            else:
                print("\nnext closest destination, " + worker.matched_employers[0][0].employer_name + " is too far, trying next closest place\n")
                repeat = False
        else:
            # print("Worker " + worker.name + "'s list is 0")
            repeat = False

# print worker schedules
print("--------- schedules ----------")
for key in finished_list.keys():
    print(key.worker_name)
    for item in finished_list[key]:
        print("\t" + item.employer_name)
    print()

# Final check for printing all possible matches for testing 
# print workers and their matched employers
# for worker in Copy_Worker_List:
#     print(worker.worker_name + " length is " + str(len(worker.matched_employers)))
#     for item in worker.matched_employers:
#         print("\t" + item[0].employer_name + ": " + str(item[1]))
#     print()
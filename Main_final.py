# File to hold our main function that will be ran 
from Employer import Employer
from Worker import Worker
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
"3041 RIDGETOP ROAD Ottawa, Ontario", # employer address 
0, 1, 1, 1, 1, 1, 0,  # day of the week the job should be on 
15,   # pay for the job
0,    # job id, should be unique number in the job table in the database
)

# Same as worker3
ex_Employer2 = Employer("Employer2", 2,  "Male", "Male", 0, 2,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Cooking"], "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0, 15, 1)

ex_Employer3 = Employer("Employer3", 3, "Female", "Female", 0, 3,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Cooking"], "331 Ch. Vanier, Quebec", 0, 1, 1, 1, 1, 1, 0, 15, 2)

ex_Employer4 = Employer("Employer4", 4, "Female", "Male", 0, 4,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Driving"], "27 BLACKSMITH ROAD|Lombardy, Ontario K0G1L0", 1, 1, 1, 1, 1, 1, 1, 16, 3)

ex_Employer5 = Employer("Employer5", 5, "Male", "Male", 0, 5,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  0,  0], 
["Gardening"], "510 VICTORIA STREET|Winchester, Ontario K0C2K0", 1, 1, 1, 1, 1, 1, 1, 15, 4)

ex_Employer6 = Employer("Employer6", 6, "Female", "Male", 0, 6,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Cooking"], "1468 DAVID ROAD|Rockland, Ontario K4K1K7", 0, 1, 1, 1, 1, 1, 0, 16, 5)

ex_Employer7 = Employer("Employer7", 7, "Non-binary", "Female", 0, 7,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Driving"], "00 GAGNE ROAD|Hammond, Ontario K0A2A0", 0, 1, 1, 1, 1, 1, 0, 14, 6)

ex_Employer8 = Employer("Employer8", 8, "Non-binary", "Non-binary", 0, 8,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1], 
["Babysitting"], "1025 GRENON AVENUE|Ottawa, Ontario K2B8S5", 0, 1, 1, 1, 1, 1, 0, 15, 7)

ex_Employer9 = Employer("Employer9", 9, "Male", "Male", 0, 9,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Cooking"], "14 HILLTOP CRESCENT|Kemptville, Ontario K0G1J0", 0, 1, 1, 1, 1, 1, 0, 15, 8)

ex_Employer10 = Employer("Employer10", 10, "Female", "Female", 0, 10,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0], 
["Babysitting"], "119 MANOR WAY|Rideau Ferry, Ontario K0G1W0", 0, 1, 1, 1, 1, 1, 0, 14, 9)

# 1 Check for multi job matching for same employer and worker
ex_Employer11 = Employer("Employer11", 11, "Male", "Female", 0, 11,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Driving"], "2 ALBERT STREET|Johnstown, Ontario K0E1T1", 0, 1, 1, 1, 1, 1, 0, 15, 10)

ex_Employer11_1 = Employer("Employer11_1", 11, "Male", "Female", 0, 11,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Cooking"], "2 ALBERT STREET|Johnstown, Ontario K0E1T1", 0, 1, 1, 1, 1, 1, 0, 15, 11)

ex_Employer11_2 = Employer("Employer11_2", 11, "Male", "Female", 0, 11,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Babysitting"], "2 ALBERT STREET|Johnstown, Ontario K0E1T1", 0, 1, 1, 1, 1, 1, 0, 15, 12)


ex_Employer12 = Employer("Employer12", 12, "Male", "Female", 0, 12,
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1], 
["Babysitting"], "607 ROBERT HILL STREET|Almonte, Ontario K0A1A0", 0, 1, 1, 1, 1, 1, 0, 16, 13)
       
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


# 2 Check for multi job matching for same employer and worker 2
ex_Worker9 = Worker("Worker9", 9, "Female", "Male", 0, 1,
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0], 
["Gardening", "Babysitting"], "51 NORICE STREET Ottawa, Ontario", 0, 1, 1, 1, 1, 1, 0, 13)

ex_Employer13 = Employer("Employer13", 13, "Male", "Male", 0, 13,
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Gardening"], "607 ROBERT HILL STREET Almonte, Ontario", 0, 1, 1, 1, 1, 1, 0, 13, 14)

ex_Employer13_1 = Employer("Employer13_1", 13, "Male", "Male", 0, 13_1,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0], 
["Babysitting"], "607 ROBERT HILL STREET Almonte, Ontario", 0, 1, 1, 1, 1, 1, 0, 13, 15)

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
Employer_List.append(ex_Employer11_1)
Employer_List.append(ex_Employer11_2)
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


#perform initial matching
for employer in Employer_List:
    for worker in Worker_List:
         match(worker, employer) # creates a list of matched employers for each worker


 # print workers and their matched employers
for worker in Worker_List:
    print(worker.worker_name + " length is " + str(len(worker.matched_employers)))
    for item in worker.matched_employers:
        print("\t" + item.employer_name)
    print()


# ==============================================================================
# Create distance dictionary for every possible address combination

# The current API used is only allowed for non-commercial uses. The get_route function should
# be changed to use a paid routing API such as google maps API instead when the program is in use.
# It should be fairly simple to change.

# creates a dictionary with two addresses as the key and the distance between them
# as the value
dist_dict = {} 
CalcDistanceDict2(Employer_List, Worker_List, dist_dict)


# add distances to all the objects using dictionary dist_dict
addDistanceToMatches(Worker_List, dist_dict)

# matched_employers list after this call now contains tuples where the first item is the 
# employer object and the second object is the distance to the worker


# sorts worker and employer lists by distance
#sortMatchedWorkers(Employer_List)
sortMatchedEmployers(Worker_List)


# multiple job matching preparation

# the multi-job matching runs off copies of the worker/employer list 
Copy_Worker_List = copy.deepcopy(Worker_List)
Copy_Employer_List = copy.deepcopy(Employer_List)

# make job_id dictionary
# key is the job_id, value is the employer object that is associated with the job_id
job_dict = {};
for employer in Copy_Employer_List:
    if (employer.job_id not in job_dict):
        job_dict[employer.job_id] = employer
        
# make worker_id dictionary
# key is the worker_id, value is the worker associated with that worker_id
worker_id_dict = {};
for worker in Copy_Worker_List:
    if (worker.worker_id not in worker_id_dict):
        worker_id_dict[worker.worker_id] = worker



finished_list = {}
job_taken_list = []
max_distance = 30
max_multi_distance = 45
worker_list = {}; 

# create list of jobs for each employer under each worker 
for worker in Copy_Worker_List:    # for loop through each worker
    worker_list[worker.worker_id] = {};    # initialize each key value pair to a dictionary
    for employer in worker.matched_employers:   # for loop through matched employer list (list of employers that matched with the worker)
        job_id = employer[0].job_id;    # gets the job_id (unique value) from the employer object
        emp_id = employer[0].employer_id;    # gets the employer_id from the employer object
        if (emp_id not in worker_list[worker.worker_id]):   # if the employer id does not exist in the worker list dictionary for the current worker
            worker_list[worker.worker_id][emp_id] = [job_id]; # set the employer id to a list containing the job id
        else: # if the employer id already has a list in the worker list for the current worker 
            worker_list[worker.worker_id][emp_id].append(job_id);  # append the job id to the list


# before
# Worker 3
#     13: [10, 11]
# Worker 2
#     13: [10, 11, 12]
# Worker 8
#     13: [10, 11, 12]
# Worker 1
#     13: [10]

# after
# Worker 2
#     13: [10, 11, 12] ---- 28
# Worker 8
#     13: [10, 11, 12] ---- 34
# Worker 3
#     13: [10, 11]
# Worker 1
#     13: [10]

# adds jobs to worker lists in order of most items in list to least
# worker_list_sorted[worker_id, employer_id, job_list, len(job_list), distance]
# item[0] = worker_id
# item[1] = employer_id
# item[2] = job_list
# item[3] = len(job_list)
# item[4] = distance
worker_list_sorted = [];
for item in worker_list.items():
    for item2 in item[1].items():
        if (len(item2[1]) > 1):
            index = 0;
            distance = dist_dict[worker_id_dict[item[0]].address, job_dict[item2[1][0]].address]
            if (len(worker_list_sorted) == 0): # if the list is empty, add the first item to the list
                worker_list_sorted.append([item[0], item2[0], item2[1], len(item2[1]), distance])
            else:  # if the list has entries, insert it into its sorted position
                while (worker_list_sorted[index][3] > len(item2[1])):
                    index += 1;
                worker_list_sorted.insert(index, [item[0], item2[0], item2[1], len(item2[1]), distance])

# worker_list_sorted[worker_id, employer_id, job_list, len(job_list), distance]
                
# sort the worker_list by number of jobs primarily, then driving distance secondary
for i in range(len(worker_list_sorted)):
    max_index = i;
    for j in range(i+1, len(worker_list_sorted)):
        
        # if the number of items in the list is greater than the max index
        if (worker_list_sorted[j][3] > worker_list_sorted[max_index][3]): 
            max_index = j; # set the max index to the current index
            
        # else if the number of items in the list are equal, check if the distance of theh current
        # index is closer than the max index
        elif (worker_list_sorted[j][3] == worker_list_sorted[max_index][3]):
            if (worker_list_sorted[j][4] < worker_list_sorted[max_index][4]):
                max_index = j; # set the max index to the current index
    worker_list_sorted[max_index], worker_list_sorted[i] = worker_list_sorted[i], worker_list_sorted[max_index];

# bubble sort to compare the time arrays to make sure the first job in the list has the earliest start time
for i in range(len(worker_list_sorted)):
    for j in range(0, len(worker_list_sorted[i][2])):
        for k in range(0, len(worker_list_sorted[i][2])-1):
            if (compareTime(job_dict[worker_list_sorted[i][2][k]].time_array, job_dict[worker_list_sorted[i][2][k+1]].time_array) == False):
                worker_list_sorted[i][2][k], worker_list_sorted[i][2][k+1] = worker_list_sorted[i][2][k+1], worker_list_sorted[i][2][k]

# print
for item in worker_list_sorted:
    print(worker_id_dict[item[0]].worker_name)
    print("\t" + str(item[1]) + ": " + str(item[2]) + " --- distance: " + str(item[4])) 


# worker_list_sorted[worker_id, employer_id, job_list, len(job_list), distance]
# item[0] = worker_id
# item[1] = employer_id
# item[2] = job_list
# item[3] = len(job_list)
# item[4] = distance
# add the jobs to the best worker for them

# this is very similar to the multijob matching iteration below,
# it has print statements to show what is going on
for item in worker_list_sorted:
    worker = worker_id_dict[item[0]]
    if (worker not in finished_list):
        finished_list[worker] = []
    if (item[3] > 1):
        if (item[4] < max_multi_distance):
            last_job = item[2][0]
            for job in item[2]:
                last_job = job;
                if (job_dict[job].job_id not in job_taken_list):
                    if (checkTimeArray(worker, job_dict[job])):
                        # remove used time slots from the worker's time array
                        work_array = np.array(worker.time_array)
                        employ_array = np.array(job_dict[job].time_array)
                        worker.time_array = np.subtract(work_array, employ_array).tolist()
                        
                        # adds the job to the worker's list of jobs
                        finished_list[worker].append(job_dict[job])
                        
                        # sets the worker's address to the location of the job
                        worker.address = job_dict[job].address
                        
                        # marks the job as taken
                        job_taken_list.append(job_dict[job].job_id)
            
            # if the worker claimed all the jobs for that employer, add an extra hour of padding at the end
            if (len(finished_list[worker]) == item[3]):
                extra_hour = getLastTimeIndexPlusOne(job_dict[last_job].time_array)
                if (extra_hour != -1):
                    worker.time_array[extra_hour] = 0;    


# print worker schedules after first iteration
print("--------- schedules ----------")
for key in finished_list.keys():
    print(key.worker_name)
    for item in finished_list[key]:
        print("\t" + item.employer_name)
    print()



show_print_statements = True
# Finished list holds the finalized list of workers and each employer
# jobs_taken_list holds the jobs already assigned to workers/employers
# max_distance to filter out jobs that are too far for the workers 
#   -> can be changed according to sponsor preference
# initial multiple job matching
for worker in Copy_Worker_List:
    repeat = True
    print(worker.worker_name)
    # for x in worker.matched_employers:
    #     print("\t" + x[0].employer_name + ": " + str(x[1]))
    while(repeat is True):
        if (worker not in finished_list):
            finished_list[worker] = []
        if (show_print_statements):
            print("\tmatched employers length " + str(len(worker.matched_employers)) + " > 0 ---- " + str(len(worker.matched_employers) > 0))
        if (len(worker.matched_employers) > 0):
            if (show_print_statements):
                print("\tmatched employer distance " + str(worker.matched_employers[0][1]) + " <= " + str(max_distance) + " ---- " + str(worker.matched_employers[0][1] <= max_distance)) 
            if (worker.matched_employers[0][1] <= max_distance):
                if (show_print_statements):
                    print("\temployer job id " + str(worker.matched_employers[0][0].job_id) + " not in " + str(job_taken_list) + " ---- " + str(worker.matched_employers[0][0].job_id not in job_taken_list))
                if (worker.matched_employers[0][0].job_id not in job_taken_list):
                    if (show_print_statements):
                        print("\tworker array: " + str(worker.time_array));
                        print("\temploy array: " + str(worker.matched_employers[0][0].time_array));
                        print("\tresult array: " + str(np.subtract(np.array(worker.time_array), np.array(worker.matched_employers[0][0].time_array)).tolist()))
                        print("\ttime check: " + str(checkTimeArray(worker, worker.matched_employers[0][0])));
                    if (checkTimeArray(worker, worker.matched_employers[0][0])):
                        
                        # remove the used time slots from the worker's time array
                        work_array = np.array(worker.time_array)
                        employ_array = np.array(worker.matched_employers[0][0].time_array)
                        worker.time_array = np.subtract(work_array, employ_array).tolist()
                        
                        if (show_print_statements):
                            print("\tnew time array: " + str(worker.time_array))
                        
                        # remove extra hour at the end of the job to account for traveling to the next one
                        extra_hour = getLastTimeIndexPlusOne(employ_array.tolist())
                        if (extra_hour != -1):
                            worker.time_array[extra_hour] = 0;
                        
                        if (show_print_statements):
                            print("\textra hour removed: " + str(worker.time_array))
                        
                        if (show_print_statements):
                            finished_list_print = "\t";
                            for item in finished_list[worker]:
                                finished_list_print += item.employer_name + ", ";
                            finished_list_print = finished_list_print[:-2]    
                            print("\tfinished list for worker before: " + finished_list_print);
                        
                        # adds the job to the worker's list of jobs
                        finished_list[worker].append(worker.matched_employers[0][0])
                        
                        if (show_print_statements):
                            finished_list_print = "\t";
                            for item in finished_list[worker]:
                                finished_list_print += item.employer_name + ", ";
                            finished_list_print = finished_list_print[:-2]    
                            print("\tfinished list for worker after: " + finished_list_print);
                                                          
                        if (show_print_statements):
                            print("\tsetting worker address to: " + str(worker.matched_employers[0][0].address))
                        # sets the worker's address to the location of the job
                        worker.address = worker.matched_employers[0][0].address
                        if (show_print_statements):
                            print("\tjob taken list: " + str(job_taken_list))
                        # marks the job as taken
                        job_taken_list.append(worker.matched_employers[0][0].job_id)
                    #else:
                        #print("\ntime did not match for " + worker.matched_employers[0][0].employer_name + " trying next closest place\n")
                # consumes the job for the current worker
                del worker.matched_employers[0]
                
                # calculates new distances
                #match_update(worker, Copy_Employer_List, job_taken_list, dist_dict);
                RecalcDistances(worker, dist_dict)
                if (show_print_statements):
                    for item in worker.matched_employers:
                        print("\t\t" + item[0].employer_name + " - " + str(item[1]) + " miles")
                print(worker.worker_name)
                #for x in worker.matched_employers:
                    #print("\t" + x[0].employer_name + ": " + str(x[1]))
            else:
                print("\tthe next closest destinatiton is too far, exiting loop")
                repeat = False
        else:
            print("\tlist size is 0, exiting loop")
            repeat = False


# print worker schedules
print("--------- schedules ----------")
for key in finished_list.keys():
    print(key.worker_name)
    for item in finished_list[key]:
        print("\t" + item.employer_name)
    print()
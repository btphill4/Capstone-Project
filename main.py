# File to hold our main function that will be ran 
# from methods import *
from Employer import Employer
from Employee import Employee
from pprint import pprint

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

def filter_jobType(ex_Employee: Employee, ex_Employer: Employer):
    print("filter_jobType() function: \n")
    if ex_Employee.job_skills == ex_Employer.job_skills:

        # job is matched
        print("Job Matched for: " + ex_Employee.employee_name + " and " + ex_Employer.employer_name +
                " for job(s): " + ex_Employee.job_skills)

    elif ex_Employee.job_skills != ex_Employer.job_skills:
        print("Jobs NOT Matched for: " + ex_Employee.employee_name + " and " + ex_Employer.employer_name)



ex_employer = Employer("Employer1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, "Gardening", 
                    "348 Wheat Boom Dr #11, Oakville, ON L6H 0V1", 0, 1, 1, 1, 1, 1, 0)

ex_employee = Employee("Employee1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, "Gardening", 
                    "498 Markland St Unit 4, Markham, ON L6C 1Z6, Canada", 0, 1, 1, 1, 1, 1, 0)

# print(ex_employee)

# Method Calls

filter_jobType(ex_employee, ex_employer)
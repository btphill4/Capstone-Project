# File to hold our main function that will be ran 
from Employer import Employer
from Employee import Employee
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


ex_employer = Employer("Employer_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Gardening", "Driving", "Babysitting"], 
                    "348 Wheat Boom Dr #11, Oakville, ON L6H 0V1", 0, 1, 1, 1, 1, 1, 0)

ex_employee = Employee("Employee_1", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 
                    1, 1, 1, 1, 1, 0 , 0, 0, 0, 0, ["Babysitting", "Gardening"] , 
                    "498 Markland St Unit 4, Markham, ON L6C 1Z6, Canada", 0, 1, 1, 1, 1, 1, 0)

# print(ex_employee)

# Method Calls

filter_jobType(ex_employee, ex_employer)
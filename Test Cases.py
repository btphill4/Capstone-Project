# File to hold our main function that will be ran 
from Employer import Employer
from Worker import Worker
# from pprint import pprint
from methods import *
import time
import copy



# Test case for 1 employer female to 1 worker female
# Same skill sets, same days
# Expected Results -> matched
ex_Employer1 = Employer("Employer1", 2,  "Female", "Female", 1, 2,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0], 
["Cooking"], "514 GILMOUR STREET Ottawa, Ontario K1R5L4", 0, 1, 1, 1, 1, 1, 0 )

ex_Worker1 = Worker("Worker1", 1, "Female", "Female", 1, 1,
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
["Cooking", "Cooking", "Gardening"], "2014 BOISFRANC CIRCLE", 0, 1, 0, 0, 0, 1, 0 )



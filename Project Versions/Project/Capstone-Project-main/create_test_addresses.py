import csv
import time
from methods import *

newList = []
with open('real_addresses_test.csv', newline='') as csvfile:
    
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        result = test_route(row[0])
        if (result != None):
            print(row[0] + ": " + str(result.latitude) + ", " + str(result.longitude))
            newList.append(row[0])
        time.sleep(1)    

f = open("real_addresses_working.csv", "w")
for item in newList:
    f.write("\"" + item + "\"\n")
f.close()
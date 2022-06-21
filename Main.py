
# Import template - to be updated with proper files
import csv

#Store imported data in an empty array imported
imported = []

#Figure out how to change the path for it to work on all machines
with open("/home/brandon/Desktop/business.csv", 'r') as businessFile:
    rows = csv.reader(businessFile, delimiter= ',')
    for r in rows:
        #append(r[0]) get first column, append(r[1]) gets 2nd column
        imported.append(r[1])
        #print(r)

print(imported)
#CSV is imported and added to array(imported) 

#Matching starts here




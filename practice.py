import names ## Get this by installing names (pip install names)
import random
import json

with open('jobs.json', 'r') as f:
    data = f.read()
jobs = json.loads(data)

def getRandomFirstName():
    firstName = names.get_first_name()
    return firstName

def getRandomLastName():
    lastName = names.get_last_name()
    return lastName

def getRandomJob():
    ran = random.randrange(len(jobs['jobList']))
    job = jobs['jobList'][ran].rstrip()
    return job

def getRandomTime():
    day = random.randrange(0,6,1)
    start = random.randrange(0,22,1)
    end = random.randrange(start+1,23, 1)
    dayAndTime = [day,start,end]
    return dayAndTime

## Calls- just to check it works
print(getRandomFirstName())
print(getRandomLastName())
print(getRandomJob())
print(getRandomTime())

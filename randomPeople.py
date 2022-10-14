import names ## Get this by installing names (pip install names)
import random
import json

with open('jobs.json', 'r') as f:
    data = f.read()
jobs = json.loads(data)

def getRandomGender():
    gender = random.randrange(0,2)
    return gender

## Use only for employee
def getRandomGenderedFirstName(gender):
    if gender == 0:
        firstName = names.get_first_name(gender='male')
    if gender == 1:
        firstName = names.get_first_name(gender='female')
    return firstName

## Use only for employer
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
    end = random.randrange(start+1,24, 1)
    dayAndTime = [day,start,end]
    return dayAndTime

## Returns an employee in an array with gender, name according to gender, job, and time
def getRandomEmployee():
    gender = getRandomGender()
    firstName = getRandomGenderedFirstName(gender)
    lastName = getRandomLastName()
    job = getRandomJob()
    time = getRandomTime()
    employee = [gender,firstName,lastName,job,time]
    return employee


## Calls- just to check it works
employee = getRandomEmployee()
print(employee[0])
print(employee[1])
print(employee[2])
print(employee[3])
print(employee[4])

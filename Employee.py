# Employee Class Objects

from time import timezone


class Employee:
    #in order based on schema.txt
    def __init__(self, employee_name, employee_id, timeslot_id, timezone, hour_0, hour_1, hour_2,
        hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12,
        hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, 
        hour_23, job_skills, address, sunday, monday, tuesday, wednesday, thursday, friday, saturday):

        self.employee_name = employee_name
        self.employee_id = employee_id
        self.timeslot_id = timeslot_id
        self.timezone = timezone
        self.hour_0 = hour_0
        self.hour_1 = hour_1
        self.hour_2 = hour_2
        self.hour_3 = hour_3
        self.hour_4 = hour_4
        self.hour_5 = hour_5
        self.hour_6 = hour_6
        self.hour_7 = hour_7
        self.hour_8 = hour_8
        self.hour_9 = hour_9
        self.hour_10 = hour_10
        self.hour_11 = hour_11
        self.hour_12 = hour_12
        self.hour_13 = hour_13
        self.hour_14 = hour_14
        self.hour_15 = hour_15
        self.hour_16 = hour_16
        self.hour_17 = hour_17
        self.hour_18 = hour_18
        self.hour_19 = hour_19
        self.hour_20 = hour_20
        self.hour_21 = hour_21
        self.hour_22 = hour_22
        self.hour_23 = hour_23
        self.job_skills = job_skills
        self.address = address
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        

        
        #class methods if needed here

        # def get_appid(self):
        #     print("appplication ID: " + self.appid)

        # def updateMatchPercent(self, value):
        #     self.matchPercent = self.matchPercent + value

        # def get_MatchPercent(self):
        #     print("Homeowner:", self.appid ,"Match Percent:", self.matchPercent)

        #pass avoids empty object error          
        pass
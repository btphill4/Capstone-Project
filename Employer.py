# Employee Class Objects

from time import timezone


class Employer:
    #in order based on schema.txt
    def __init__(self, employer_name, employer_id, gender, timeslot_id, timezone, start_time, end_time, 
    job_skills, address, sunday, monday, tuesday, wednesday, thursday, friday, saturday, 
    sunday_matched, monday_matched, tuesday_matched, wednesday_matched, thursday_matched, friday_matched, 
    saturday_matched ):

        self.employer_name = employer_name
        self.employer_id = employer_id
        self.gender = gender
        self.timeslot_id = timeslot_id
        self.timezone = timezone
        self.start_time = start_time
        self.end_time = end_time
        # self.hour_0 = hour_0
        # self.hour_1 = hour_1
        # self.hour_2 = hour_2
        # self.hour_3 = hour_3
        # self.hour_4 = hour_4
        # self.hour_5 = hour_5
        # self.hour_6 = hour_6
        # self.hour_7 = hour_7
        # self.hour_8 = hour_8
        # self.hour_9 = hour_9
        # self.hour_10 = hour_10
        # self.hour_11 = hour_11
        # self.hour_12 = hour_12
        # self.hour_13 = hour_13
        # self.hour_14 = hour_14
        # self.hour_15 = hour_15
        # self.hour_16 = hour_16
        # self.hour_17 = hour_17
        # self.hour_18 = hour_18
        # self.hour_19 = hour_19
        # self.hour_20 = hour_20
        # self.hour_21 = hour_21
        # self.hour_22 = hour_22
        # self.hour_23 = hour_23
        self.job_skills = job_skills
        self.address = address
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday_matched = sunday_matched
        self.monday_matched = monday_matched
        self.tuesday_matched = tuesday_matched
        self.wednesday_matched = wednesday_matched
        self.thursday_matched = thursday_matched
        self.friday_matched = friday_matched
        self.saturday_matched = saturday_matched
        

        
        #class methods if needed here
        def addressToString(self):
            print("Employer address: " + self.address)
            tempAddress = self.address
            return tempAddress
        
        # def get_appid(self):
        #     print("appplication ID: " + self.appid)

        # def updateMatchPercent(self, value):
        #     self.matchPercent = self.matchPercent + value

        # def get_MatchPercent(self):
        #     print("Homeowner:", self.appid ,"Match Percent:", self.matchPercent)

        #pass avoids empty object error          
        pass
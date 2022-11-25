# Employee Class Objects

from time import timezone


class Employer:
    #in order based on schema.txt
    def __init__(self, employer_name, employer_id, gender, gender_preferred, gender_matters, 
    timeslot_id, time_array, job_skills, address, 
    sunday, monday, tuesday, wednesday, thursday, friday, saturday, payrate, job_id ):

    # def __init__(self, employer_name, employer_id, gender, timeslot_id, timezone, start_time, end_time, 
    # job_skills, address, sunday, monday, tuesday, wednesday, thursday, friday, saturday, 
    # sunday_matched, monday_matched, tuesday_matched, wednesday_matched, thursday_matched, friday_matched, 
    # saturday_matched ):

        self.employer_name = employer_name
        self.employer_id = employer_id
        self.gender = gender
        self.gender_preferred = gender_preferred
        self.gender_matters = gender_matters
        self.timeslot_id = timeslot_id
        self.time_array = time_array
        self.job_skills = job_skills
        self.address = address
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.matched_workers = []
        self.payrate = payrate;
        self.job_id = job_id

        
        #class methods if needed here
        def addressToString(self):
            print("Employer address: " + self.address)
            tempAddress = self.address
            return tempAddress
        
            #pass avoids empty object error          
        pass
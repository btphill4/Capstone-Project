# Worker Class Objects

from time import timezone

# change to helper
class Worker:
    #in order based on schema.txt
    def __init__(self, worker_name, worker_id, gender, gender_preferred, gender_matters, 
    timeslot_id, time_array, job_skills, address, 
    sunday, monday, tuesday, wednesday, thursday, friday, saturday, payrate ):
        
        
        self.start_time = 7
        self.end_time = 14
        # 10 - 11
        # 7 - 10, 11 - 14
        
        # [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] - workers availability
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0] - required job time by employer
        
        # [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0] - result of subtracting
        
        self.worker_name = worker_name
        self.worker_id = worker_id
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
        self.matched_employers = []
        # self.pay_range_start = 0;
        self.payrate = payrate

        
        #class methods if needed here
        def nameToString(self):
            return worker_name

        #pass avoids empty object error          
        pass
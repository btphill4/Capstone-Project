# Class: Tenant
# Holds data values for Tenant DB

class Tenant:
    #in order based on schema.txt
    def __init__(self, appid, full_name, phone_number, email, age,
        what_do_you_do, city, preferred_neighborhood, max_house_mates,
        rent_range_start, rent_range_end, age_range, lease_or_rent,
        lease_length, has_children, children_ages, live_with_children,
        personal_pets_bool, personal_pets_text, live_with_pets_bool,
        live_with_pets_text, move_in_date, q18_1, q18_2, q18_3, q18_4, 
        environment_type, q20_1, q20_2, q20_3, q20_4, q20_5, q21_1, 
        q21_2, q21_3, q21_4, q21_5, q21_6, q22_1, q22_2, q22_3, q22_4,
        q22_5, privacy_needs, q24_1, q24_2, q24_3, q24_4, q24_5, q24_6,
        q24_7, future_events, q26_1, q26_2, q26_3, q26_4, q26_5, q26_6,
        q26_7, hobbies_text, additional_info, matchPercent):

        self.appid = appid
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.age = age
        self.what_do_you_do = what_do_you_do
        self.city = city
        self.preferred_neighborhood = preferred_neighborhood
        self.max_house_mates = max_house_mates
        self.rent_range_start = rent_range_start
        self.rent_range_end = rent_range_end
        self.age_range = age_range
        self.lease_or_rent = lease_or_rent
        self.lease_length = lease_length
        self.has_children = has_children
        self.children_ages = children_ages
        self.live_with_children = live_with_children
        self.personal_pets_bool = personal_pets_bool
        self.personal_pets_text = personal_pets_text
        self.live_with_pets_bool = live_with_pets_bool
        self.live_with_pets_text = live_with_pets_text
        self.move_in_date = move_in_date
        self.q18_1 = q18_1
        self.q18_2 = q18_2
        self.q18_3 = q18_3
        self.q18_4 = q18_4
        self.environment_type = environment_type
        self.q20_1 = q20_1
        self.q20_2 = q20_2
        self.q20_3 = q20_3
        self.q20_4 = q20_4
        self.q20_5 = q20_5
        self.q21_1 = q21_1
        self.q21_2 = q21_2
        self.q21_3 = q21_3
        self.q21_4 = q21_4
        self.q21_5 = q21_5
        self.q21_6 = q21_6
        self.q22_1 = q22_1
        self.q22_2 = q22_2
        self.q22_3 = q22_3
        self.q22_4 = q22_4
        self.q22_5 = q22_5
        self.privacy_needs = privacy_needs
        self.q24_1 = q24_1
        self.q24_2 = q24_2
        self.q24_3 = q24_3
        self.q24_4 = q24_4
        self.q24_5 = q24_5
        self.q24_6 = q24_6
        self.q24_7 = q24_7
        self.future_events = future_events
        self.q26_1 = q26_1
        self.q26_2 = q26_2
        self.q26_3 = q26_3
        self.q26_4 = q26_4
        self.q26_5 = q26_5
        self.q26_6 = q26_6
        self.q26_7 = q26_7
        self.hobbies_text = hobbies_text
        self.additional_info = additional_info
        self.matchPercent = matchPercent

        #class methods if needed here

        def get_appid(self):
            print("appplication ID: " + self.appid)
        
        def get_MatchPercent(self):
            print("matchPercent:  ", matchPercent)
        #pass avoids empty object error          
        pass
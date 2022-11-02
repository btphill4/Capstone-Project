# Class: HomeOwner2
# Holds data values for HomeOwner DB

class HomeOwner2:
    #in order based on schema.txt
    def __init__(self, row, fields):
        for field in fields:
            setattr(self, field, getattr(row,field))


        #class methods if needed here

        def get_appid(self):
            print("appplication ID: " + self.appid)
            
        #pass avoids empty object error          
        pass
from geopy import distance
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD
# to call the openmap/google apis
# import requests
# import json
# import datetime
# import math
# import itertools
# for travelling salesman problem
#import mlrose

# Required for distance calculations
geolocater = Nominatim(user_agent="http")

print("==========================================================================")
print("Loading addresses and printing: ")
print("==========================================================================\n")


# general asu address
location1 = geolocater.geocode("1151 S Forest Ave Tempe")

# Cardinals Stadium address
location2 = geolocater.geocode("1 Cardinals Dr")

# Print addresses
print("ASU address: \n" + location1.address)
# print("Longitude and latitude: ")
asu = (location1.latitude, location1.longitude)
print(asu)

print()

print("Cardinal Stadium Address: \n" + location2.address)
# print("Longitude and latitude: ")
print((location2.latitude, location2.longitude))
cardinals = (33.529115, -112.264563)

print()

# Distance calculation
print("==========================================================================")
print("Distance from ASU to Cardinal stadium calculations: ")
print("==========================================================================\n")

print("Distance in miles: " + str("{:.2f}".format(GD((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles)) + " miles")
# print(GD((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles)
print()

print("Distance in kilometers: " + str("{:.2f}".format(GD((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km)) + " km")
# print(GD((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km)
print("\n==========================================================================")

# print from GD calls -> for referencing in project -> temp variables 
asu_cards_MILES = GD((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles
asu_cards_KM = GD((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km

# print("Distance in miles: " + str("{:.2f}".format(asu_cards_MILES)) + " miles")
# print("Distance in kilometers: " + str("{:.2f}".format(asu_cards_KM)) + " km")

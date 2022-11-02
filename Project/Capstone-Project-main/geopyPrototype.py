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


# employers/employess matching software

# Required for distance calculations
geolocater = Nominatim(user_agent="http")

print("==========================================================================")
print("Loading addresses and printing: ")
print("==========================================================================\n")


# general asu address
asu_Location = geolocater.geocode("1151 S Forest Ave Tempe")

# Cardinals Stadium address
cards_Location = geolocater.geocode("1 Cardinals Dr")

# Suns statdium address
suns_Location = geolocater.geocode("201 E Jefferson St, Phoenix, AZ 85004")

# 

# Print addresses
print("ASU address: \n" + asu_Location.address)
# print("Longitude and latitude: ")
asu = (asu_Location.latitude, asu_Location.longitude)
print(asu)

print()

print("Cardinal Stadium Address: \n" + cards_Location.address)
# print("Longitude and latitude: ")
print((cards_Location.latitude, cards_Location.longitude))
cardinals = (33.529115, -112.264563)

print()

print("Suns address: \n" + asu_Location.address)
# print("Longitude and latitude: ")
suns = (suns_Location.latitude, suns_Location.longitude)
print(suns)

print()

# Distance calculation
print("==========================================================================")
print("Distance from ASU to Cardinal stadium calculations: ")
print("==========================================================================\n")

print("Distance in miles: " + str("{:.2f}".format(GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).miles)) + " miles")
# print(GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).miles)
print()

print("Distance in kilometers: " + str("{:.2f}".format(GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).km)) + " km")
# print(GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).km)
print("\n==========================================================================")

print("\n==========================================================================")
print("Distance from ASU to Suns stadium calculations: ")
print("==========================================================================\n")

print("Distance in miles: " + str("{:.2f}".format(GD((asu_Location.latitude, asu_Location.longitude), (suns_Location.latitude, suns_Location.longitude)).miles)) + " miles")
# print(GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).miles)
print()

print("Distance in kilometers: " + str("{:.2f}".format(GD((asu_Location.latitude, asu_Location.longitude), (suns_Location.latitude, suns_Location.longitude)).km)) + " km")
# print(GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).km)
print("\n==========================================================================\n")



# print from GD calls -> for referencing in project -> temp variables 
asu_cards_MILES = GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).miles
asu_cards_KM = GD((asu_Location.latitude, asu_Location.longitude), (cards_Location.latitude, cards_Location.longitude)).km

# print("Distance in miles: " + str("{:.2f}".format(asu_cards_MILES)) + " miles")
# print("Distance in kilometers: " + str("{:.2f}".format(asu_cards_KM)) + " km")


def shortest_distance(location1, location2, location3):
    # d1 = distance from location1 -> location2 -> location3
    d1_1 = GD((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles
    d1_2 = GD((location2.latitude, location2.longitude), (location3.latitude, location3.longitude)).miles
    d1 = d1_1 + d1_2
    print("D1 distance in miles: ") 
    print(d1)
    print()
    # print(str("{::2f}".format(d1)))

    # d2 = location2 -> location1 -> location3
    d2_1 = GD((location2.latitude, location2.longitude), (location1.latitude, location1.longitude)).miles
    d2_2 = GD((location1.latitude, location1.longitude), (location3.latitude, location3.longitude)).miles
    d2 = d2_1 + d2_2
    # print("D2 distance in miles: " + d2)
    print("D2 distance in miles: ") 
    print(d2)
    print()

    # d3 = location3 -> location2 -> location1
    d3_1 = GD((location3.latitude, location3.longitude), (location2.latitude, location2.longitude)).miles
    d3_2 = GD((location2.latitude, location2.longitude), (location1.latitude, location1.longitude)).miles
    d3 = d3_1 + d3_2
    print("D3 distance in miles: ") 
    print(d3)
    print()

    # print("D3 distance in miles: " + d3)
    # d4 = location1 -> location3 -> location2 
    d4_1 = GD((location1.latitude, location1.longitude), (location3.latitude, location3.longitude)).miles
    d4_2 = GD((location3.latitude, location3.longitude), (location2.latitude, location2.longitude)).miles
    d4 = d4_1 + d4_2
    print("D4 distance in miles: ") 
    print(d4)
    print()

    # find min distance 
    distance_arr = [d1, d2, d3, d4]
    # print("Shortest Distance: " + str("{::2f}".format(min(distance_arr))) + " miles")
    print("Shortest Distance: " + str(min(distance_arr)) + " miles")


# shortest distance call
shortest_distance(asu_Location, cards_Location, suns_Location)


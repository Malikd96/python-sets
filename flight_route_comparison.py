#Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes 
# of your airline with a competitor. You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out:

#1. Destinations that both airlines fly to.

#2. Destinations unique to your airline.

#3. Whether there are any destinations that neither airline shares.

#Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

both_airlines = our_routes.union(competitor_routes)
print(both_airlines)

mutual_airline = our_routes.difference(competitor_routes)
print(mutual_airline)

airlines_not_mutual = our_routes.symmetric_difference(competitor_routes)
print(airlines_not_mutual)
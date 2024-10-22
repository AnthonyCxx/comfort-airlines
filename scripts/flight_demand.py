# Team: Foobar
# Authors: Anthony Cox
# Date: 1/31/2024
# Script: flight_demand.py
# Depends on: "data/airports.csv", "flight_distance.csv"
# Input: 
#   A list of the airport, their details, and the distances between them
# Output: 
#   A list of the flights between each airport (including source and destination airports)
#   and the number of passengers that want to take that flight each day. The number of passengers
#   accounts for the 2% market share and 0.5% of the population that wants to fly each day
import csv
from pprint import pprint

# Indices of values in airports.csv
RANK = 0
NAME = 1
IATA = 2
CITY = 3
STATE = 4
METRO_AREA = 5
METRO_POPULATION = 6
LATITUDE = 7
LONGITUDE = 8

# Indices of values in flight_distance.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2

# Formula constants
DAILY_DEMAND = 0.005
MARKET_SHARE = 0.02

# File-reading constants
FILE_START = 0

with open ("data/airports.csv", "r") as airport_data, open("data/flight_weighted_distances.csv", "r") as flight_data:
    # 1. Generete a mapping of airports to their metro populations
    reader = csv.reader(airport_data, delimiter=',')
    header = next(reader)
    metro_population = dict(
        (airport[NAME],int(airport[METRO_POPULATION])) for airport in reader
    )
    
    # 2. Generate a mapping of each source airport to the list of its destination airports
    reader = csv.reader(flight_data, delimiter=',')
    header = next(reader)
    flights = dict(
        (airport_name,[]) for airport_name in metro_population
    )
    
    for flight in reader:
        flights[flight[SOURCE_AIRPORT]].append(flight[DESTINATION_AIRPORT])
    
    # 3. Reset CSV reader for flight data
    flight_data.seek(FILE_START)
    header = next(reader)
    
    # 4. Calculate the demand for each given flight based on the metro population of the destination vs the metro population of all airports serviced by the source airport
    with open("data/flight_demand.csv", "w") as outfile:
        # 4A. Write Headers
        outfile.write("source airport,destination airport,company flight demand\n")
        
        # 4B. Write body
        for flight in reader:
            percent_flight_demand = metro_population[flight[DESTINATION_AIRPORT]] / sum([metro_population[destination_airport] for destination_airport in flights[flight[SOURCE_AIRPORT]]])
            num_passengers = round(metro_population[flight[SOURCE_AIRPORT]] * DAILY_DEMAND * MARKET_SHARE * percent_flight_demand)
            
            #print(f"\n\n{flight[SOURCE_AIRPORT]} => {flight[DESTINATION_AIRPORT]}")
            #pprint(f"Airports: {', '.join(map(lambda tuple: f"({tuple[0]},{tuple[1]})", [(destination_airport,metro_population[destination_airport]) for destination_airport in flights[flight[SOURCE_AIRPORT]]]))}")
            #print(f"Percent Flight Demand: {metro_population[flight[DESTINATION_AIRPORT]]} / {sum([metro_population[destination_airport] for destination_airport in flights[flight[SOURCE_AIRPORT]]])} = {percent_flight_demand}")
            #print(f"Number of Passengers: round({metro_population[flight[SOURCE_AIRPORT]]} * {DAILY_DEMAND} * {MARKET_SHARE} * {percent_flight_demand}) = {num_passengers}")
            
            outfile.write(f"{flight[SOURCE_AIRPORT]},{flight[DESTINATION_AIRPORT]},{num_passengers}\n")
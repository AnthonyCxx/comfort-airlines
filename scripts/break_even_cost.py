import csv
# NOTE: does not account for (max) fuel capacity, purely monetary calc

# Indices of values in flight_demand.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2
DEMAND = 3

# linear_aircraft_specs.csv
# aircraft,passenger_capacity,cruise_speed (km/h),max_fuel_capacity (gallons),max_range (km),mpg (mpg)
AIRCRAFT = 0
CAPACITY = 1
SPEED = 2
MAX_FUEL = 3
MAX_RANGE = 4
MPG = 5


# Formula constants
takeoff_fee = 2000
landing_fee = 2000
gas = 6.19              # gallons
KMtoM = 0.621371        # converts to miles
percent_full = 0.3

# File-reading constants
FILE_START = 0


with open ("data/flights.csv", "r") as flight_data, open ("data/linear_aircraft_specs.csv", "r") as aircraft_spec_data, open("data/cost_per_flight.csv", "w") as outfile:
    #Generate break even costs
    flight_reader = csv.reader(flight_data, delimiter=',')
    aircraft_spec_reader = csv.reader(aircraft_spec_data, delimiter=',')
    
    #write header of outfile outside loop
    outfile.write("source airport,destination airport,airplane type,total Cost,break even cost per ticket\n")

    #skip header row
    _ = next(flight_reader)
    _ = next(aircraft_spec_reader)
    
    for row_flight in flight_reader:  # Iterate over the reader object, not the file object
        source_airport = row_flight[SOURCE_AIRPORT]
        destination_airport = row_flight[DESTINATION_AIRPORT]
        demand = float(row_flight[DEMAND])
        distance_km = float(row_flight[DISTANCE_KM])

        for row_aircraft_spec in aircraft_spec_reader: 
            aircraft_name = row_aircraft_spec[AIRCRAFT]
            capacity = int(row_aircraft_spec[CAPACITY])
            mpg = float(row_aircraft_spec[MPG])

            # Calculate total cost
            total_cost = (distance_km * KMtoM / mpg ) * gas + takeoff_fee + landing_fee
            
            #calculate break even at 30% capacity
            break_even_cost_per_ticket = total_cost / (capacity * percent_full)

            #4. Write body
            outfile.write(f"{source_airport},{destination_airport},{aircraft_name},{total_cost},{break_even_cost_per_ticket}\n")
            
            # Print information
            #print(f"Source: {source_airport}, Destination: {destination_airport}")
            #print(f"Demand: {demand}, Distance: {distance_km} km")
            #print(f"Total Cost: {total_cost}")
            #print(f"Break Even Cost Per Ticket: {break_even_cost_per_ticket}")
            #print(f"Using the model: {aircraft_name} aircraft")
            #print()
        
        aircraft_spec_data.seek(FILE_START)
        _ = next(aircraft_spec_reader)

# NOTE: does not account for (max) fuel capacity, purely monetary calc
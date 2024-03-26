# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Dylan Hudson, Zach Christopher
# Date: 3/25/2024
#
# Description:
#   This module defines and implements the model class `Scheduler`.

import structlog
import csv
from models.flight import Flight
from models.aircraft import Aircraft
from models.route import Route
from models.passenger import Passenger

class Scheduler:
    """Model class. A generic representation of a scheduler."""
    
    # Static class variables
    flight_uuid: int = 0
    flights: list[Flight] = []
    logger = structlog.get_logger()
    
    @staticmethod
    def next_flight_number() -> int:
        """Internal Scheduler static method. Generates a next unique flight number"""
        # A function to increment the UUID and return the next UUID
        flight_number = Scheduler.flight_uuid
        Scheduler.flight_uuid += 1        
        return flight_number
    
    @staticmethod
    def schedule_flight(simulation_time: int, aircraft: Aircraft, all_routes: list[Route], all_passengers: list[Passenger]) -> None:
        """
        The function should take the following parameters: the simulation time, the aircraft to be scheduled, 
        the list of ALL routes, and the list of ALL passengers. Then, filter the list of all routes to find the 
        routes compatible with the aircraft. For a route to be "compatible", the following criteria must be met:
        (Write a filter() for each condition and then casting the final filter object to a list).
        """
        
        #   1) The source airport of the route must be the current location of the aircraft
        
        #   2) The aircraft type of the route must be the type of the aircraft
        
        #   3) The fuel requirement of the route must be less than or equal to the fuel capacity of the aircraft.
        
        #   4) There must be at least 1 passenger at the aircraft's current location that wants to take that route
        
        #   5) If the aircraft needs maintenance, the destination airport of the route must be a hub
        
        # Selecting the Route:
        #   You should select the route with the maximum net profit. You can do this easily by using the built-in max() function and specifying the key is the net profit.
         
        #   Then, refuel if needed (set the status of the aircraft to boarding with or without refueling).
        
        #   Set the flight object of the aircraft to the current flight, append the flight to the list of all scheduled flights,
        
        pass
    
    @staticmethod
    def output_flight_entries() -> None:
        """A method to write the list of flights entries to the file simulation-output/flights.csv in CSV format"""
        with open("simulation-output/flights.csv", "w") as outfile:
            # Write header
            outfile.write("flight number,scheduled time,aircraft tail number,route??,passengers??,expected departure time,expected arrival time,actual departure time,actual arrival time\n")
            
            # For every Flight in flights, print the flight info
            for flight in Scheduler.flights:
                # Info from each flight to print
                fl_num = str(flight.flight_number)
                s_time = str(flight.scheduled_time)
                a_t_num = flight.aircraft.tail_number
                r_uuid = "route_uuid??"         # flight.route
                p_uuid = "passengers_uuid??"    # flight.passengers
                e_d_time = str(flight.expected_departure_time)
                e_a_time = str(flight.expected_arrival_time)
                a_d_time = str(flight.actual_departure_time)
                a_a_time = str(flight.actual_arrival_time)
                
                # Output individual flight info
                outfile.write(f"{fl_num},{s_time},{a_t_num},{r_uuid},{p_uuid},{e_d_time},{e_a_time},{a_d_time},{a_a_time}\n")

        

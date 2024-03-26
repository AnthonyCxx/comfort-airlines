# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Dylan Hudson, Zach Christopher
# Date: 3/25/2024
#
# Description:
#   This module tests the model class `Scheduler`.

# Import necessary libraries and modules
import pytest
import structlog
from decimal import Decimal
from queue import Queue
from models.airport import Airport
from models.aircraft import Aircraft, AircraftType, AircraftStatus, AircraftFactory
from models.flight import Flight
from models.route import Route
from models.passenger import Passenger
from models.scheduler import Scheduler

# ////////////////////////////////////////////////////// PYTEST FIXTURES //////////////////////////////////////////////////////
# Setup a sample Aircraft
@pytest.fixture()
def sample_aircraft() -> Aircraft:
    aircraft1: Aircraft = AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 6300)
    return aircraft1

# Setup a sample Airports
@pytest.fixture()
def airport1() -> Airport:
    airport = Airport(
        "John F. Kennedy International Airport", "JFK", "New York City", "New York", 18713220, False, 5, 40.6413, 
        -73.7781, 2.50, Decimal('1000.00'), Decimal('500.00'), Queue()
    )
    return airport
@pytest.fixture()
def airport2() -> Airport:
    airport = Airport(
        "Dallas/Fort Worth International Airport", "DFW", "Dallas/Fort Worth", "Texas", 7233323, True, 11, 32.8998, 
        -97.0403, 2.65, Decimal('1100.00'), Decimal('550.00'), Queue()
    )
    return airport
    
# Setup a sample Route
@pytest.fixture()
def sample_route(airport1, airport2) -> Route:
    route = Route(AircraftType.BOEING_737_600, airport1, airport2, 2215.6694092085722, 35, 220, 2503.7227066032797)
    return route
    
# Setup a sample Passengers
@pytest.fixture()
def sample_passengers(airport1, airport2) -> list[Passenger]:
    passengers = [Passenger(airport1, airport2), Passenger(airport1, airport2), Passenger(airport1, airport2), 
                  Passenger(airport1, airport2), Passenger(airport1, airport2), Passenger(airport1, airport2)]
    return passengers

# Setup a sample test_flights
@pytest.fixture()
def sample_route_list(sample_route) -> list[Route]:
    routes: list[Route] = [sample_route, sample_route, sample_route, sample_route, sample_route, sample_route]
    return routes
# ////////////////////////////////////////////////////// END PYTEST FIXTURES //////////////////////////////////////////////////////


# Define the test function to test the instantiation of Scheduler
def test_scheduler_initialization() -> None:
    # Testing Variables
    empty_flights: list[Flight] = []
    test_logger = structlog.get_logger()
    
    assert Scheduler.flight_uuid == 0
    assert Scheduler.flights == empty_flights
    assert type(Scheduler.logger) == type(test_logger)

# Function to test the schedule_flight() function
def test_schedule_flight(sample_aircraft, sample_route_list, sample_passengers) -> None:
    # Scheduler.schedule_flight(simulation_time, aircraft, all_routes, all_passengers)
    pass

# Function to test the output_flight_entries() function
def test_output_flight_entries() -> None:
    # Scheduler.output_flight_entries()
    pass
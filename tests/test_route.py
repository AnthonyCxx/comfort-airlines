
# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Corey Lawrence, Zach Christopher
# Date: 3/21/2024
#
# Description:
#   This module defines and implements tests for the `Route` class, which provides an object associated with 
#   a specific source, destination, and aircraft type.

import pytest
from models.route import Route
from models.airport import Airport
from models.aircraft import AircraftType
from decimal import Decimal
from queue import Queue

@pytest.fixture
def sample_aircraft_type():
    """Fixture providing a sample aircraft type."""
    return AircraftType.BOEING_737_600

@pytest.fixture
def sample_source_airport():
    """Fixture providing a sample source airport."""
    return Airport("John F. Kennedy International Airport", "JFK", "New York City", "New York", 18713220, 
                   False, 5, 40.6413, -73.7781, 2.50, Decimal('1000.00'), Decimal('500.00'), Queue())

@pytest.fixture
def sample_destination_airport():
    """Fixture providing a sample destination airport."""
    return Airport("Los Angeles International Airport", "LAX", "Los Angeles", "California", 20116801, 
                   False, 8, 33.9416, -118.4085, 8.00, Decimal('2000.00'), Decimal('1000.00'), Queue())

def test_route_init(sample_aircraft_type, sample_source_airport, sample_destination_airport):
    """Route.__init__() method test.
    
    Asserts that the Route class constructor initializes attributes correctly.
    """
    distance = 2500.0
    daily_demand = 100
    estimated_flight_time = 180
    fuel_requirement = 750.0

    route = Route(sample_aircraft_type, sample_source_airport, sample_destination_airport, distance, daily_demand, estimated_flight_time, fuel_requirement)

    assert route.aircraft_type == sample_aircraft_type
    assert route.source_airport == sample_source_airport
    assert route.destination_airport == sample_destination_airport
    assert route.distance == distance
    assert route.daily_demand == daily_demand
    assert route.estimated_flight_time == estimated_flight_time
    assert route.fuel_requirement == fuel_requirement

def test_route_init_invalid_input(sample_source_airport, sample_destination_airport):
    """Route.__init__() method test.
    
    Asserts that the Route class constructor raises appropriate errors for invalid input.
    """
    invalid_aircraft_type = "Invalid Aircraft Type"
    invalid_airport = "Invalid Airport"
    invalid_distance = -1000.0
    invalid_daily_demand = -1
    invalid_estimated_flight_time = -180
    invalid_fuel_requirement = -750.0

    with pytest.raises(TypeError):
        _ = Route(invalid_aircraft_type, invalid_airport, invalid_airport, 2500.0, 100, 180, 750.0)

    with pytest.raises(TypeError):
        _ = Route(AircraftType.BOEING_737_600, invalid_airport, invalid_airport, 2500.0, 100, 180, 750.0)

    with pytest.raises(TypeError):
        _ = Route(AircraftType.BOEING_737_600, sample_source_airport, invalid_airport, 2500.0, 100, 180, 750.0)

    with pytest.raises(ValueError):
        _ = Route(AircraftType.BOEING_737_600, sample_source_airport, sample_destination_airport, invalid_distance, 100, 180, 750.0)

    with pytest.raises(ValueError):
        _ = Route(AircraftType.BOEING_737_600, sample_source_airport, sample_destination_airport, 2500.0, invalid_daily_demand, 180, 750.0)

    with pytest.raises(ValueError):
        _ = Route(AircraftType.BOEING_737_600, sample_source_airport, sample_destination_airport, 2500.0, 100, invalid_estimated_flight_time, 750.0)

    with pytest.raises(ValueError):
        _ = Route(AircraftType.BOEING_737_600, sample_source_airport, sample_destination_airport, 2500.0, 100, 180, invalid_fuel_requirement)

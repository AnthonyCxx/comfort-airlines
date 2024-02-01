from sqlalchemy import (MetaData, Table, Column, ForeignKey)
from sqlalchemy.types import (Integer, Date, Time, Float, Boolean, DECIMAL, VARCHAR)
from eralchemy2 import render_er


metadata = MetaData()


# TEMPLATE
# create your own model ....
#users = Table('users', metadata,
#    Column('user_id', Integer(), primary_key=True),
#    Column('username', String(15), nullable=False, unique=True),
#)    
#orders = Table('orders', metadata,
#    Column('order_id', Integer()),
#    Column('user_id', ForeignKey('users.user_id')),
#)
# ....


# ACTUAL
Passenger = Table('passenger', metadata,
    Column('passenger_id', Integer, primary_key=True),
    Column('name', VARCHAR, nullable=False)
)

PassengerFlights = Table('passenger_flights', metadata,
    Column('passenger_flight_id', Integer, primary_key=True),
    Column('passenger_id', Integer, ForeignKey('passenger.passenger_id'), nullable=False),
    Column('flight_number', Integer, ForeignKey('flight.flight_number'), nullable=False)
)

Flight = Table('flight', metadata,
    Column('flight_number', Integer, primary_key=True),
    Column('date', Date, nullable=False),
    Column('source_id', Integer, ForeignKey('airport.airport_id'), unique=True, nullable=False),
    Column('layover_id', Integer, ForeignKey('airport.airport_id'), unique=True, nullable=False),
    Column('destination_id', Integer, ForeignKey('airport.airport_id'), unique=True, nullable=False),
    Column('num_passengers', Integer, nullable=False),
    Column('depart_time', Time, nullable=False),
    Column('arrival_time', Time, nullable=False),
    Column('actual_depart_time', Time, nullable=False),
    Column('actual_arrival_time', Time, nullable=False),
    Column('tail_number', Integer, ForeignKey('aircraft.tail_number'), unique=True, nullable=False)
)

Airport = Table('airport', metadata,
    Column('airport_id', Integer, primary_key=True),
    Column('flight_number', Integer, ForeignKey('flight.flight_number'), unique=True, nullable=False),
    Column('gate_used', Integer, nullable=False),
    Column('takeoff_cost', DECIMAL, nullable=False),
    Column('name', VARCHAR, nullable=False),
    Column('lata_code', VARCHAR, nullable=False),
    Column('city', VARCHAR, nullable=False),
    Column('state', VARCHAR, nullable=False),
    Column('metro_population', Integer, nullable=False),
    Column('paris_acceptable', Boolean, nullable=False),
    Column('hub', Boolean, nullable=False),
    Column('num_gates', Integer, nullable=False),
    Column('latitude', Float, nullable=False),
    Column('longitude', Float, nullable=False),
    Column('landing_cost', DECIMAL, nullable=False),
    Column('fuel_price', DECIMAL, nullable=False)
)

Aircraft = Table('aircraft', metadata,
    Column('tail_number', Integer, primary_key=True),
    Column('craft_type', Integer, ForeignKey('aircraft_type.craft_type'), nullable=False),
    Column('at_hub', Boolean, nullable=False),
    Column('maintenance', Boolean, nullable=False),
    Column('maintenance_timer', Time, nullable=False),
    Column('flight_hours', Time, nullable=False),
    Column('in_flight', Boolean, nullable=False)
)

AircraftType = Table('aircraft_type', metadata,
    Column('craft_type', Integer, primary_key=True),
    Column('craft_make', VARCHAR, nullable=False),
    Column('craft_model', VARCHAR, nullable=False),
    Column('passenger_capacity', Integer, nullable=False),
    Column('max_speed', Integer, nullable=False),
    Column('max_fuel_capacity', Integer, nullable=False),
    Column('max_range', Integer, nullable=False),
    Column('max_altitude', Integer, nullable=False)
)


# Show ER model from here
render_er(metadata, 'thing.png')



# TEMPLATE
# User (user_id PK, username, email)
# Product (product_id PK, name, price, user_id FK)

# ACTUAL
# Passenger (passengerID PK, name)
# PassengerFlights (passFlightID PK, flightNumber FK, passengerID FK)
# Flight (flightNumber PK, date, numPassengers, departureTime, arrivalTime, 
#         actualDepartureTime, actualArrivalTime, sourceID FK, layoverID FK, 
#         destinationID FK, tailNumber FK)
# Airport (airportID PK, gateUsed, takeoffCost, name, lataCode, city, state, 
#          metroPop, ParisAccept, hub, numGates, lat, long, landCost, fuelPrice,
#          flightNumber FK)
# Aircraft (tailNum PK, atHub, maintenance, maintenanceTimer, flightHours, 
#           inFlight, type FK)
# AircraftType (type PK, make, model, passengerCapacity, maxSpeed,
#               maxFeulCapacity, maxRange, maxAlt)


from sqlalchemy import create_engine, Column, ForeignKey
#                 app object ^
from sqlalchemy.types import (Integer, Boolean, Float, Time, Date, DECIMAL, VARCHAR)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, sessionmaker


# define base class for table class definitions
Base = declarative_base()


# TEMPLATE
#
#class User(Base):
#    __tablename__ = 'users'
#    id = Column(Integer, primary_key=True)
#    username = Column(String)
#
#class Post(Base):
#    __tablename__ = 'posts'
#    id = Column(Integer, primary_key=True)
#    title = Column(String)
#    content = Column(String)
#    user_id = Column(Integer, ForeignKey('users.id'))
#    user = relationship('User', back_populates='posts')


# ACTUAL -- create tables
class Passenger(Base):
    __tablename__ = 'passenger'
    # PRIMARY KEY
    passenger_ID = Column(Integer, primary_key=True)
    
    # DATA
    name = Column(VARCHAR, nullable=False)
    
    # RELATION
    passenger_flights = relationship('PassengerFlights', back_populates='Passenger')


class PassengerFlights(Base):
    __tablename__ = 'passenger_flights'
    # PRIMARY KEY
    pass_flight_ID = Column(Integer, primary_key=True)
    
    # DATA
    passenger_ID = Column(Integer, ForeignKey('passenger.passenger_ID'), nullable=False)
    flight_number = Column(Integer, ForeignKey('flight.flight_number'), nullable=False)
    
    # RELATION
    flight = relationship('Flight', back_populates='PassengerFlights')
    passenger = relationship('Passenger', back_populates='PassengerFlights')


class Flight(Base):
    __tablename__ = 'flight'
    # PRIMARY KEY
    flight_number = Column(Integer, primary_key=True)
    
    # DATA
    date = Column(Date, nullable=False)
    source_ID = Column(Integer, ForeignKey('airport.airport_ID'), unique=True, nullable=False)
    layover_ID = Column(Integer, ForeignKey('airport.airport_ID'), unique=True, nullable=False)
    destination_ID = Column(Integer, ForeignKey('airport.airport_ID'), unique=True, nullable=False)
    num_passengers = Column(Integer, nullable=False)
    depart_time = Column(Time, nullable=False)
    arrival_time = Column(Time, nullable=False)
    actual_depart_time = Column(Time, nullable=False)
    actual_arrival_time = Column(Time, nullable=False)
    tail_number = Column(Integer, ForeignKey('aircraft.tail_number'), unique=True, nullable=False)
    
    # RELATION
    airport = relationship('Airport', back_populates='Flight')
    aircraft = relationship('Aircraft', back_populates='Flight')
    passenger_flights = relationship('PassengerFlights', back_populates='Flight')


class Airport(Base):
    __tablename__ = 'airport'
    # PRIMARY KEY
    airport_ID = Column(Integer, primary_key=True)
    
    # DATA
    flight_number = Column(Integer, ForeignKey('flight.flight_number'), nullable=False)
    gate_used = Column(Integer, nullable=False)
    takeoff_cost = Column(DECIMAL, nullable=False)
    name = Column(VARCHAR, nullable=False)
    lata_code = Column(VARCHAR, nullable=False)
    city = Column(VARCHAR, nullable=False)
    state = Column(VARCHAR, nullable=False)
    metro_population = Column(Integer, nullable=False)
    paris_acceptable = Column(Boolean, nullable=False)
    hub = Column(Boolean, nullable=False)
    num_gates = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    landing_cost = Column(DECIMAL, nullable=False)
    fuel_price = Column(DECIMAL, nullable=False)
    
    # RELATION
    flight = relationship('Flight', back_populates='Airport')


class Aircraft(Base):
    __tablename__ = 'aircraft'
    # PRIMARY KEY
    tail_number = Column(Integer, primary_key=True)

    # DATA
    craft_type = Column(Integer, ForeignKey('aircraft_type.craft_type'), nullable=False)
    at_hub = Column(Boolean, nullable=False)
    maintenance = Column(Boolean, nullable=False)
    maintenance_timer = Column(Time, nullable=False)
    flight_hours = Column(Time, nullable=False)
    in_flight = Column(Boolean, nullable=False)

    # RELATION
    aircraft_type = relationship('AircraftType', back_populates='Aircraft')


class AircraftType(Base):
    __tablename__ = 'aircraft_type'
    # PRIMARY KEY
    craft_type = Column(Integer, primary_key=True)

    # DATA
    craft_make = Column(VARCHAR, nullable=False)
    craft_model = Column(VARCHAR, nullable=False)
    passenger_capacity = Column(Integer, nullable=False)
    max_speed = Column(Integer, nullable=False)
    max_fuel_capacity = Column(Integer, nullable=False)
    max_range = Column(Integer, nullable=False)
    max_altitude = Column(Integer, nullable=False)

    # RELATION
    aircraft = relationship('Aircraft', back_populates='AircraftType')


# set up engine based on db location
# manages the connection to the db
database_url = 'mariadb+mariadbconnector://root:toor@172.17.0.1:3306/comfort_airlines_db'
engine = create_engine(database_url, echo=True)

# USE THIS ENGINE FOR A .db FILE
#database_uri = 'sqlite:///comfort_airlines.db'
#engine = create_engine(database_uri)


# create tables based on definitions above, define which engine to use
Base.metadata.create_all(bind=engine)


# declare a new session to interact with db, define which engine to use
Session = sessionmaker(bind=engine)
# create session
session = Session()


# commit changes
session.commit()


# close session
session.close()


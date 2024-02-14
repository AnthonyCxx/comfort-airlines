
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
from sqlalchemy.types import (Integer, Time, Date, VARCHAR)
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, relationship, Session, sessionmaker


# define base class for table class definitions
Base = declarative_base()
#metadata = MetaData()


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
    name = Column(VARCHAR(255), nullable=False)
    
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
    flight_in_number = Column(Integer, ForeignKey('flight.flight_number'), unique=True, nullable=False)
    flight_out_number = Column(Integer, ForeignKey('flight.flight_number'), unique=True, nullable=False)
    
    # RELATION
    flight = relationship('Flight', back_populates='Airport')


class Aircraft(Base):
    __tablename__ = 'aircraft'
    # PRIMARY KEY
    tail_number = Column(Integer, primary_key=True)

    # DATA
    craft_type = Column(Integer, nullable=False)


# set up engine based on db location
# manages the connection to the db
DATABASE_URL = 'mariadb+mariadbconnector://root:toor@172.19.0.2:3306/comfort-airlines-db'
engine = create_engine(DATABASE_URL, echo=True)


# USE THIS ENGINE FOR A .db FILE
#DATABASE_URI = 'sqlite:///comfort_airlines.db'
#engine = create_engine(DATABASE_URI)


# create tables based on definitions above, define which engine to use
Base.metadata.create_all(bind=engine)


# declare a new session to interact with db, define which engine to use
session = Session(engine)
Session = sessionmaker(bind=engine)
# create session
session = Session()


# commit changes
session.commit()


# close session
session.close()
#connection.close()


# REMEMBER TO
# - docker compose down
# - check ip (ip a)
# - update ip for each run after build
#
# - delete tables after done
#
# TO DO
# - input data for test
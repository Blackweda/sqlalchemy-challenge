# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite://Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurements = Base.classes.measurement
Stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

start = ""
end = ""


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to my Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/{start}"
        f"/api/v1.0/{start}/{end}"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():    

    session = Session(engine)
    
    one_year_span = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    one_year_history = session.query(Measurements.date, Measurements.prcp).filter(Measurements.date >= one_year_span).all()

    session.close()

    year_measurements = []
    for date, prcp in one_year_history:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["precipitation"] = prcp
        year_measurements.append(messenger_dict)

    return jsonify(year_measurements)

@app.route("/api/v1.0/stations")
def station_list():

    session = Session(engine)

    list = session.query(Stations.station, Stations.name).all()
    list_of_stations = []
    for station, name in list:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        list_of_stations.append(station_dict)

    session.close()

    return jsonify(list_of_stations)

@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)

    station_counter = session.query(Measurements.station, func.count(Measurements.station)).group_by(Measurements.station).order_by(func.count(Measurements.station).desc()).all()
    most_active = station_counter[0][0]
    most_active_station = session.query(Measurements.date, Measurements.tobs).filter(Measurements.station == most_active)
    
    list_of_temperatures = []
    for date, tobs in list_of_temperatures:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["temperature"] = tobs
        list_of_temperatures.append(temp_dict)

    session.close()

    return jsonify(list_of_temperatures)

@app.route(f"/api/v1.0/{start}")
def start_func():

    return ""

@app.route(f"/api/v1.0/{start}/{end}")
def start_end_func():

    return ""


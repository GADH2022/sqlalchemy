# dependencies

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
import datetime as dt

from flask import Flask,jsonify

# database connection setup
engine=create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect  database to a new model
Base=automap_base()
#Reflect the tables
Base.prepare(engine,reflect=True)

#saving References
Measurement=Base.classes.measurement
Stations=Base.classes.station

#Flask set up
app=Flask(__name__)

#Flask Routes
#1st route
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"

      #  f"/api/v1.0/start<br/>"
      #  f"/api/v1.0/<start>/<end><br/>"
    )
 #2nd  route
@app.route("/api/v1.0/precipitation")  
def precipitation(): 
    # Query dates and precipitation
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Creating a dictionary using 'date' as the key and 'prcp' as the value
    prcp_list = []

    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        prcp_list.append(prcp_dict) 

    session.close()

    # Return the list of dates and precipitation
    return jsonify(prcp_list)

#3rd route

@app.route("/api/v1.0/stations")
def stations():
    
    # Query all distinct stations
    session = Session(engine)
    results = session.query(Measurement.station).distinct().all()
    
    # Store results as a list
    stations_list = list(np.ravel(results))

    session.close()

    # Return a list of all distinct stations
    return jsonify(stations_list)


#4 th route
@app.route("/api/v1.0/tobs")
def tobs():
    
    # Query all dates
    session = Session(engine)
    dates = session.query(Measurement.date).all()
    
    # Extract and store the start and end dates of one year's data
    last_date = dates[-1][0]
    end_dt = dt.datetime.strptime(last_date, '%Y-%m-%d')
    end_dt = end_dt.date()
    start_dt = end_dt - dt.timedelta(days=365)
    
    # Query one year's worth of temperature observations
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date>=start_dt).\
        filter(Measurement.date<=end_dt).all()
    
    # Create a dictionary using 'date' as the key and 'tobs' as the value
    tobs_list = []

    for date, tobs in results:
        tobs_dict = {}
        tobs_dict[date] = tobs
        tobs_list.append(tobs_dict) 

    session.close()

    # Return the list of dates and temperature observations
    return jsonify(tobs_list)

#5,6 routes

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):


    session = Session(engine)
    statements = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
       
        results = session.query(*statements).\
            filter(Measurement.date >= start).all()

        session.close()

        temps = list(np.ravel(results))
        return jsonify(temps)

 

    results = session.query(*statements).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    session.close()

    t_list = list(np.ravel(results))
    return jsonify(t_list)   

         

if __name__ == "__main__":
    app.run(debug=True)



     


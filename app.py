# 1. import Flask, Python SQL toolkit and ORM
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, or_, and_


# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return ("Welcome to my 'Home' page!"
          f"Available Routes:<br/>"
          f"/api/v1.0/precipitation<br/>"
          f"/api/v1.0/stations<br/>"
          f"/api/v1.0/tobs<br/>"
          f"/api/v1.0/start_date/2011-05-01<br/>"
          f"/api/v1.0/start/end/2016-01-01/31-07-2017<br/>"
    )

# 4. Define what to do when a user hits this:
#  /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
  # Create session (link) from Python to the DB
    session = Session(engine)
    # Query all precipitation in the last year
    results = session.query(Measurement.date,Measurement.prcp).\
    filter(and_(Measurement.date>="2016-08-23",Measurement.prcp!="None")).\
    order_by(Measurement.date)
    Precipitation_list = [result[0] for result in results]
    Date_list = [result[1] for result in results]
    zipbObj = zip(Precipitation_list, Date_list)
    dictOfPrecip = dict(zipbObj)
    session.close()
    print("Server received request for 'Precipitation in the last year'...")
    return jsonify(dictOfPrecip)         

# 5. Define what to do when a user hits this:
#  /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def stations():
  # Create session (link) from Python to the DB
    session = Session(engine)
    # Query all stations
    stations = session.query(Station.name).distinct().all()
    session.close()
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations))
    print("Server received request for 'Stations'...")
    return jsonify(all_stations)         


# 6. Define what to do when a user hits this:
#   `/api/v1.0/<tobs>`
@app.route("/api/v1.0/tobs")
def tobs():
  # Create session (link) from Python to the DB
    session = Session(engine)
    # Query active station last year

    active1_tobs = session.query(Measurement.date,Measurement.tobs).\
    filter(and_(Measurement.station=='USC00519281',Measurement.date>="2016-08-23")).\
    order_by((Measurement.date).desc()).all()
  
    session.close()
     # Convert list of tuples into normal list
    all_tobs = list(np.ravel(active1_tobs))

    print("Server received request for 'Most active station Temperatures in the last year'...")
    return jsonify(all_tobs)         

#7. Define what to do when a user hits this:
#   `/api/v1.0/<start>` route
@app.route("/api/v1.0/start_date/<start_date>")
def dates(start_date):
  # Create session (link) from Python to the DB
    session = Session(engine)
  # Query tobs with date range
    Startminavgmax = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    session.close()
  # Convert list of tuples into normal list
    startamm = list(np.ravel(Startminavgmax))
    print("Server received request for 'MIN, AVG and MAX' from start date...")
    return  jsonify(startamm) 


# 8. Define what to do when a user hits this:
#  `/api/v1.0/datestwo/<start>/<end>` route
@app.route("/api/v1.0/start/end/<start>/<end>")
def datestwo(start,end):
  # Create session (link) from Python to the DB
    session = Session(engine)
  # Query tobs with date range
    minavgmax = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
      filter(and_(Measurement.date>=start,Measurement.date<=end)).all()
    session.close()
  # Convert list of tuples into normal list
    startendamm = list(np.ravel(minavgmax))
    print("Server received request for 'MIN, AVG and MAX' from start date to end date...")
    return  jsonify(startendamm) 


if __name__ == "__main__":
    app.run(debug=True)

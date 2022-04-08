# SQLAlchemy-challenge
Surfs Up!  Climate analysis!

I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with the trip planning, I need to do some climate analysis on the area. 

Python and SQLAlchemy are used to do climate analysis and data exploration of the climate database including SQLAlchemy ORM queries, Pandas, and Matplotlib.

The climate analysis can be found at [starter notebook](/main/climate_starter.ipynb). This includes the precipiation analysis and the station analysis.

A Flask API was designed based on the queries developed. [app/py](/main/app.py)

To run the app.py, nevigate to the folder and type "python app.py".
Open the homepage and adjust the url to your selection from the list of routes:
/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/start_date/2011-05-01
/api/v1.0/start/end/2016-01-01/31-07-2017

The following code contains additional queries: 
[bonus 1](./temp_analysis_bonus_1_starter.ipynb) and [bonus 2](./temp_analysis_bonus_2_starter.ipynb)

![Home Page](./images/homepage.png)

![Precipitaion](./images/precipitation.png)

![Start End](./images/start-end.png)

![Start Date](./images/startdate.png)

![Stations](./images/stations.png)

![Tobs](./images/tobs.png)
This climate analysis can be found at [starter notebook](./climate_starter.ipynb). This includes the precipiation analysis and the station analysis.

I designed a Flask API based on the queries that were just developed. [app/py](./app.py)

The following are optional challenge queries: 
[bonus 1](./temp_analysis_bonus_1_starter.ipynb) and [bonus 2](./temp_analysis_bonus_2_starter.ipynb)

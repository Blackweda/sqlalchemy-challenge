# Import the dependencies.
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################



# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


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

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")

@app.route("/api/v1.0/tobs")

@app.route(f"/api/v1.0/{start}")

@app.route(f"/api/v1.0/{start}/{end}")



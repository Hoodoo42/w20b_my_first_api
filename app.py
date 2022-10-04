# importing packaeges neccesary for the project
import dbhelpers as dbh
from flask import Flask
import json

#
app = Flask(__name__)

# @app is like an eventlistener. It matches the flask function to the function that follows it
# it holds the endpoint


@app.get('/animals')
# this function is using dbhelpers to open db connection, grab the stated procedure needed and then close the db connection.
# it then confirms it recieved data by checking to see if the type is list
# next is serializes to json and then returns the collected data.
def get_animals():
    results = dbh.run_statement('CALL get_animals')
    if (type(results) == list):
        animal_json = json.dumps(results, default=str)
        return animal_json
    else:
        return "Sorry there is an error"


@app.get('/dogs')
def get_dogs():
    results = dbh.make_api('CALL get_dogs()')
    return results


@app.get('/cats')
def get_cats():
    results = dbh.make_api('CALL get_cats()')
    return results


# this runs the code in a debug environment.
app.run(debug=True)

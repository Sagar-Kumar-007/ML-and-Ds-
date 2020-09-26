from flask import Flask, request, \
    jsonify  # jsonify is used to convert the data type list into json ( Since http response from the server cannot be a list )
import main  # importing main.py module to use its functions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/get_location_names/")
def get_location_names():
    response = jsonify({
        'location': main.get_locations()
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')   # To have access to CORS
    return response


@app.route("/get_area_type/")
def get_area_type():
    response = jsonify({
        "area_type": main.get_area_type()
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/get_estimated_price/", methods=['POST'])
def get_estimated_price():
    size = request.form['size']
    total_sqft = request.form['total_sqft']
    balcony = request.form['balcony']
    area_type = request.form['area_type'].lower()
    location = request.form['location'].lower()
    response = jsonify({
        "estimated_price": main.get_estimated_price(size, total_sqft, balcony, location, area_type)
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run()

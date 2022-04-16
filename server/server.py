from ctypes import util
import string
from aem import app
from flask import Flask, request, jsonify
from matplotlib.pyplot import text
import utils

app = Flask(__name__)

@app.route("/get_areas")
def get_areas():
    response = jsonify({
        "areas" : ["Built-up","Carpet","Plot","Super"]
    })
    response.headers.add("Access-Control-Allow-Origin","*")

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    sqft = float(request.form.get('total_sqft'))
    bath = float(request.form.get('bath'))
    balcony = float(request.form.get('balcony'))
    bhk = float(request.form.get('bhk'))
    area = request.form.get('area')
    area = area.split(" ")[0]

    response = jsonify({
        'estimated_price': utils.get_price_prediction(sqft,bath,balcony,bhk,area)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("starting python flask server for home price prediction")
    utils.load_save_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=True)
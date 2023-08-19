from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/get_location_names" , methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/predict_home_price", methods=['GET','POST'])
def predict_home_price():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    lift = int(request.form['lift'])
    location = request.form['location']
    carPark = int(request.form['carPark'])
    
    
    estimated_price = util.get_estimated_price(area, location, bedrooms, lift, carPark)
    
    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    print("Starting Python Flask for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True )

from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('REPLIERS_KEY')
API_ENDPOINT = 'https://api.repliers.io/listings'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_listings')
def get_listings():
    cluster = request.args.get('cluster', 'true')
    precision = request.args.get('precision', '10')
    limit = request.args.get('limit', '10')
    min_price = request.args.get('minPrice', '1')
    max_price = request.args.get('maxPrice', '10000000')
    property_type = request.args.get('propertyType')  # Use camelCase to match HTML
    status = request.args.get('statusFilter')  # Use statusFilter to match HTML
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')
    basement = request.args.get('basement')
    garage = request.args.get('garage')

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "REPLIERS-API-KEY": API_KEY
    }

    params = {
        'cluster': cluster,
        'clusterPrecision': precision,
        'clusterLimit': limit,
        'listings': True,
        'hasImages': True,
        'minPrice': min_price,
        'maxPrice': max_price,
        'propertyType': property_type,
        'statusFilter': status,  # Adjusted to match parameter name
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'basement': basement,
        'garage': garage        
    }

    result_fields = ("address.*,map.*,mlsNumber,listPrice,originalPrice,images[1],"
                     "details.numBedrooms,details.numBathrooms,details.sqft,"
                     "details.numGarageSpaces,details.propertyType,lastStatus,lot.,resource")

    api_url = f'{API_ENDPOINT}?fields={result_fields}'
    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({'error': f'Failed to fetch data. Error: {str(e)}'}), 500


@app.route('/search')
def search():
    return render_template('map.html')

@app.route('/markettrends')
def markettrends():
    return render_template('markettrends.html')

@app.route('/homevalues')
def homevalues():
    return render_template('homevalues.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        pass
    return render_template('join.html')

if __name__ == '__main__':
    app.run(debug=True)

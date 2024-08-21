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
    return render_template('map.html')

@app.route('/get_listings')
def get_listings():
    cluster = request.args.get('cluster', 'true')  # Control clustering with a query parameter
    precision = request.args.get('precision', '10')
    limit = request.args.get('limit', '10')
    
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    
    params = {
        'cluster': cluster,
        'clusterPrecision': precision,
        'clusterLimit': limit,
        'listings': True, # Fetch detailed listings if not clustering
        'hasImages': True
    }

    result_fields = "address.,mlsNumber,listPrice,originalPrice,images[1],details.numBedrooms,details.numBathrooms,details.sqft,details.numGarageSpaces,details.propertyType,lastStatus,lot.,resource"
    
    api_url = f'https://api.repliers.io/listings?fields={result_fields}'
    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': f'Failed to fetch data. Status code: {response.status_code}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

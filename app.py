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

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    map_data = data.get('map')
    map_operator = data.get('mapOperator', 'OR')  # Default to 'OR' if not provided

    # Prepare the request parameters
    params = {
        'mapOperator': map_operator,
        'apiKey': API_KEY
    }

    headers = {'Content-Type': 'application/json'}

    try:
        # Send the POST request to the real estate API
        response = requests.post(API_ENDPOINT, json={'map': map_data}, params=params, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        # Return the JSON response back to the frontend
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/filter-listings', methods=['POST'])
def filter_listings():
    data = request.json

    if 'map' not in data:
        return jsonify({"error": "Map parameter is required"}), 400

    payload = {
        "map": data['map']
    }

    params = {
        'apiKey': API_KEY
    }

    if 'mapOperator' in data:
        params['mapOperator'] = data['mapOperator']

    if 'other_filters' in data:
        params.update(data['other_filters'])

    headers = {'Content-Type': 'application/json'}

    try:
        # Make the POST request to the real estate API
        response = requests.post(API_ENDPOINT, json=payload, params=params, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/markettrends')
def markettrends():
    return render_template('markettrends.html')

@app.route('/homevalues')
def homevalues():
    return render_template('homevalues.html')

@app.route('/agents')
def agents():
    return render_template('agents.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

if __name__ == '__main__':
    app.run(debug=True)

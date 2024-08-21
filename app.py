from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('yDgFEZO0g76kMWiy6ADBnB0AojzF2E')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/property')
def property_page():
    # Example API request (replace with your actual API endpoint)
    url = 'https://api.repliers.com/properties'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        properties = response.json()
        return render_template('property.html', properties=properties)
    else:
        return render_template('property.html', error='Failed to fetch properties')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/join')
def join():
    return render_template('join.html')

if __name__ == '__main__':
    app.run(debug=True)

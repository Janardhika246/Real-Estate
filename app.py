from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv('yDgFEZO0g76kMWiy6ADBnB0AojzF2E')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/property')
def property_page():
    return render_template('property.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/join')
def join():
    return render_template('join.html')


if __name__ == '__main__':
    app.run(debug=True)

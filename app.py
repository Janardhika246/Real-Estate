from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # You can add dynamic data fetching from an API or database here
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
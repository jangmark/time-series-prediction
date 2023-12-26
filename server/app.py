from flask import render_template,Flask, request
import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    # Define the list of oil types
    oil_types = ['Brent', 'Dubai','WTI']

    # Get the value of the dropdown form element
    selected_oil = oil_types[0]  # set a default value
    if 'dropdown' in request.form:
        selected_oil = request.form['dropdown']

    # Pass the selected oil type to the prediction.html templat
    return render_template('index.html',oil=selected_oil,oil_types=oil_types)

@app.route('/time_page', methods=['GET','POST'])
def next_page():

    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)


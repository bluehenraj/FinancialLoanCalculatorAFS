from flask import Flask, render_template, url_for, request, redirect
import os
import sys
from dotenv import load_dotenv

app = Flask(__name__)

# Load the environment variables
load_dotenv()
# Set the environment variable
database_url = os.environ["DATABASE_URL"]
# Home
@app.route('/')
def my_home():
    return render_template('index.html')

# Redirect Pages
@app.route('/form')
def form_page():
    return render_template('form.html')

@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

# Submitting form
@app.route('/submitform', methods=['POST'])
def form_submit():

    first_name = request.form['firstname']
    last_name = request.form['lastname']

    income = request.form['incomeTotal']
    debtTotal = request.form['debtTotal']

    rent = request.form.get('rent', None)
    propTax = request.form.get('propTaxes', None)
    phone_number = request.form.get('phone', None)

    power = request.form.get('power', None)
    waterSewer = request.form.get('waterSewer', None)
    insurance = request.form.get('insurance', None)

    return render_template('index.html')

# App run
if __name__ == "__main__":
    app.run(debug=True)

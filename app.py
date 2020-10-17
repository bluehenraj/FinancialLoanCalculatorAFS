from flask import Flask, render_template, url_for, request, redirect
import os
import sys
from dotenv import load_dotenv

app = Flask(__name__)

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

    rent = request.form.get('rent')
    propTax = request.form.get('propTaxes')
    phone = request.form.get('phone')

    power = request.form.get('power')
    waterSewer = request.form.get('waterSewer')
    insurance = request.form.get('insurance')

    print(first_name)
    print(last_name)

    print(income)
    print(debtTotal)

    print(rent)
    print(propTax)
    print(phone)

    print(power)
    print(waterSewer)
    print(insurance)

    return  render_template('index.html')

# App run
if __name__ == "__main__":
    app.run(debug=True)

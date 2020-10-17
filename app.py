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
    # Must haves
    # Name
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    # Financial Information (Needed)
    income = request.form['incomeTotal']
    debt_total = request.form['debtTotal']

    # Can be without
    # Housing Information
    rent = request.form.get('rent')
    prop_tax = request.form.get('propTaxes')
    phone_number = request.form.get('phone')
    # Utilities
    power = request.form.get('power')
    water_sewer = request.form.get('waterSewer')
    garbage = request.form.get('gargagerecycling')
    bundlepackage = request.form.get('bundlepackagecable')
    # HealthCare
    prescriptions = request.form.get('prescriptions')
    doctorvisits = request.form.get('doctorvisits')
    # ChildCare
    daycare = request.form.get('daycare')
    # Automobile
    carpayment1 = request.form.get('carpayment')
    carpayment2 = request.form.get('carpayment#2')
    autoinsurance = request.form.get('autoinsurance')
    gasoline = request.form.get('gasoline')
    # Food
    groceries = request.form.get('groceries')
    pchi = request.form.get('personalcarehomeitems')

    q = Query(first_name, last_name, prop_tax, phone_number, rent, debt_total, income,
              power, water_sewer, insurance)
    q.create_tables()
    q.insert_all()

    return render_template('index.html')

# App run
if __name__ == "__main__":
    app.run(debug=True)

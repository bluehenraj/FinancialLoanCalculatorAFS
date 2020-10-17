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

#   quiz
@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

@app.route('/quizpages/videopage')
def video_page():
    return render_template('/quizpages/videopage.html')


@app.route('/quizpages/question2')
def question2_page():
    return render_template('/quizpages/question2.html')

@app.route('/quizpages/question2bad')
def question2bad_page():
    return render_template('/quizpages/question2bad.html')

@app.route('/quizpages/question31')
def question31_page():
    return render_template('/quizpages/question31.html')

@app.route('/quizpages/question31bad')
def question31bad_page():
    return render_template('/quizpages/question31bad.html')

@app.route('/quizpages/question32')
def question32_page():
    return render_template('/quizpages/question32.html')

@app.route('/quizpages/question32bad')
def question32bad_page():
    return render_template('/quizpages/question32bad.html')

@app.route('/quizpages/results')
def results_page():
    return render_template('/quizpages/results.html')


# Submitting form
@app.route('/submitform', methods=['POST'])
def form_submit():

    """
    # Mandatory
    # Name
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    # Financial Information
    income = request.form['incomeTotal']
    debt_total = request.form['debtTotal']
    # Can do without
    # Housing Information
    rent = request.form.get('rent')
    prop_tax = request.form.get('propTaxes')
    phone = request.form.get('phone')
    # Utilities
    power = request.form.get('power')
    water = request.form.get('waterSewer')
    garbage = request.form.get('garbagerecycling')
    cable = request.form.get('bundlepackagecable')
    # Healthcare
    prescriptions = request.form.get('prescriptions')
    doctor_visits = request.form.get('doctorvisits')
    # Childcare
    daycare = request.form.get('daycare')
    # Automobile
    carpayment1 = request.form.get('carpayment1')
    carpayment2 = request.form.get('carpayment&2')
    autoinsurance = request.form.get('autoinsurance')
    gasoline = request.form.get('gasoline')
    # Food
    groceries = request.form.get('groceries')
    pchi = request.form.get('personalcarehomeitems')
    """
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            data = data.items()
            print(data)
        except Exception as e:
            print(e)
            return 'Did not work'
    else:
        return 'something went wrong. try again!'

    return  render_template('index.html')

# App run
if __name__ == "__main__":
    app.run(debug=True)

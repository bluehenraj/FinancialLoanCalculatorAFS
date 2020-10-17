from flask import Flask, render_template, url_for, request, redirect
import os
import sys
from dotenv import load_dotenv
from Query import Query

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

@app.route('/quizpages/videopage')
def video_page():
    return render_template('/quizpages/videopage.html')

# Submitting form
@app.route('/submitform', methods=['POST'])
def form_submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            data = data.items()
            condensed = [i[1] for i in data]
            for index, val in enumerate(condensed):
                if val == '':
                    condensed[index] = 0
            print(condensed)
            q = Query(condensed[0], condensed[1], condensed[2], condensed[3], condensed[4], condensed[5],
                      condensed[6], condensed[7], condensed[8], condensed[9], condensed[10], condensed[11],
                      condensed[12], condensed[13], condensed[14], condensed[15], condensed[16], condensed[17],
                      condensed[18])
            q.create_tables()
            q.insert_all()
        except Exception as e:
            print(e)
            return 'Did not work'
    else:
        return 'something went wrong. try again!'

    return  render_template('index.html')

# App run
if __name__ == "__main__":
    app.run(debug=True)

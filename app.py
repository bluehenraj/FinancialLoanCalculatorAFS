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
            id_num = q.insert_all()
            print(id_num)
            if condensed[21] != 0:
                q.insert_email(condensed[21], id_num)
        except Exception as e:
            print(e)
            return 'Did not work'
    else:
        return 'something went wrong. try again!'

    return redirect(url_for('thankyou'))


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


# App run
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for
import os
import sys

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


# App run
if __name__ == "__main__":
    app.run(debug=True)

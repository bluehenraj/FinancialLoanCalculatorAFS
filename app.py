from flask import Flask, render_template, url_for
import os
import sys


app = Flask(__name__)


# Home
@app.route('/')
def my_home():
    return render_template('index.html')


# Redirect Pages
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# App run
if __name__ == "__main__":
    app.run(debug=True)

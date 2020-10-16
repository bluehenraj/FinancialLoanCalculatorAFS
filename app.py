from flask import Flask, render_template, url_for
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

# App run
if __name__ == "__main__":
    app.run(debug=True)

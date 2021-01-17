from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    meal_response = requests.get("http://qrandom:5000/meal")
    qran_response = requests.post("http://qrandom:5000/qran", data = meal_response.text)
    return render_template("index.html", meal = meal_response.text, qran=qran_response.text)
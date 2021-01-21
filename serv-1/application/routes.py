from application import app, db
from flask import render_template
from flask import request
import requests
import json

class Qrand(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    qran_num = db.Column(db.String(24), nullable=False)
    qran_meal = db.Column(db.String(24), nullable=False)
    qran_what = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    qran_response = requests.get("http://qrandom-qran:5000/qran")
    meal_response = requests.get("http://qrandom-meal:5000/meal")
    
    whatudone_response = requests.post("http://qrandom-whatudone:5000/whatudone", json = { 'qran' : qran_response.text, 'meal' : meal_response.text })
    
    new_qran = Qrand(qran_num = qran_response.text, qran_meal = meal_response.text, qran_what = whatudone_response.text)
    db.session.add(new_qran)
    db.session.commit()

    all_qran = Qrand.query.all()

    return render_template("index.html", meal = meal_response.text, qran=qran_response.text, whatudone=whatudone_response.text, all_qran = all_qran)
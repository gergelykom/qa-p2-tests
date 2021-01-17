from application import app
from flask import request, Response
import random


@app.route("/qran", methods=["GET"])
def get_qran():
    qrans = ["6", "12", "36"]
    return Response(str(random.choice(qrans)), mimetype = 'text/plain')

@app.route("/meal", methods=["POST"])
def get_meal():
    meals = { "6" : "burger", "12" : "salad", "18" : "fish&chips" }

    meal = request.data.decode("utf-8")
    return Response(noises[meal], mimetype = 'text/plain')
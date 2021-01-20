from application import app
from flask import request, Response
import random


@app.route("/meal", methods=["POST"])
def get_meal():
    meals = [ 'pasta', 'burger', 'pizza', 'pbj' ]
    meal = request.data.decode("utf-8")
    return Response(str(random.choice(meals)), mimetype = 'text/plain')
    



from application import app
from flask import request, Response
import random


@app.route("/qran", methods=["GET"])
def get_qran():
    qrans = [ '60' , '600' , '1800' , '2400' , '3600' , '4200']
    return Response(str(random.choice(qrans)), mimetype = 'text/plain')
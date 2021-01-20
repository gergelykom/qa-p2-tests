from application import app
from flask import request, Response
import random


@app.route("/qran", methods=["GET"])
def get_qran():
    qrans = random.getrandbits(12)
    return Response(str(qrans), mimetype = 'text/plain')
from application import app
from flask import render_template
from flask import request
import requests

@app.route('/whatudone')
def whatudone():
    meal_response = requests.get("http://qrandom:5000/meal")
    qran_response = requests.get("http://qrandom:5000/qran")
    whatudone = ''

    if qran_response < 2000 and meal_response == 'pasta':
        whatudone = "Congratulations, you just destroyed the Universe!"
    elif 2000 <= qran_response and meal_response == 'pasta':
        whatudone = "You will roll 6 nat20's in a row!"

    elif qran_response < 2000 and meal_response == 'burger':
        whatudone = "You just aided the emergence of intelligent sushi!"
    elif 2000 <= qran_response and meal_response == 'burger':
        whatudone = "You just helped humanity to achieve techonological singularity!"

    elif qran_response < 2000 and meal_response == 'pizza':
        whatudone = "You will get a hearthburn!"
    elif 2000 <= qran_response and meal_response == 'pizza':
        whatudone = "You will cause doplhins to take over the Earth!"

    elif qran_response < 2000 and meal_response == 'pbj':
        whatudone = "You will cause flip-flops to be mandatory at fashion shows!"
    elif 2000 <= qran_response and meal_response == 'pbj':
        whatudone = "Your actions will start a war with a K3 civilisation!"
    
    return Response(str(whatudone), mimetype = 'text/plain')
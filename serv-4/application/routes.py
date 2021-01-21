from application import app
from flask import render_template
from flask import request, Response
import json

@app.route("/whatudone", methods=["POST", "GET"])
def whatudone():
    get_meal = request.json['meal']
    get_qran = int(request.json['qran'])
    

    if get_qran < 2000 and get_meal == 'pasta':
        whatudone = "Congratulations, you just destroyed the Universe!"
    elif 2000 <= get_qran and get_meal == 'pasta':
        whatudone = "You will roll 6 nat20's in a row!"

    elif get_qran < 2000 and get_meal == 'burger':
        whatudone = "You just aided the emergence of intelligent sushi!"
    elif 2000 <= get_qran and get_meal == 'burger':
        whatudone = "You just helped humanity to achieve techonological singularity!"

    elif get_qran < 2000 and get_meal == 'pizza':
        whatudone = "You will get a hearthburn!"
    elif 2000 <= get_qran and get_meal == 'pizza':
        whatudone = "You will cause doplhins to take over the Earth!"

    elif get_qran < 2000 and get_meal == 'pbj':
        whatudone = "You will cause crocs to be mandatory at fashion shows!"
    elif 2000 <= get_qran and get_meal == 'pbj':
        whatudone = "Your actions will start a war with a K3 civilisation!"
    
    return Response(str(whatudone), mimetype = 'text/plain')
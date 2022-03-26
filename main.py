
from EcoleDirect import *
from flask import Flask
from flask import render_template, url_for, request, redirect
from json import *

app = Flask(__name__)
utilisateur = EcoleDirect("nom d'utilisateur", "mots de passe")


@app.route('/')
def index():

    return f""" 
        <a href="./travail">travail</a>
        </br></br>
        <a href="./note">note</a>
        </br></br>
        <a href="./message">message</a>
    """


@app.route('/travail')
def travail():
    xzdfazfa = utilisateur.getHW()
    json_dump = json.dumps(xzdfazfa)
    json_object = json.loads(json_dump)
            
    return render_template('travail.html',json_object=json_object)
@app.route('/travail/<jours>')
def travailjours(jours):
    xzdfazfa = utilisateur.getHWj(jours)
    json_dump = json.dumps(xzdfazfa)
    json_object = json.loads(json_dump)
            
    return render_template('travailjours.html',json_object=json_object)



@app.route('/note')
def note():
    xzdfazfa = utilisateur.getNotes()
    json_dump = json.dumps(xzdfazfa)
    json_object = json.loads(json_dump)
    test = " "
    for y in json_object['notes']:
        test = f"{y['libelleMatiere']}: {y['valeur']} / {y['noteSur']}   pour une moyenne de classe à {y['moyenneClasse']}"
    return f""" 
        {test}
    """

@app.route('/message')
def message():
    xzdfazfa = utilisateur.getmes()
    json_dump = json.dumps(xzdfazfa)
    json_object = json.loads(json_dump)
    test = " "
    teste = " "
    for y in json_object['messages']['received']:
        test = f"{test}{y['date']}______________  {y['from']['name']}</br></br>"
    for i in json_object['messages']['received']:
        teste = f"{teste}{i}<br/></br>"

    return f""" 
        {test}
    """

app.run(host='0.0.0.0', port=80)

from EcoleDirect import *
from flask import Flask
from flask import render_template, url_for, request, redirect
from json import *

app = Flask(__name__)
utilisateur = EcoleDirect("LUDOVICDEBORDE", "Sylvainc1")


@app.route('/')
def index():

    lien = ['travail','note','message']
    return render_template('index.html',lien=lien)
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
    liste = " "
    return render_template('note.html',json_object=json_object, liste=liste)
 
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

app.run(host='127.0.0.1', port=8080)
 
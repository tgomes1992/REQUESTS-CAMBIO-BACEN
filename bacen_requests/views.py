from flask import render_template , request , url_for , redirect
from bacen_requests.buscar import *
from bacen_requests.help_functions import formDateAdjustment
from bacen_requests import app


@app.route('/')
def home():
    return "all good"


@app.route('/home')
def mainIndex():
    moeda = show_options_server()
    return render_template("index.html",moedas=moeda)

@app.route('/consultar',methods=['POST'])
def consulta():
    req = request.form
    form_bacen = create_form_server(req['opcao'], formDateAdjustment(req['DATAINI']),req['MOEDA'])
    request_data_server(form_bacen)
    return redirect(url_for('mainIndex'))


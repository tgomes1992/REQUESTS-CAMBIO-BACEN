from flask import render_template , request , url_for , redirect
from bacen_requests.buscar import *
from bacen_requests.help_functions import formDateAdjustment
from bacen_requests import app
from bacen_requests.bacen import Bacen


banco = Bacen()


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


@app.route('/consulta',methods=['POST'])
def get_all_datas():
    req = request.form
    print (req)
    if req['opcao']=='2':
        df = banco.todas_em_uma_data(formDateAdjustment(req['DATAINI']))
    elif req['opcao']=='1':
        df = banco.uma_moeda_em_periodo(formDateAdjustment(req['DATAINI']), formDateAdjustment(req['DATAFIM']), req['MOEDA'])
    elif req['opcao']=='3':
        df = banco.intermediario_em_uma_data(formDateAdjustment(req['DATAINI']),int(req['MOEDA']))
    print (df)
    return redirect(url_for('mainIndex'))


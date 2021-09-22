from flask import render_template , request , url_for , redirect , send_file
from bacen_requests.buscar import *
from bacen_requests.help_functions import formDateAdjustment , define_filename , clean_folder
from bacen_requests import app
from bacen_requests.bacen import Bacen
import os


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
    clean_folder()
    req = request.form
    filename = f"{define_filename(req['opcao'])}.xlsx"
    if req['opcao']=='2':
        df = banco.todas_em_uma_data(formDateAdjustment(req['DATAINI']))
        df.to_excel(f"bacen_requests/temp-files/{filename}")
        return send_file(os.path.join("temp-files",filename),as_attachment=filename)
    elif req['opcao']=='1':
        df = banco.uma_moeda_em_periodo(formDateAdjustment(req['DATAINI']), formDateAdjustment(req['DATAFIM']), req['MOEDA'])
        df.to_excel(f"bacen_requests/temp-files/{filename}")
        return send_file(os.path.join("temp-files",filename),as_attachment=filename)
    elif req['opcao']=='3':
        df = banco.intermediario_em_uma_data(formDateAdjustment(req['DATAINI']),int(req['MOEDA']))
        df.to_excel(f"bacen_requests/temp-files/{filename}")
        return send_file(os.path.join("temp-files",filename),as_attachment=filename)
    return redirect(url_for('mainIndex'))





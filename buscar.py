import requests
from bs4 import BeautifulSoup 
import pandas as pd
pd.options.display.float_format = '${:,.2f}'.format

#get request info

url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim"

def prep_request():
    bacen_taxas = requests.get(url)   
    bacen_pagina = BeautifulSoup(bacen_taxas.content,'html.parser')
    options = bacen_pagina.findAll('option')
    #base do dataframe de moedas
    ndict = {
        'code': [] ,
        'moeda':[]
    }
    #criação do dataframe com as moedas
    for i in options:
        ndict['code'].append(i.attrs['value'])
        ndict['moeda'].append(i.text)
        #list_options.append(ndict)
    moedas = pd.DataFrame.from_dict(ndict)
    return moedas

moedas = prep_request()

def show_options():
#escolha as suas opções
    for item in moedas.iterrows():
        print (f"{item[0]}-{item[1].moeda}")

def get_moeda(id):
    try:
        moeda_selecionada = moedas[moedas.index==id]['code'].values[0]
    except Exception as e:
        print (e)
        print ('Tente Novamente')
        moeda_selecionada = "Não Localizada"
    return moeda_selecionada

def escolha_moeda():
    show_options()
    print ("Escolha a sua moeada")
    id = input ("Apenas os Números : ")
    resultado = get_moeda(int(id))
    return resultado

def escolha_data():
    data = input("Digite a data da solicitação: ")
    return data

def escolha_opcao():
    opcoes = '''Escolha a opção da solicitação
            1 - Cotações de fechamento de uma moeda em um período.
            2 - Cotações de fechamento de todas as moedas em uma data.
            3 - Cotações de fechamento de todas as moedas em uma data.'''
    print (opcoes)
    opcao = input()
    return opcao
    
def create_form():    
    form = {
        'RadOpcao': escolha_opcao(),
        'DATAINI': escolha_data(),
        'ChkMoeda':  escolha_moeda()
    }
    print (form)
    return form

def request_data():
    form  = create_form()
    post_bacen_taxas = requests.post(url,form)
    post_bacen_pagina = BeautifulSoup(post_bacen_taxas.content,'html.parser')
    html_table = str(post_bacen_pagina.find_all('table')[0])
    pandas_table = pd.read_html(html_table,
                            decimal=',',
                            thousands='.',
                            )[0]
    print (pandas_table.head())
    return pandas_table 


def tentativa():
    texto = '''Deseja tentar novamente ?
                1 - Sim
                2 - Não
                 '''
    valor = input (texto)
    if valor==str(1):
        resultado = "ok"
    else: 
        resultado = "not ok"
    return resultado


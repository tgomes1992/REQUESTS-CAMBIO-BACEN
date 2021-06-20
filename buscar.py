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
    return moedas = pd.DataFrame.from_dict(ndict)

moedas = prep_request()


def show_options():
#escolha as suas opções
    for item in moedas.iterrows():
        print (f"{item[0]}-{item[1].moeda}")

def get_moeda(id):
    try:
        moeda_selecionada = moedas[moedas.index==id]
    except Exception as e:
        print (e)
        print ('Tente Novamente')
        moeda_selecionada = "Não Localizada"
    return moeda_selecionada

def escolha_moeda():
    #show_options()
    print ("Escolha a sua moeada")
    id = input ("Apenas os Números : ")
    resultado = get_moeda(int(id))
    print (resultado)
    return resultado


#post request info
#todo 
    #função para o formulário
    #função para a post request
    #preparar os dados para exportação
    



form = {
    'RadOpcao': '2',
    'DATAINI': '15/06/2021',
    'ChkMoeda':  '177'
}

# post_bacen_taxas = requests.post(url,form)
# post_bacen_pagina = BeautifulSoup(post_bacen_taxas.content,'html.parser')
# html_table = str(post_bacen_pagina.find_all('table')[0])

# pandas_table = pd.read_html(html_table,
#                             decimal=',',
#                             thousands='.',
#                             )[0]

#pandas_table.to_excel("teste.xlsx")


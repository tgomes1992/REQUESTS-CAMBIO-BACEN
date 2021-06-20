import requests
from bs4 import BeautifulSoup 
import pandas as pd
pd.options.display.float_format = '${:,.2f}'.format

url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim"

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

for row in moedas.iterrows():
    

print (moedas)



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


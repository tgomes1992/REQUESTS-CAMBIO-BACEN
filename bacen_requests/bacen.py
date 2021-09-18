import requests
from bs4 import BeautifulSoup
import pandas as pd

class Bacen:

    URL = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim"


    def __init__(self):
        pass

    def create_form(self, op , dataini,  codigo_moeda  ,datafim=""):
        form_fields = {    
            'RadOpcao': op ,
            'DATAINI': dataini,
            'DATAFIM': datafim ,
            'ChkMoeda': codigo_moeda,
        }
        print (form_fields)
        return form_fields

    def get_moedas(self):
        lista = []
        with requests.session() as s:
            r = s.get(self.URL)
            soup = BeautifulSoup(r.content,'html.parser')
            moedas = soup.find_all('option')
            for i in moedas:
                ndict = {
                    'value':i['value'] ,
                    'moeda':i.text
                }
                lista.append(ndict)
            return lista

    def todas_em_uma_data(self,dia,moeda=61):
        form = self.create_form(2,dia,moeda)
        with requests.session() as s:
            r = s.post(self.URL,form)
            soup = BeautifulSoup(r.content,'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table),
                            decimal=',',
                            thousands='.',skiprows=1)[0]
            return df  
        
    def uma_moeda_em_periodo(self,diaini, dia_fim , moeda):
        form = self.create_form(1,diaini,moeda,dia_fim)
        with requests.session() as s:
            r = s.post(self.URL,form)
            soup = BeautifulSoup(r.content,'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table),
                            decimal=',',
                            thousands='.',skiprows=1)[0][['Data','Tipo','Compra','Venda']]
            
            return df


    def intermediario_em_uma_data(self,diaini,  moeda):
        form = self.create_form(3,diaini,moeda)
        with requests.session() as s:
            r = s.post(self.URL,form)
            soup = BeautifulSoup(r.content,'html.parser')
            table = soup.find('table')
            df = pd.read_html(str(table),
                            decimal=',',
                            thousands='.',skiprows=2)[0][['Hora', 'Compra','Venda']]
            df.columns = ["Hora",'Taxa Compra','compra' , 'Taxa Venda','venda']
            return df[['Hora', 'Taxa Compra',"Taxa Venda"]]

    





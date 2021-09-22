from datetime import datetime, date
import os



def webDateToString(webdate):
    ndate = webdate.strftime("%d/%m/%Y")
    return (ndate)
    


def webStringsToDate(webstring):
    ndate = datetime.strptime(webstring,'%Y-%m-%d')
    return ndate


def formDateAdjustment(formdate):
    ndate = datetime.strptime(formdate,'%Y-%m-%d')
    adjusted_date = ndate.strftime("%d/%m/%Y")
    return adjusted_date
    

def define_filename(opcao):
    if opcao=="1":
        return "Fechamento de uma moeda em um Período:"
    elif opcao=="2":
        return "Fechamento de todas as moedas em uma data:"
    else:
        return "Boletins Intermediários em uma data:"

def clean_folder():
    for file in os.listdir("bacen_requests/temp-files"):
        print (file)
        os.remove(f"bacen_requests/temp-files/{file}")


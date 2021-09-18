from bacen_requests.buscar import escolha_moeda ,create_form , request_data , tentativa

#Mensagens

msg_inicial  =  '''Bem vindo ao extrator bacen, esolha as opções conforme abaixo.'''

informacao = '''Esse é um extrator de taxas de câmbio do bacen. 
                A seguir escolha as opções e acompanhe o resultado'''


msg_list = [msg_inicial,informacao]


def main():
    msgs = [print (x) for x in msg_list]
    msgs
    try_again = True
    while try_again:
        request_data()
        ntry = tentativa()
        if ntry=='ok':
            try_again = True
        else:
            try_again = False
            print ("Volte Sempre!")

        

if __name__=='__main__':
    main()


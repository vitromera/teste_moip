'''
Created on 23 de jun de 2017

@author: vitromera
'''
import operator

# ABERTURA DO LOG PARA LEITURA
file = open("log.txt", "r")

# SEPARACAO DOS REGISTROS DO LOG
clnLog = file.read().strip()
regs = clnLog.split("\n")

file.close()

# ====== INICIALIZACAO DAS LISTS / DICTIONARIES ======
urls = {}
status = {}

# VARREDURA DOS REGISTROS PAR OBTENCAO DOS DADOS
for reg in regs:
    if reg[:10] == "level=info": # IDENTIFICA UM WEBHOOK
        items = reg.split(" ") # FRAGMENTA O WEBHOOK
        whook = {}
        for item in items:      # PARA CADA ITEM DO WEBHOOK, BUSCA SEPARAR O PARAMETRO DE SEU VALOR (CHAR '=')
            item_str = item.split("=") 
            if len(item_str) > 1:
                whook[item_str[0]] = item_str[1]
                
                # OBTENCAO DAS URLS E RESPECTIVO NUMERO DE MENCOES
                if item_str[0] == "request_to":
                    urls[item_str[1]] = urls.setdefault(item_str[1], 0) + 1 # FAZ O PRIMEIRO REGISTRO DA URL E SOMA A CADA VEZ QUE O VALOR APARECE
                
                # OBTENCAO DAS RESPONSE_STATUS E RESPECTIVO NUMERO DE MENCOES
                if item_str[0] == "response_status":
                    status[item_str[1]] = status.setdefault(item_str[1], 0) + 1 # FAZ O PRIMEIRO REGISTRO DA URL E SOMA A CADA VEZ QUE O VALOR APARECE
        
sorted_urls = sorted(urls.items(), key=operator.itemgetter(1), reverse=True)


# IMPRESSAO DOS RESULTADOS NA TELA
print("-------------------------------------------------------------------")
print("URL Rank by # of webhooks:\n")
for i in range(3):
    print(sorted_urls[i][0] + " - " + str(sorted_urls[i][1]))
    
print("-------------------------------------------------------------------")
print("Webhooks 'response_status' counter:")
for key in status.keys():
    print(key + " - " + str(status[key]))

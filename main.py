import requests
from tkinder import *
def pegar_cotacoes():
    requisica=requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    
    rqs= requisicao.json()

    dolarAtual= rqs_list['USDBRL'] ['bid']
    euroAtual= rqs_list['EURBRL'] ['bid']
    btcAtual= rqs_list['BTCBRL'] ['bid']

    TEXTO=f'''
    DOLAR:{dolarAtual}
    EURO:{euroAtual}
    BTC:{btcAtual}'''

    print(texto)


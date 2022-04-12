from distutils.command.config import config
import requests
import json
import config

print('----------------------------------------------------------------')
print("Este programa fornece a previsao do tempo da cidade escolhida")
cid = input("Digite o nome da cidade e seu estado  ")
print('----------------------------------------------------------------')
print('Resultado:')
print('----------------------------------------------------------------')
dados = requests.get('https://api.hgbrasil.com/weather?array_limit=2&fields=only_results,city_name,temp,description,currently,humidity,wind_speedy,sunrise,sunset,condition_slug,forecast,max,min,date&key={}&city_name={}'.format(config.chave,cid))
dados = dados.json()
#dados_basicos = dados['results']['description']
print(dados)


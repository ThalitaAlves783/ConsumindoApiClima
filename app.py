from distutils.command.config import config
import requests
import json
import config




class Tempo:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado


    def informar_temp_atual(self,dados):
        if dados ==  'Temperatura atual em graus celsius':
          dados = requests.get('https://api.hgbrasil.com/weather?array_limit=2&fields=only_results,city_name,temp&key={}&city_name={}'.format(config.chave,self.cidade))
          dados = dados.json()        
          print(dados) 

    def informar_data_hora(self,dados):
        if dados ==  'Data e Hora da consulta':
          dados = requests.get('https://api.hgbrasil.com/weather?array_limit=2&fields=only_results,city_name,,date,time&key={}&city_name={}'.format(config.chave,self.cidade))
          dados = dados.json()        
          print(dados) 


    def informar_dia_noite(self,dados):
        if dados ==  'Dia ou Noite':
          dados = requests.get('https://api.hgbrasil.com/weather?array_limit=2&fields=only_results,city_name,currently&key={}&city_name={}'.format(config.chave,self.cidade))
          dados = dados.json()        
          print(dados)

    def informar_umidade(self,dados):
        if dados ==  'umidade':
          dados = requests.get('https://api.hgbrasil.com/weather?array_limit=2&fields=only_results,city_name,humidity&key={}&city_name={}'.format(config.chave,self.cidade))
          dados = dados.json()        
          print(dados)  



tempo = Tempo('Belo horizonte','Minas Gerais')
tempo.informar_temp_atual('Temperatura atual em graus celsius')
tempo.informar_data_hora('Data e Hora da consulta')
tempo.informar_dia_noite('Dia ou Noite')
tempo.informar_umidade('umidade')







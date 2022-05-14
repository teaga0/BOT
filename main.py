import os
import time
import telebot
import requests
import json

ids = ['123124', '1231234123', '123124124']

print(ids[0])

TOKEN = '5305473022:AAGEpVIWYaxh9mH4RxhbFHRu7qpetRbxRlU'
bot = telebot.TeleBot(TOKEN)


def commands(messages):
   
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':

              textmsg = m.text
              text = m.text.split(" ")
             
              if text[0] == "/cep":
              
                try:
                  dados = requests.get("https://cep.awesomeapi.com.br/json/{}".format(text[1]))
                  dados = dados.json()
                  cep = dados['cep']
                  rua = dados['address_name']
                  estado = dados['state']
                  bairro = dados['district']
                  latitude = dados['lat']
                  longitude = dados['lng']
                  cidade = dados['city']
                  ibge = dados['city_ibge']
                  ddd = dados['ddd']
                  pri =("CEP:{}\nRua:{}\nEstado:{}\nBairro:{}\nLatitude:{}\nLongitude:{}\nCidade:{}\nIBGE:{}\nDDD:{}".format(cep, rua, estado, bairro, latitude, longitude, cidade, ibge, ddd))
                  bot.send_message(chatid, pri)
                except:
                  bot.send_message(chatid,"cep invalido tente sem '-' ")

              elif text[0] == "/ip":
                    print(chatid)
                    dadosip = requests.get("https://api.ipinfodb.com/v3/ip-city/?key=87da097b47b0b39e30b28ef4f537999ef4ca0fe5b5028626c697ca72d7fedb3b&ip={}&format=json".format(text[1]))
                    dadosip = dadosip.json()
                    statuscode = dadosip['statusCode']
                    if statuscode == "OK":
                      ip = dadosip['ipAddress']
                      code = dadosip['countryCode']
                      nome = dadosip['countryName']
                      estado = dadosip['regionName']
                      cidade = dadosip['cityName']
                      zipcode = dadosip['zipCode']
                      latitude = dadosip['latitude']
                      longitude = dadosip['longitude']
                      timeone = dadosip['timeZone']
                      bot.send_message(chatid, "status:{}\nip:{}\ncode:{}\nnome:{}\nestado:{}\ncidade:{}\nzipcode:{}\nlat:{}\nlong:{}\ntimezone:{}".format(statuscode, ip, code, nome, estado, cidade, cidade, zipcode, latitude, longitude, timeone))                  
                    else:
                      bot.send_message(chatid, "ip invalido")
              elif text[0] == "/cnpj":
                try:
                      dados = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(text[1]))
                      dados = dados.json()
                      atividade_principal = dados['atividade_principal']
                      data_situacao = dados['data_situacao']
                      complemento = dados['complemento']
                      tipo = dados['tipo']
                      nome = dados['nome']
                      estado = dados['uf']
                      telefone = dados['telefone']
                      email = dados['email']
                      atividades_secundarias = dados['atividades_secundarias']
                      situacao = dados['situacao']
                      bairro = dados['bairro']
                      logradouro = dados['logradouro']
                      numero = dados['numero']
                      cep = dados['cep']
                      municipio = dados['municipio']
                      porte = dados['porte']
                      abertura = dados['abertura']
                      natureza_juridica = dados['natureza_juridica']                     
                      bot.send_message(chatid, "ATIVIDADE PRINCIPAL:{}\nDATA SITUAÇAO:{}\nCOMPLEMENTO:{}\nTIPO:{}\nNOME:{}\nESTADO:{}\nTELEFONE:{}\nEMAIL:{}\nOUTRAS ATIVIDADES:{}\nSITUACAO:{}\nBAIRRO:{}\nLOGRADOURO:{}\nNUMERO:{}\nCEP:{}\nMUNICIPIO:{}\nPORTE:{}\nABERTURA:{}\nNATUREZA JURIDICA:{}\n".format(atividade_principal, data_situacao, complemento, tipo, nome, estado, telefone, email, atividades_secundarias, situacao, bairro, logradouro, numero, cep, municipio, porte, abertura, natureza_juridica))
                except:
                  bot.send_message(chatid, "cnpj invalido")
              else:
                bot.send_message(chatid, textmsg)


bot.set_update_listener(commands) 

bot.polling()

bot.polling(none_stop=True)

bot.polling(interval=3)

while True:
    pass


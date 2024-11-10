import os
import time
from datetime import date

import pandas as pd
import requests
import schedule
from bs4 import BeautifulSoup

urls = {'Sao_Paulo':'https://weather.com/pt-BR/clima/hoje/l/63e18eea74a484c42c3921cf52a8fec98113dbb13f6deb7c477b2f453c95b837',
'Parana':'https://weather.com/pt-BR/clima/hoje/l/4e6dc1807e947497fb8e0065241a1e4990ea4b5e9f35cb2385e81d14116ba0db',
'Salvador':'https://weather.com/pt-BR/weather/today/l/1a30b5660557a35bbc5aac31120b809ac9db04ea07027135e481d4f99e3af008',
'Goiania':'https://weather.com/pt-BR/clima/hoje/l/930b61e13ae96dc475625df8f694b2d0e87202ab825727b69594719b82b94a72',
'Belem':'https://weather.com/pt-BR/clima/hoje/l/9274324460970180f3c157f373dbde4b02af7eeb7ca08c7ec04b167b5744a5ce'}

def get_soap_object(url):
    r = requests.get(url)
    soap = BeautifulSoup(r.content, "html.parser")
    return soap

def data_de_hoje():
    data = date.today()
    data_formatada = data.strftime('%d/%m/%Y')
    return data_formatada

def coletar_dados(soap, data_formatada):
    # Procura e transforma em texto, retirando o html, transforma em lista e recorta depois da virgula para pegarmos o texto completo sem a parte depois da virgula.
    find_state_by_class = soap.find(class_="CurrentConditions--location--yub4l").text.split(",")[0]
    # find_temp = soap.find(class_="TodayDetailsCard--hero--rC8-j").text.split('térmica')[1].split('°')[0]
    find_temp = soap.find("span", attrs={"data-testid": "TemperatureValue"}).text.split('°')[0]
    temp_int = int(find_temp)
    find_min_max_temp = soap.find(class_="WeatherDetailsListItem--wxData--lW-7H").text.split('/')
    min_temp = find_min_max_temp[1]
    max_temp = find_min_max_temp[0]
    find_current_conditions = soap.find(class_="CurrentConditions--phraseValue---VS-k").text
    horario_coleta = soap.find(class_="CurrentConditions--timestamp--LqnOd").text.split("Até ")[1].split(" GMT")[0]
    
    linhas_arquivo = {"Local":[find_state_by_class], "Temp":[temp_int], "Minima":[min_temp], "Maxima":[max_temp], "Clima":[find_current_conditions], "Horário": [horario_coleta], "Data_Coleta" : [data_formatada]}
    return linhas_arquivo

def incluir_dados_excel(dados):
    df_novos = pd.DataFrame(dados)

    if os.path.exists('dados_climaticos_sp.xlsx'):
        with pd.ExcelFile('dados_climaticos_sp.xlsx') as xls:
            df = pd.read_excel(xls)
            df_final = pd.concat([df, df_novos], ignore_index=True)
    else:
        df_final = df_novos

    df_final.to_excel('dados_climaticos_sp.xlsx', sheet_name='Temperatura Regiões Brasil',index=False)
    print(df_final)

def tarefa_coleta_e_inclusao():
    for url in urls.values():
        data = data_de_hoje()
        soap = get_soap_object(url)
        dados = coletar_dados(soap, data)
        incluir_dados_excel(dados)

def timer():
    schedule.every(30).minutes.do(tarefa_coleta_e_inclusao)

    while True:
        schedule.run_pending()
        time.sleep(60)

timer()

# print(coletar_dados())
# find_min_temp = soap.find(id="min-temp-1").text
# find_max_temp = soap.find(id="max-temp-1").text
# print(h1_in_text)
# print(find_min_temp)
# print(find_current_conditions)

# with open('itens.txt', 'w') as arquivo_texto:
#     for linha in linhas_arquivo:
#         arquivo_texto.write(linha + "\n")

import pandas as pd
import requests
import sqlite3
from bs4 import BeautifulSoup
from pandas import DataFrame
import os

# Dados de conexão

url: str = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_name: str = 'PIB_por_pais'
csv_path: str = '../data/pib_paises.csv'
nome_csv: str = 'pib_paises.csv'
db = 'economia_mundial.db'

# Trecho referente a extração dos dados via webscrapping

def extracao_tabela(url):
    pagina = requests.get(url).text
    dados = BeautifulSoup(pagina,'html.parser')
    df = pd.DataFrame(columns=['País', 'PIB'])
    tabela = dados.find_all('tbody')
    rows = tabela[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"País": col[0].a.contents[0],
                             "PIB": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df



# Trecho referente a transformação dos dados com pandas


dados_tabela = extracao_tabela(url)

print(dados_tabela.loc[0])

dados_tabela["PIB"] = dados_tabela["PIB"].str.replace(",", "", 1).str.replace(",", ".").astype(float)

dados_tabela["PIB"] = dados_tabela['PIB'] / 1000

dados_tabela["PIB"] = dados_tabela["PIB"].map('{:,.2f}'.format)


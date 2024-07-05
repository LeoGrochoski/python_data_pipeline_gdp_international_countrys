import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# Dados de conexão

url: str = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_name: str = 'PIB_por_pais'
csv_bkp: str = '../backup/pib_paises.csv'
nome_csv: str = 'pib_paises.csv'


# Trecho referente a extração dos dados via webscrapping

def extracao_tabela(url):
    pagina = requests.get(url).text
    dados = BeautifulSoup(pagina,'html.parser')
    df = pd.DataFrame(columns=['Pais', 'PIB'])
    tabela = dados.find_all('tbody')
    rows = tabela[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Pais": col[0].a.contents[0],
                             "PIB": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df


# Trecho referente a transformação dos dados com pandas


dados_tabela = extracao_tabela(url)

dados_tabela["PIB"] = dados_tabela["PIB"].str.replace(",", "", 1).str.replace(",", ".").astype(float)

dados_tabela["PIB"] = dados_tabela['PIB'] / 1000

dados_tabela["PIB"] = dados_tabela["PIB"].map('{:,.2f}'.format)

# Criação de arquivo csv como backup dos dados

def salva_bkp_csv(diretorio_saida, nome_arquivo, df):
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    path_arquivo = os.path.join(diretorio_saida, nome_arquivo)

    df.to_csv(path_arquivo, index = False)

    print(f"Arquivo CSV '{nome_arquivo}' salvo com sucesso em '{diretorio_saida}'!")

salva_bkp_csv(csv_bkp, nome_csv, dados_tabela)


# Trecho referente ao carregamento dos dados

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

def carrega_banco (host, user, password, db, port):
    
    str_conexao = f"mysql://{user}:{password}@{host}:{port}/{db}?allowPublicKeyRetrieval=true&useSSL=false"
    print(f"Connection String: {str_conexao}")

    engine = create_engine(str_conexao)
    Conexao = sessionmaker(bind=engine)
    conexao = Conexao()
    return conexao

conexao_banco = carrega_banco(db_host, db_user, db_password, db_name, db_port)


cria_tabela = text(f'''CREATE TABLE Countries_by_GDP(
               	Pais VARCHAR,
               	PIB VARCHAR)
                   ''')


conexao_banco.execute(cria_tabela)

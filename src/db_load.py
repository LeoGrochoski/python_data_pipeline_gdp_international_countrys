import os
import pandas as pd
from dotenv import load_dotenv
from urllib.parse import quote_plus
import mysql.connector
import logging

logging.basicConfig(
    filename = "../log/code_logs.log", 
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
    )

# carregando variaveis 
load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

logging.info("conexao SQL iniciada")

# conexão com o banco
try: 
    conexao = mysql.connector.connect(
        user = db_user,
        password = db_password,
        host = db_host,
        database = db_name
    )
    cursor = conexao.cursor()
    logging.info(f"Conexao com Banco realizada, iniciando execucao das queries!")
except mysql.connector.Error as conn_err:
    logging.critical(f"Erro ao conectar com o banco: {conn_err}")


# Ao criar a tabela, se atentar em passar os tipos corretamente, inclusive o tamanho dos campos quando necessario

create_table = """
                  CREATE TABLE Countries_by_GDP (
                  Pais VARCHAR(255),
                  PIB NUMERIC(15, 2)
                  );
"""
try:
    cursor.execute(create_table)
    logging.info(f"Tabela Criada com sucesso, iniciando carregamento dos dados!")
    conexao.commit()
except mysql.connector.Error as cr_tab_err:
    logging.error(f"Falha ao criar a tabela devido: {cr_tab_err}")

# Importando csv do backup para criação do dataframe
df = pd.read_csv('../backup/pib_paises.csv/pib_paises.csv')

insert_query = """
    INSERT INTO Countries_by_GDP (Pais, PIB)
    VALUES (%s, %s)
"""

# Inserindo os dados na tabela do banco

try:
    for index, row in df.iterrows():
        cursor.execute(insert_query, (row["Pais"], row["PIB"]))
    logging.info("Dados importados com sucesso!")
    conexao.commit()
except mysql.connector.Error as imp_err:
    logging.error(f"Erro ao inserir dados: {imp_err}")

conexao.commit()

# Selecionando paises com PIB maior que 100 bilhões.


select_table = """SELECT * FROM countries_by_gdp WHERE PIB >= 100"""

try:
    cursor.execute(select_table)
    retorno = cursor.fetchall()
    for row in retorno:
        print(row)
except mysql.connector.Error as er:
    logging.error(f"Erro ao executar SELECT: {er}")
except Exception as e:
    logging.error(f"Erro inesperado: {e}")
finally:
    cursor.close()
    conexao.close()
    logging.info("Conexao fechada")
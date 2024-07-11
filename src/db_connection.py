import os
import pandas as pd
from dotenv import load_dotenv
from urllib.parse import quote_plus
import mysql.connector

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

conexao = mysql.connector.connect(
    user = db_user,
    password = db_password,
    host = db_host,
    database = db_name
)

cursor = conexao.cursor()

try:
    conexao = engine.connect()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")

# Ao criar a tabela, se atentar em passar os tipos corretamente, inclusive o tamanho dos campos quando necessario
# create_table = """
#                   CREATE TABLE Countries_by_GDP (
#                   Pais VARCHAR(255),
#                   PIB NUMERIC(15, 2)
#                   );
# """
# cursor.execute(create_table)6
#
# conexao.commit()
# 
# print("Tabela Criada com sucesso!")


df = pd.read_csv("C:\Lab\python_data_pipeline_gdp_international_countrys\backup\pib_paises.csv\pib_paises.csv")

cursor.execute()

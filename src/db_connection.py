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


df = pd.read_csv('../backup/pib_paises.csv/pib_paises.csv')

insert_query = """
    INSERT INTO Countries_by_GDP (Pais, PIB)
    VALUES (%s, %s)
"""

try:
    for index, row in df.iterrows():
        cursor.execute(insert_query, (row["Pais"], row["PIB"]))
    conexao.commit()
    print("Dados importados com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro ao inserir dados: {err}")
finally:
    cursor.close()
    conexao.close()
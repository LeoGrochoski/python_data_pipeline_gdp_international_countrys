# Pipeline de Dados com Python: PIB Paises

![Imagem](./pics/pipeline.png)

## Objetivo do Projeto

Objetivo do Projeto: Engenharia de Dados com Python
O objetivo deste projeto é aplicar e consolidar as habilidades adquiridas ao longo do curso de formação para Engenharia de Dados oferecido pela IBM. Neste curso, intitulado Python Project for Data Engineering, os participantes são desafiados a implementar uma pipeline completa de ETL (Extract, Transform, Load) utilizando Python.

Como parte do cenário do projeto, uma empresa internacional, que está em expansão para diversos países, contratou você, um engenheiro de dados júnior, para criar um script automatizado. Este script tem como finalidade extrair, transformar e carregar dados de uma lista de países ordenados por seus PIBs em bilhões de dólares americanos, conforme reportado pelo Fundo Monetário Internacional (FMI). Este relatório é publicado duas vezes ao ano e o código desenvolvido será utilizado para capturar essas atualizações de forma eficiente.

Através deste projeto, os participantes demonstram sua proficiência em técnicas essenciais de manipulação de dados, incluindo a extração de dados de múltiplas fontes, web scraping, utilização de APIs e preparação dos dados para análise em bancos de dados. Além de reforçar os conhecimentos em Python, este projeto proporciona uma valiosa experiência prática em um cenário realista, contribuindo significativamente para o portfólio profissional dos alunos.

Este curso é uma continuação natural do Python for Data Science, AI and Development da IBM, sendo necessário que os participantes tenham uma base sólida em Python e manipulação de dados antes de iniciar este projeto. Ao final, os alunos terão mostrado sua capacidade de construir pipelines de dados robustas e eficientes, uma competência fundamental para qualquer engenheiro de dados.

### Pontos Práticos para Projeto

1.  Escrever uma função de extração de dados para recuperar as informações relevantes do URL fornecido.

2.  Transformar as informações disponíveis do PIB em 'Bilhões de dólares' de 'Milhões de dólares'.

3.  Carregar as informações transformadas no arquivo CSV necessário e como um arquivo de banco de dados.

4.  Execute a consulta necessária no banco de dados.

5. Registrar o progresso do código com logs de data/hora apropriados.

### Principais desafios do projeto

- Realizar a localização da tabela com os dados de interesse via html;
- Iterar pelas linhas trazendo os dados de forma correta e disponibilizar para as transformações;
- Converter o formato do valor para poder transformar milhões para bilhões de dolares, reduzir para duas casas apos a virgula;
- Criação do backup dos dados em .csv;

### Como rodar o projeto

1. Acessar o repositorio do github localizado [aqui](https://github.com/LeoGrochoski/python_data_pipeline_gdp_international_countrys) para verificar mais sobre a documentação.

2. Efetuar o clone do repositorio.
~~~bash
git clone https://github.com/LeoGrochoski/python_data_pipeline_gdp_international_countrys.git
~~~

3. Ativar o ambiente virtual.
~~~bash
source .venv/Scripts/activate
~~~

4. Instalar as bibliotecas necessarias.
~~~python
pip install requirements.txt
~~~

5. rodar o comando para iniciar o etl.
~~~bash
.run_etl
~~~

6. Para verificar se o etl ocorreu conforme deve, verificar os logs
* O arquivo logs_web_scrapping_extract.logs registra os logs da extração e transformação dos dados.
* O arquivos logs_db_load.log registra os logs do carregamento dos dados do banco e a seleção dos dados conforme regra.
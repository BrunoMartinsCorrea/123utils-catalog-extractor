import pandas
import requests

# URL para obter o JSON
url = 'https://123util.com.br/estoque/prod.json'

# Faz a requisição e obtém o JSON de resposta
response = requests.get(url).json()

# Carrega o JSON em um DataFrame para exportar um CSV
pandas.DataFrame.from_dict(response).to_csv('data.csv')

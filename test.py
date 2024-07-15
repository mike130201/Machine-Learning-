import requests
import pandas as pd

# URL del archivo CSV con datos meteorológicos (ejemplo)
url = "https://opendata.dwd.de/path/to/data.csv"
response = requests.get(url)
with open('data.csv', 'wb') as file:
    file.write(response.content)

# Cargar los datos en un DataFrame de pandas
data = pd.read_csv('data.csv')

# Mostrar los primeros registros
print(data.head())
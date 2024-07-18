import os
import pandas as pd

# Ruta del archivo de texto
archivo_txt = r"C:\Users\Miguel\Downloads\temperature 3379\produkt_tu_termin_19850101_20231231_03379.txt"

# Leer el archivo de texto
df = pd.read_csv(archivo_txt, delimiter=';')

# Ruta completa del archivo CSV, incluyendo el nombre del archivo
temp = r'C:\Users\Miguel\OneDrive\Documentos\UDLAP\Exchange\Python\Machine-Learning-\temp.csv'

# Verificar si el directorio existe, y si no, crearlo
directorio = os.path.dirname(temp)
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Guardar el DataFrame como un archivo CSV
df.to_csv(temp, index=False)

print(f"Archivo CSV guardado correctamente en {temp}")

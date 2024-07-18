import os
import pandas as pd

# Ruta del archivo de texto
archivo_txt = r"C:\Users\Miguel\Downloads\wind 3379\produkt_fk_termin_18900101_19730630_03088.txt"

# Leer el archivo de texto
df = pd.read_csv(archivo_txt, delimiter=';')

# Ruta completa del archivo CSV, incluyendo el nombre del archivo
temp = r'C:\Users\Miguel\OneDrive\Documentos\UDLAP\Exchange\Python\Machine-Learning-\wind.csv'

# Verificar si el directorio existe, y si no, crearlo
directorio = os.path.dirname(temp)
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Guardar el DataFrame como un archivo CSV
df.to_csv(temp, index=False)

print(f"Archivo CSV guardado correctamente en {temp}")

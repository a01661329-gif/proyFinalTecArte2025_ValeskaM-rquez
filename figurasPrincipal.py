
import pandas as pd
from funciones import triangulo, rectangulo, circulo	#Llama las funciones definidas en fnciones.py

dataFile = pd.read_csv("figuras.csv")		#Lee el archivo que contiene las medidas de las figuras

print("Procesando figuras ...\n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():		#itera por cada fila
	if row['FIGURA'] == 't':		#decide qué fórmula usar según la figura
		area = triangulo(row['MEDIDA1'], row ['MEDIDA2'])
	elif row['FIGURA'] == 'r':
		area = rectangulo(row['MEDIDA1'], row ['MEDIDA2'])
	elif row['FIGURA'] == 'c':
		area = circulo(row['MEDIDA1'])
	print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
	print(f"Fila {index}: Area:{area}")		#imprime el resultado

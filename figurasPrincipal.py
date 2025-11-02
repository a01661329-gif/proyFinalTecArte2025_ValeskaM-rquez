
import pandas as pd
from funciones import triangulo, rectangulo, circulo

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
	if row['FIGURA'] == 't':
		area = triangulo(row['MEDIDA1'], row ['MEDIDA2'])
	elif row['FIGURA'] == 'r':
		area = rectangulo(row['MEDIDA1'], row ['MEDIDA2'])
	elif row['FIGURA'] == 'c':
		area = circulo(row['MEDIDA1'])
	print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
	print(f"Fila {index}: Area:{area}")

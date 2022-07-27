import sys
import os
from os import listdir
import time
import shutil

"""IMPORTANTE: El programa no está modularizado para simplificar la implementación."""

def RemoveDuplicates(listaDup):
	listaSinDup = list(dict.fromkeys(listaDup))
	return listaSinDup


def Crear_Ordenar(): # No paso parametros porque saco las variables desde principal.
	for tipo in range(len(listOfTypes)):	
		NewDir = (MainDir + f'/{listOfTypes[tipo]}')

		if os.path.exists(NewDir) == False: # Controlo que la carpeta no exista previamente
			os.mkdir(NewDir) # para que pueda ser creada sin errores

	for i in range(len(listOfFiles)):  # Muevo a cada carpeta el archivo que corresponda
		for z in range(len(listOfTypes)):
			if listOfFiles[i].endswith(listOfTypes[z]):
				shutil.move(MainDir + f'/{listOfFiles[i]}', MainDir + f'/{listOfTypes[z]}')

#---------------------------------------------PRINCIPAL----------------------------------------
try:
	MainDir = sys.argv[1]	# El formato en cmd es: 'python <nombrescript> <direccion> <parametro>'

	if len(str(sys.argv)) == 3:  # Con este bloque verifico si ingresó un parametro adicional
		if sys.argv [2] == '--check':
			if os.path.exists(MainDir):
				print('Si existe')
			else:
				print('no existe')
		else:
			print(f'Has ingresado un parámetro inexistente ({sys.argv[2]})')


	elif os.path.exists(str(MainDir)):
		listOfFiles = [file for file in listdir(MainDir)] # Contiene todos los archivos
		listOfTypes = []  # Contiene todas las extensiones de cada archivo

		print(f'\nSe han encontrado los siguientes archivos: {listOfFiles}')

		for archivo in listOfFiles:
			if '.' in archivo: # Si el nombre tiene un punto considero que lo que procede es su extensión.
				if archivo == 'desktop.ini': # El escritorio tiene este archivo que lo inicializa al bootear.
					continue

				auxVar = archivo.split('.')
				listOfTypes.append(auxVar[1])

		listOfTypes = RemoveDuplicates(listOfTypes)
		Crear_Ordenar()

		time.sleep(0.5)
		print('...')	# Si ya llego a este punto sin errores, los archivos se organizaron
		time.sleep(1)	#  de manera correcta. Con esto simulamos para el usuario un último análisis.
		print('Todos los archivos han sido organizados correctamente.')


	else:
		print(f'El directorio:  "{MainDir}" no existe')
		print('Si tu carpeta tiene espacios por favor escribe\
		 toda la direccion entre doble comilla (" ")')

except IndexError:
	print('Ha ocurrido un error con la cantidad de parámetros y no se ha realizado ningún cambio.')

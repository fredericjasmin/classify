import os
import time
import shutil
ExtensionsList = [[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
DirectorysList = ["Documentos","Presentaciones","Imagenes","Setups","Videos","Musica","Libros","Archivos Comprimidos"]
classifyExecutable = "Classify.exe"

# classifyMenu
def classifyMenu():
	while (True):
		option = int(input("\nClassify Menu\n\n1.Organizar (auto).\n2.Organizar (manual).\n3.Completo (fecha y formato).\n4.Organizar por fechas.\n5.Salir.\n\nroot@classify:~# "))
		if option == 1:
			classifyAyM(0)
		elif option == 2:
			classifyAyM(1)
		elif option == 3:
			classifyComplete()
		elif option == 4:
			classifyDate()
		elif option == 5:
			print("Hasta pronto...")
			break
		elif option == 6:
			classifyInformation()
		else:
			print("La opcion seleccionada no existe, intenta de nuevo...")

# classifyAyM
def classifyAyM(manual):
	if manual:
		path = input("Introduzca la ruta que desea organizar: ")
		num_carpetas = int(input("¿Cuantas carpetas quiere crear?"))
		i = 0
		while i<num_carpetas:
			carpeta = int(input("¿Que contiene la %dº carpeta?\n     1.Documentos\n     2.Presentaciones\n     3.Imagenes\n     4.Setups\n     5.Videos\n     6.Musica\n     7.Libros\n     8.Archivos Comprimidos\n-->"%(i+1)))
			DirectorysList[i] = DirectorysList[carpeta-1]
			ExtensionsList[i] = ExtensionsList[carpeta-1]
			i+=1
		i = 0
		while i<num_carpetas:
			valor = input("Introduzca el nombre de la carpeta de %s: "%DirectorysList[i])
			DirectorysList.append("\\" + valor)
			i = i+1
	else:
		path = os.getcwd()
		print("Organizando --> ", path)
		type_files = os.listdir(path)
	for folder_name in DirectorysList:
		if path[-1] == "\\":
			if not os.path.exists(path + folder_name):
				os.makedirs(path + folder_name)
		else:
			if not os.path.exists(path + "\\" + folder_name):
				os.makedirs(path + "\\" + folder_name)
	for c in range(len(DirectorysList)):
		for extension in ExtensionsList[c]:
			for file in type_files:
				if path[-1] == "\\":
					if extension in file and not os.path.exists(path + DirectorysList[c] + "\\" + file) and not file == classifyExecutable:
						shutil.move(path + file, path + DirectorysList[c] + "\\" + file)
				else:
					if extension in file and not os.path.exists(path + "\\" + DirectorysList[c] + "\\" + file) and not file == classifyExecutable:
						shutil.move(path + "\\" + file, path + "\\" + DirectorysList[c] + "\\" + file)
	completeMessage()
	classifyMenu()

# classifyComplete
def classifyComplete():
	ruta = input("Escriba la ruta que desea organizar (dejelo vacio y aprete enter dos veces si quiere la que esta por defecto): ")
	if ruta == "":
		path = os.getcwd()
	else:
		while (True):
			path = ruta
			if os.path.exists(path):
				break
	print(f"Organizando archivos de {path}, espere un momento...")
	type_files = os.listdir(path)
	punto = "."
	for folder_name in DirectorysList:
		if path[-1] == "\\":
			if not os.path.exists(path + folder_name):
				os.makedirs(path + folder_name)
		else:
			if not os.path.exists(path + "\\" + folder_name):
				os.makedirs(path + "\\" + folder_name)
	for c in range(len(DirectorysList)):
		for extension in ExtensionsList[c]:
			for file in type_files:
				if path[-1] == "\\":
					if extension in file and not os.path.exists(path + DirectorysList[c] + "\\" + file) and not file == classifyExecutable:
						shutil.move(path+file,path+DirectorysList[c]+"\\"+file)
				else:
					if extension in file and not os.path.exists(path + "\\" + DirectorysList[c] + "\\" + file) and not file == classifyExecutable:
						shutil.move(path + "\\" + file, path + "\\" + DirectorysList[c] + "\\" + file)
	for folder_name in DirectorysList:
		if ruta == "":
			path = os.getcwd()
		else:
			while (True):
				path = ruta
				if os.path.exists(path):
					break
		path = path + "\\" + folder_name
		archivos_enlistados = os.listdir(path)
		for file in archivos_enlistados:
			date = time.ctime(os.path.getctime(path + "\\" + file))
			year = date[-4:]
			if not os.path.exists(path + "\\" + year):
				os.makedirs(path + "\\" + year)
			else:
				pass
			if not os.path.exists(path + "\\" + year + "\\" + file) and not file == classifyExecutable and not file==year and punto in file:
				shutil.move(path + "\\" + file, path + "\\" + year + "\\" +file)
	completeMessage()
	classifyMenu()

# classifyDate
def classifyDate():
	punto = "."
	texto = "¿Esta seguro de que quiere ejecutar este comando?(s/n)"
	option = input(texto)
	if option == 's':
		path = os.getcwd()
		archivos_enlistados = os.listdir()
		print(archivos_enlistados)
		for file in archivos_enlistados:
			date = time.ctime(os.path.getctime(path + "\\" + file))
			year = date[-4:]
			if not os.path.exists(path + "\\" + year):
				os.makedirs(path + "\\" + year)
			else:
				pass
			if not os.path.exists(path + "\\" + year + "\\" + file) and not file == classifyExecutable and not file == year and punto in file:
				shutil.move(path + "\\" + file, path + "\\" + year + "\\" + file)
	elif option == 'n':
		classifyMenu()
	completeMessage()
	classifyMenu()

# classifyInformation
def classifyInformation():
	print("Hola, esta seccion incluye informacion sobre cada una de las opciones de este programa")
	print("1.Clasificador Completo: \n2.Clasificar Automaticamente: \n3.Clasificar Manualmente: ")
	option = int(input("¿Desea volver al menu de inicio?(s/n) "))
	if option == s:
		classifyMenu()

# completeMessage
def completeMessage():
	input("Completado con exito...")
	return

classifyMenu()
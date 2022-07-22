# MENU
def classifyMenu():
	menu = "\nClassify Menu\n\n1.Organizar (auto).\n2.Organizar (manual).\n3.Organizar por fechas.\n4.Completo (fecha y formato).\n5.Salir.\n\nroot@classify:~# "
	while (True):
		option = int(input(menu))
		if option == 1:
			clasificar(0)
		elif option == 2:
			clasificar(1)
		elif option == 3:
			classifyDate()
		elif option == 4:
			classifyComplete()
		elif option == 5:
			print("Hasta pronto...")
			break
		else:
			print("La opcion seleccionada no existe, intenta de nuevo...")

# COMPLETO
def classifyComplete():
	import os
	import time
	import shutil
	files=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	files_copy=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	ruta=input("Escriba la ruta que desea organizar (dejelo vacio y aprete enter dos veces si quiere la que esta por defecto): ")
	if ruta=="":
		path=os.getcwd()
	else:
		while (True):
			path=ruta
			if os.path.exists(path):
				break
	directorios=["Documentos","Presentaciones","Imagenes","Setups","Videos","Musica","Libros","Archivos Comprimidos"]
	print(f"Organizando archivos de {path}, espere un momento...")
	type_files = os.listdir(path)
	punto = "."
	for folder_name in directorios:
		if path[-1]=="\\":
			if not os.path.exists(path+folder_name):
				os.makedirs(path+folder_name)
		else:
			if not os.path.exists(path+"\\"+folder_name):
				os.makedirs(path+"\\"+folder_name)
	for c in range(len(directorios)):
		for extension in files[c]:
			for file in type_files:
				if path[-1]=="\\":
					if extension in file and not os.path.exists(path+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+file,path+directorios[c]+"\\"+file)
				else:
					if extension in file and not os.path.exists(path+"\\"+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+"\\"+file,path+"\\"+directorios[c]+"\\"+file)
	for folder_name in directorios:
		if ruta=="":
			path=os.getcwd()
		else:
			while (True):
				path=ruta
				if os.path.exists(path):
					break
		path=path+"\\"+folder_name
		archivos_enlistados=os.listdir(path)
		for file in archivos_enlistados:
			date=time.ctime(os.path.getctime(path+"\\"+file))
			year=date[-4:]
			if not os.path.exists(path+"\\"+year):
				os.makedirs(path+"\\"+year)
			else:
				pass
			if not os.path.exists(path+"\\"+year+"\\"+file) and not file=="Organizar fecha.exe" and not file==year and punto in file:
				shutil.move(path+"\\"+file,path+"\\"+year+"\\"+file)
	completeMessage()

def clasificar(manual):
	import os
	import shutil
	files=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	files_copy=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	if manual:
		path=input("Introduzca la ruta que desea organizar: ")
		num_carpetas=int(input("¿Cuantas carpetas quiere crear?"))
		i=0
		directorios=[]
		fichero=["documentos","presentaciones","imagenes","setups","videos","musica","libros","archivos comprimidos"]
		while i<num_carpetas:
			carpeta=int(input("¿Que contiene la %dº carpeta?\n     1.Documentos\n     2.Presentaciones\n     3.Imagenes\n     4.Setups\n     5.Videos\n     6.Musica\n     7.Libros\n     8.Archivos Comprimidos\n-->"%(i+1)))
			fichero[i]=fichero[carpeta-1]
			files[i]=files_copy[carpeta-1]
			i+=1
		i=0
		while i<num_carpetas:
			valor=input("Introduzca el nombre de la carpeta de %s: "%fichero[i])
			directorios.append("\\"+valor)
			i=i+1
	else:
		path=os.getcwd()
		directorios=["Documentos","Presentaciones","Imagenes","Setups","Videos","Musica","Libros","Archivos Comprimidos"]
	print("Organizando --> ",path)
	type_files = os.listdir(path)
	for folder_name in directorios:
		if path[-1]=="\\":
			if not os.path.exists(path+folder_name):
				os.makedirs(path+folder_name)
		else:
			if not os.path.exists(path+"\\"+folder_name):
				os.makedirs(path+"\\"+folder_name)
	for c in range(len(directorios)):
		for extension in files[c]:
			for file in type_files:
				if path[-1]=="\\":
					if extension in file and not os.path.exists(path+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+file,path+directorios[c]+"\\"+file)
				else:
					if extension in file and not os.path.exists(path+"\\"+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+"\\"+file,path+"\\"+directorios[c]+"\\"+file)
	completeMessage()

# ORGANIZAR POR FECHAS
def classifyDate():
	import os
	import time
	import shutil
	punto = "."
	texto = "¿Esta seguro de que quiere ejecutar este comando?(s/n)"
	option = input(texto)
	if option == 's':
		path = os.getcwd()
		archivos_enlistados = os.listdir()
		print(archivos_enlistados)
		for file in archivos_enlistados:
			date = time.ctime(os.path.getctime(path+"\\"+file))
			year = date[-4:]
			if not os.path.exists(path+"\\"+year):
				os.makedirs(path+"\\"+year)
			else:
				pass
			if not os.path.exists(path+"\\"+year+"\\"+file) and not file=="Organizar fecha.exe" and not file==year and punto in file:
				shutil.move(path+"\\"+file,path+"\\"+year+"\\"+file)
	elif option=='n':
		classifyMenu()
	completeMessage()

# Message of complete
def completeMessage():
	input("Completado con exito...")
	return

classifyMenu()
from pathlib import Path

#Forzamos que los archivos creados se vayan a la carpeta de "Jair" dentro del repositorio
carpetaGit = Path.cwd() / "Jair"

#Creamos una lista vacía para poder calcular la cantidad de archivos que hay
thislist = [""]

#Detectamos cuantos archivos .txt hay dentro de la carpeta "Jair"
for files in carpetaGit.glob("*txt*"):
    thislist.append(files)

#Asignamos una variable dependiendo cantidad de archivos .txt existentes
n = len(thislist)

#Input sobre lo que se vaya a escribir dentro del archivo .txt nuevo
msg = input("Mensaje: ")

#Para añadir a la carpeta Jair dentro del repositorio con el número siguiente de archivo .txt
my_dir = carpetaGit/f"{n}.txt"

#creamos el archivo con el mensaje del usuario
with open(my_dir, "w") as file:
    file.write(msg)

#Confirmamos el código
print("Tu archivo ", f"{n}.txt", " se ha creado.")

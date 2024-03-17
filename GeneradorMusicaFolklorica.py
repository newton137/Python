import urllib #permite descargas desde internet
import zipfile
import nottingham_util #clase de asistencia
import rnn

url = "http://www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip" #ubicación de descarga
urllib.urlretrieve(url,"dataset.zip") #"urlretrieve" descarga el dataset.zip

zip = zipfile.ZipFile(r"dataset.zip")
zip.extractall("data") #se extrae informacion y se guarda en el directorio "data"

nottingham_util.create_model()
rnn.train_model()
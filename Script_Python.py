import os #Operation System acceder a comandos para acceder a comandos para ejecutar en nuestro sistema operativo


###### carpeta data set ######
location = "C:/Users/ASUS/Downloads/DataOPS/Proyecto_Parcial/dataset" # los simbolos van mirando hacia la derecha

##### validar existencia de carpeta #####
if not os.path.exists(location): #Si no existe debo crear carpeta
    os.mkdir(location) #mkdir para crear directorio
else: #Si existe carpeta
    ## Si la carpeta existe borramos contenido.
    for root, dirs, files in os.walk(location, topdown=False): #indica la ruta raiz, si hay directorios dentro de la carpeta #Tambien indica si hay archivos
        for name in files:
            os.remove(os.path.join(root,name))  #Eliminar archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) #Eliminar archivos
            #Comentario final, la lógica es eliminar todo desde los archivos, luego directorios
            #Esto para ahorrar espacio siempre


##### Descargar dataset #####
from kaggle.api.kaggle_api_extended import KaggleApi

##### Autenticarnos #####
api = KaggleApi()
api.authenticate()
# Nuestro objetivo es automatizar

#print(api.dataset_list(search='')) Para ver que archivos tenemos disponibles
#Todo encerrado entre llaves eso es lista, 

#Método que descarga dataset
api.dataset_download_files('youssefismail20/olympic-games-1994-2024',path=location,force=True,quiet=False,unzip=True)
















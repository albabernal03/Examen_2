import pandas as pd
from pandas.core.frame import DataFrame #esta funcion se encarga de realizar la union de los datos




def dataset_conversiones():
    datos_conversion=pd.read_csv('conversiones (4).csv', sep=';')                                   
    datos_conversion= datos_conversion.dropna()
    print(datos_conversion)
dataset_conversiones()

def dataset_navegacion():
    datos_navegacion=pd.read_csv('navegacion (4) (1).csv', sep=';')
    datos_navegacion= datos_navegacion.dropna()
    print(datos_navegacion)
dataset_navegacion()

def separacion_datos_url(datos_navegacion):
    #En primer lugar creo lista vacias, que luego usaremos para hacer columnas en la tabla
    campaña=[]
    adgroup=[]
    advertisement=[]
    site_link=[]
    #Estos datos los vamos a extraer de las urls que se encuentran en la columna de url_landings
    urls = datos_navegacion['url_landings']

    for url in urls: #En esta parte se separan los datos de la url
        try:
             x= str(url).split('camp=') #Se separa la url por el caracter 'camp=', para acceder a este string delante hemos puesto lo de str(url)
             y= (x[1]).split('&') #ponemos x[1] para que nos deje solo lo que esta después de 'camp='
             campaña.append(y[0]) #Se añade a la lista de campaña tan solo lo que esta después de 'camp='
        except:
            campaña.append(0)
    datos_navegacion['id_campaña']=campaña #Añadimos una nueva columna al csv con los datos de campaña
    print(datos_navegacion) #mostramos casv con la nueva columna
    datos_navegacion.to_csv('navegacion_final', index= False) #guardamos el csv
#printeamos la funcion
separacion_datos_url('dataset_navegacion()')








 









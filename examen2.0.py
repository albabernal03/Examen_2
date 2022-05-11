
from numpy.lib.function_base import append #Esta libreria nos permite elementos a un array
import pandas as pd #Esta libreria nos permite trabajar con dataframes
#Una vez exportadas las librerias, definimos las funciones para cada dataset


#PASO 1: LEER LOS FICHEROS CSV
def Dataset_conversiones():
    datos_conversion=pd.read_csv('conversiones (4).csv', sep=';')
    return datos_conversion
print (Dataset_conversiones())

#Acabamos de ejecutarlo y vemos que nos da el resultado esperado

def Dataset_navegacion():
    datos_navegacion=pd.read_csv('navegacion (4) (1).csv', sep=';') 
    return datos_navegacion
print (Dataset_navegacion())

#PASO 2: SEPARAR LOS DATOS DE LA URL DE LOS DATOS DE LA CAMPAÑA, ADGROUP, ADVERTISEMENT, SITE_LINK
#hay fallos en alguna de las url pues el idUser y gclid en muchas de las lineas no coinciden con la de la url proporcionada, luego estos datos también los sacaremos de la url y crearemos columnas nuevas

def Separacion_datos_url(URL):

    #En primer lugar creo lista vacias, que luego usaremos para hacer columnas en la tabla
    campaña=[]
    adgroup=[]
    advertisement=[]
    site_link=[]
    id_user1=[]
    gclid_1=[]
    uuid_1=[]
    #Estos datos los vamos a extraer de las urls que se encuentran en la columna de url_landings
    
    for url in URL: #En esta parte se separan los datos de la url
        try:
            x= str(url).split('camp=') #Se separa la url por el caracter 'camp=', para acceder a este string delante hemos puesto lo de str(url)
            y= (x[1]).split('&') #ponemos x[1] para que nos deje solo lo que esta después de 'camp='
            campaña.append(y[0]) #Se añade a la lista de campaña tan solo lo que esta después de 'camp='
        except:
            campaña.append(0)
    for url in URL:
        try:
            x= str(url).split('adg=')
            y= (x[1]).split('&')
            adgroup.append(y[0])
        except:
            adgroup.append(0)
    for url in URL:
        try:
            x= str(url).split('ad=')
            y= (x[1]).split('&')
            advertisement.append(y[0])
        except:
            advertisement.append(0)
    for url in URL:
        try:
            x= str(url).split('sl=')
            y= (x[1]).split('&')
            site_link.append(y[0])
        except:
            site_link.append(0)
    for url in URL:
        try:
            x= str(url).split('idUser=')
            y= (x[1]).split('&')
            id_user1.append(y[0])
        except:
            id_user1.append(0)
    for url in URL:
        try:
            x= str(url).split('gclid=')
            y= (x[1]).split('&')
            gclid_1.append(y[0])
        except:
            gclid_1.append(0)
    for url in URL:
        try:
            x= str(url).split('uuid=')
            y= (x[1]).split('&')
            uuid_1.append(y[0])
        except:
            uuid_1.append(0)

#Con esto vamos a creasr el nuevo csv con los datos separados
    Datos= {'Campaña':campaña, 'Adgroup':adgroup, 'Advertisement':advertisement, 'Site_link':site_link, 'id_user':id_user1, 'gclid':gclid_1, 'uuid':uuid_1, 'ts':Dataset_navegacion()['ts']} #Se crea un diccionario con los datos de la url
    navegacion_final=pd.DataFrame(Datos) #Se crea un dataframe con los datos de la url
    navegacion_final.to_csv('navegacion_final.csv', sep=';')
Separacion_datos_url(Dataset_navegacion()['url_landing'])

#PASO 3: ELIMINAMOS LOS USUARIOS DONDE SE REPITE LOS DATOS DEL ID_USER, GCLID, UUID

def Eliminacion_datos_repetidos(navegacion_final):
    navegacion_final=pd.read_csv('navegacion_final.csv', sep=';')
    navegacion_final=navegacion_final.drop_duplicates(subset=['id_user', 'gclid', 'uuid'], keep='first')
    navegacion_final.to_csv('navegacion_final.csv', sep=';')
Eliminacion_datos_repetidos()

#DENTRO DE ESTE EJERCICIO ENCONTRAMOS OTRO APARTADO QUE NOS PIDE ORDENAR POR LA COLUMNA 'TS'

def Ordenacion_por_ts(navegacion_final):
    navegacion_final=pd.read_csv('navegacion_final.csv', sep=';')
    navegacion_final=navegacion_final.sort_values(by='ts')
    navegacion_final.to_csv('navegacion_final.csv', sep=';')
Ordenacion_por_ts()














    






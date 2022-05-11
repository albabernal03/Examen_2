
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

def Eliminacion_datos_repetidos():
    navegacion_final=pd.read_csv('navegacion_final.csv', sep=';')
    navegacion_final=navegacion_final.drop_duplicates(subset=['id_user', 'gclid', 'uuid'], keep='first')
    navegacion_final.to_csv('navegacion_final.csv', sep=';')
Eliminacion_datos_repetidos()

# A continuacion hacemos una funcion que ordena los datos por fecha de navegacion
def Ordenacion_por_ts():
    navegacion_final=pd.read_csv( 'navegacion_final.csv', sep=';')
    navegacion_final=navegacion_final.sort_values('ts', ascending=False)
    navegacion_final.to_csv('navegacion_final.csv', sep=';')
Ordenacion_por_ts()

#PASO 4: UNIMOS AMBAS CSV
#4.1 Antes de unir limpiamos el dataframe de conversiones
#ahora vamos a limpiar el csv de conversiones 
def Limpiar_conversiones(dato=[]):
    for i in range(len(dato)): #en este bucle vamos a sustituir los valores 0 por None por blancos
        if dato[i]=='None': 
            dato[i]= ''
    return dato
#Aplicamos la funcion a las columnas 'id_user' y 'gclid'
Limpiar_conversiones(Dataset_conversiones()['id_user'])
Limpiar_conversiones(Dataset_conversiones()['gclid'])
conversion_final = pd.DataFrame({'id_user':Limpiar_conversiones(Dataset_conversiones()['id_user']), 'gclid':Limpiar_conversiones(Dataset_conversiones()['gclid']), 'date':Dataset_conversiones()['date'], 'hour':Dataset_conversiones()['hour'], 'id_lead':Dataset_conversiones()['id_lead'], 'lead_type': Dataset_conversiones()['lead_type'], 'result':Dataset_conversiones()['result']})
conversion_final.to_csv('conversion_final.csv', sep=';')

#4.2 Ahora vamos a unir los datos de navegacion y conversiones

def Conversiones(data_1, data_2):
    conversion= []
    for i in data_1:
        if i in data_2:
            conversion.append(1)
        else:
            conversion.append(0)
    return conversion
#Aplicamos la funcion a las columnas 'id_user' y 'gclid'
navegacion_final=pd.read_csv('navegacion_final.csv', sep=';')
conversion_final=pd.read_csv('conversion_final.csv', sep=';')
conversiones_por_id= Conversiones(navegacion_final['id_user'], conversion_final['id_user'])
conversiones_por_gclid=Conversiones(navegacion_final['gclid'], conversion_final['gclid'])
#creamos un csv con la union de los datos
union={'Campaña':navegacion_final['Campaña'],'Adgroup':navegacion_final['Adgroup'], 'Advertisement':navegacion_final['Advertisement'],'Site_link': navegacion_final['Site_link'], 'id_user_navegacion': navegacion_final['id_user'], 'gclid_navegacion':navegacion_final['gclid'], 'uuid': navegacion_final['uuid'], 'ts': navegacion_final['ts'], 'id_user_conversiones': conversion_final['id_user'], 'gclid_conversiones': conversion_final['gclid'], 'hour': conversion_final['hour'], 'date': conversion_final['date'], 'id_lead': conversion_final['id_lead'], 'lead_type': conversion_final['lead_type'], 'result': conversion_final['result'] }
union_final=pd.DataFrame(union)
csv_union= union_final.assign(conversiones_por_gclid= conversiones_por_gclid, conversiones_por_id=conversiones_por_id)
csv_union.to_csv('union_final.csv', sep=';')


#PASO 5: RESPONDEMOS A LAS PREGUNTAS
#5.1: Cuantos id_user hay en total
def Id_user_total():
    datos_navegacion=pd.read_csv('navegacion (4) (1).csv', sep=';')
    total=datos_navegacion['id_User'].count
    return total
print()





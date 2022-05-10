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
#hay fallos en alguna de las url pues el idUser y gclid muchas de oas lineas no coinciden con la de la url proporcionada, luego estos datos también los sacaremos de la url y crearemos columnas nuevas

def Separacion_datos_url(datos_navegacion):
    #En primer lugar creo lista vacias, que luego usaremos para hacer columnas en la tabla
    campaña=[]
    adgroup=[]
    advertisement=[]
    site_link=[]
    id_user1=[]
    gclid_1=[]
    #Estos datos los vamos a extraer de las urls que se encuentran en la columna de url_landings
    urls = datos_navegacion['url_landing']
    for url in urls: #En esta parte se separan los datos de la url
        try:
            x= str(url).split('camp=') #Se separa la url por el caracter 'camp=', para acceder a este string delante hemos puesto lo de str(url)
            y= (x[1]).split('&') #ponemos x[1] para que nos deje solo lo que esta después de 'camp='
            campaña.append(y[0]) #Se añade a la lista de campaña tan solo lo que esta después de 'camp='
        except:
            campaña.append(0)
    for url in urls:
        try:
            x= str(url).split('adg=')
            y= (x[1]).split('&')
            adgroup.append(y[0])
        except:
            adgroup.append(0)
    for url in urls:
        try:
            x= str(url).split('ad=')
            y= (x[1]).split('&')
            advertisement.append(y[0])
        except:
            advertisement.append(0)
    for url in urls:
        try:
            x= str(url).split('sl=')
            y= (x[1]).split('&')
            site_link.append(y[0])
        except:
            site_link.append(0)
    for url in urls:
        try:
            x= str(url).split('idUser=')
            y= (x[1]).split('&')
            id_user1.append(y[0])
        except:
            id_user1.append(0)
    for url in urls:
        try:
            x= str(url).split('gclid=')
            y= (x[1]).split('&')
            gclid_1.append(y[0])
        except:
            gclid_1.append(0)


    #Añadimos las columnas a la tabla
    datos_navegacion['id_campaña']=campaña
    datos_navegacion['id_adgroup']=adgroup
    datos_navegacion['id_advertisement']=advertisement
    datos_navegacion['id_site_link']=site_link
    datos_navegacion['id_user_1']=id_user1
    datos_navegacion['gclid_1']=gclid_1
    print(datos_navegacion)
print (Separacion_datos_url(Dataset_navegacion()))

def navegacion_final():
    datos_navegacion_final=pd.read_csv('navegacion_final.csv', sep=';')
    datos_navegacion_final.pop(['id_user'])
    datos_navegacion_final.pop(['gclid'])
    print(datos_navegacion_final)
    datos_navegacion_final.to_csv('navegacion_final.csv', index= False)
print (navegacion_final(Separacion_datos_url('datos_navegacion_final')))





    






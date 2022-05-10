import pandas as pd
from pandas.core.frame import DataFrame #esta funcion se encarga de realizar la union de los datos




def Dataset_conversiones():
    datos_conversion=pd.read_csv('conversiones (4).csv', sep=';')
    print(datos_conversion)                                
Dataset_conversiones()

def Dataset_navegacion():
    datos_navegacion=pd.read_csv('navegacion (4) (1).csv', sep=';')
    datos_navegacion= datos_navegacion.dropna(subset=['url_landing'], inplace= True)
    print(datos_navegacion)
Dataset_navegacion()   

def Separacion_datos_url(datos_navegacion):
    #En primer lugar creo lista vacias, que luego usaremos para hacer columnas en la tabla
    campaña=[]
    adgroup=[]
    advertisement=[]
    site_link=[]
    #Estos datos los vamos a extraer de las urls que se encuentran en la columna de url_landings
    urls = datos_navegacion
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
    #Se crea una tabla con los datos separados
    datos_navegacion['id_campaña']=campaña
    datos_navegacion['id_adgroup']=adgroup
    datos_navegacion['id_advertisement']=advertisement
    datos_navegacion['id_site_link']=site_link
    print(datos_navegacion)
    datos_navegacion.to_csv('navegacion_final.csv', sep=';')









 









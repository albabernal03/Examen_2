import pandas as pd
datos_navegacion=pd.read_csv('navegacion (4) (1).csv', sep=';')
datos_navegacion= datos_navegacion.dropna()
print(datos_navegacion)

campaña=[]
adgroup=[]
advertisement=[]
site_link=[]

urls = datos_navegacion['url_landing']

for url in urls: 
    try:
        x= str(url).split('camp=') #Se separa la url por el caracter 'camp=', para acceder a este string delante hemos puesto lo de str(url)
        y= (x[1]).split('&') #ponemos x[1] para que nos deje solo lo que esta después de 'camp='
        campaña.append(y[0]) #Se añade a la lista de campaña tan solo lo que esta después de 'camp='
    except:
        campaña.append(0)

    datos_navegacion['id_campaña']=campaña #Añadimos una nueva columna al csv con los datos de campaña
    print(datos_navegacion) #mostramos casv con la nueva columna
    datos_navegacion.to_csv('navegacion_final', index= False) #guardamos el csv
  



 
    
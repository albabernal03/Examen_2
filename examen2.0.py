from numpy.lib.function_base import append #Esta libreria nos permite elementos a un array
import pandas as pd #Esta libreria nos permite trabajar con dataframes

#Una vez exportadas las librerias, definimos las funciones para cada dataset

def Dataset_conversiones():
    datos_conversion=pd.read_csv('conversiones (4).csv', sep=';')
    return datos_conversion
print (Dataset_conversiones())

#Acabamos de ejecutarlo y vemos que nos da el resultado esperado



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


def Ordenacion_por_ts():
    navegacion_final=pd.read_csv('navegacion_final.csv', sep=';')
    navegacion_final=navegacion_final.sort_values(by='ts')
    navegacion_final.to_csv('navegacion_final.csv', sep=';')
Ordenacion_por_ts()

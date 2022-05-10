import re
from numpy import shares_memory
from numpy.lib.function_base import append
import pandas as pd
from pandas import tseries

conversiones = pd.read_csv("conversiones (4).csv", sep = ";")
navegacion = pd.read_csv("navegacion (4) (1).csv", sep = ";")


campaña = []
adg = []
adv = []
sl = []
urls = navegacion["url_landing"]
#Valor del id campaña
for url in urls:
    try:
        esp = str(url).split("camp=")
        bueno = esp[1].split("&")
        campaña.append(bueno[0])
    except:
        campaña.append(0)
#Valor del id del adgroup
for url in urls:
    try:
        esp = str(url).split("adg=")
        bueno = esp[1].split("&")
        adg.append(bueno[0])
    except:
        adg.append(0)
#valor del adv
for url in urls:
    try:
        esp = str(url).split("adv=")
        bueno = esp[1].split("&")
        adv.append(bueno[0])
    except:
        adv.append(0)
#valor del sl
for url in urls:
    try:
        esp = str(url).split("sl=")
        bueno = esp[1].split("&")
        sl.append(bueno[0])
    except:
        sl.append(0)
navegacion["id_camp"] = campaña
navegacion["id_adg"] = adg
navegacion["id_adv"] = adv
navegacion["id_sl"] = sl

print(navegacion)
#Esto es para guardar el fichero final, comentar si no se usa
navegacion.to_csv("navegacion_final.csv", index = False)

import pandas as pd #pandas para trabajar sobre DataFrames
import matplotlib.pyplot as plt #herramienta de ploteo para python
import seaborn as sns #sofisticacion de plt
import re
from datetime import datetime

def tipo_datos(df): #verifica el tipo de datos y devuelve todos los tipos de datos por cada columna y nulos
    dic = {'Columna': [], 'Tipo_datos': [], '%_nulos': [], 'Nulos': [], 'Largo':[]}
    for column in df.columns: #itera sobre columnas
        tipos_de_datos = df[column].apply(lambda x: type(x).__name__).unique() #nos devuelve sobre la columna los tipos de datos sin repeticion
        isnap = df[column].isna().sum()/df[column].shape[0]*100 # calcula el porcentaje de nans 
        isna = df[column].isna().sum() #calcula la cantidad de nans
        largo_datos = df[column].apply(lambda x: len(str(x))).unique()
        dic['Columna'].append(column) # adjunta datos
        dic['Tipo_datos'].append(tipos_de_datos)
        dic['%_nulos'].append(isnap)
        dic['Nulos'].append(isna)
        dic['Largo'].append(largo_datos)
    
    datf = pd.DataFrame(dic) #genera dataframe para devolver

    return datf

def indentificar_duplicados(df,columna): #identifica los duplicados y los muestra
    duplicados = df[df.duplicated(subset=columna,keep=False)]
    return duplicados
    
def convertir_proper(valor):
    if isinstance(valor,str):
        valor = valor.strip()
        valor = valor.title()
        return valor
    else:
        return valor
    
def porcentaje_repr(df,column):
    dic = {'Valor': [], 'Cantidad': [], 'Porcentaje': []}
    df_count = df[column].value_counts()
    for i,v in df_count.items():
        dic['Valor'].append(i)
        dic['Cantidad'].append(v)
        dic['Porcentaje'].append(round((v/df_count.sum()*100),2))
    dfs = pd.DataFrame(dic)
    return dfs

def horas(valor):
    try:
        return pd.to_datetime(valor, format='%H:%M:%S').time()
    except:
        return 'Sin Dato'